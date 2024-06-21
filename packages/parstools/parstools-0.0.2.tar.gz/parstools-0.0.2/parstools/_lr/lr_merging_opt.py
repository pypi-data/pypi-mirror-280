"""Kernel-merging LR(1) parser construction.


References
==========

* David Pager
  "A practical general method for
   constructing LR(k) parsers"
  Acta Informatica
  Volume 7, pages 249--268, 1977
  <https://doi.org/10.1007/BF00290336>
"""
import collections as _cl
import collections.abc as _abc
import functools as _ft
import itertools as _itr
import re
import textwrap as _tw
import time
import typing as _ty

import parstools._ff as _ff
import parstools._grammars as _grm
import parstools._lr.parser as _p
import parstools._lr.utils as _lu
import parstools._utils as _u


_Grammar = _grm.Grammar
_Production = _grm.Production
Result = _p.Result


class _Dot(
        _ty.NamedTuple):
    symbol: str
    done: tuple[str, ...] = tuple()
    rest: tuple[str, ...] = tuple()
    lookaheads: set[str] | None = None

    def __str__(
            self
            ) -> str:
        return _pformat_dot(self)


def _pformat_dot(
        dot:
            _Dot,
        unicode:
            bool=True
        ) -> str:
    """Return text describing `dot`."""
    _u.assert_not_in(' . ', dot.done)
    _u.assert_not_in(' . ', dot.rest)
    def pformat(symbols):
        return ' '.join(map(
            _grm.format_empty_symbol, symbols))
    done = pformat(dot.done)
    rest = pformat(dot.rest)
    if done:
        done = f' {done}'
    VERTICAL_LINE = '\u2502'
    if dot.lookaheads:
        WIDTH = 100
        lexemes = ', '.join(sorted(
            dot.lookaheads))
        text = '{' + lexemes + '}'
        lookaheads = _tw.fill(
            text,
            width=WIDTH)
    else:
        lookaheads = '{ }'
    if unicode:
        subseteq = '\u2287'
    else:
        subseteq = r'\subseteq'
    start = (
        f'{dot.symbol} {subseteq} '
        f'{done} . {rest}  {VERTICAL_LINE} ')
    first_line, *other_lines = lookaheads.splitlines()
    indent_width = 1 + len(start)
    indent = indent_width * '\x20'
    other_lines = '\n'.join(other_lines)
    other_lines = _tw.indent(
        other_lines,
        prefix=indent)
    return (
        f'{start}{first_line}\n'
        f'{other_lines}')


_Kernel: _ty.TypeAlias = set[_Dot]
_Core: _ty.TypeAlias = set[_Dot]
_Kernels: _ty.TypeAlias = set[_Kernel]


def make_parser(
        grammar:
            _Grammar,
        cache_filename:
            str |
            None=None
        ) -> _p.Parser:
    """Return LR-merged parser.

    If `cache_filename is not None`,
    use to store parser, attempting to
    load the parser first from file (JSON).
    """
    parser = _p.check_parser_cache(
        grammar, cache_filename)
    if parser is not None:
        return parser
    parser = make_lr_1_tables(grammar)
    _p.dump_parser_cache(
        grammar, parser, cache_filename)
    return parser


def make_lr_1_tables(
        grammar:
            _Grammar
        ) -> _p.Parser:
    t1 = time.perf_counter()
    grammar = _lu.add_root_equation(grammar)
    first_sets = _ff.compute_first_sets(
        grammar.equations)
    nodes, edges = _collect_merged_nodes(
        grammar, first_sets)
    all_kernels = all(map(
        _is_kernel, nodes))
    if not all_kernels:
        raise AssertionError(all_kernels)
    # text = _lu.pformat_states(nodes)
    # print(text)
    actions = _make_lr_1_action_table(
        edges, grammar, first_sets)
    initial = _make_init_state(
        grammar.root_symbol)
    t2 = time.perf_counter()
    dt = t2 - t1
    print(f'parser computed in: {dt:1.2f} sec')
    return _p.Parser(
        initial, actions)


def _make_lr_1_action_table(
        edges:
            dict[
                _Kernel,
                _Kernels],
        grammar:
            _Grammar,
        first_sets:
            dict
        ) -> dict[
            tuple[_Kernel, str],
            _lu.Action]:
    """Return parser-actions table."""
    # compute actions
    actions = _u.MonotonicDict()
    for node, succ in edges.items():
        _make_lr_1_actions_at_node(
            node, succ, actions,
            grammar, first_sets)
    # check actions for next-node
    states = {
        node
        for node, _ in actions}
    for key, action in actions.items():
        next_state = action.state
        if next_state is None:
            continue
        if next_state not in states:
            print(_lu.pformat_state(next_state))
            print(f'{edges[next_state] = }')
            raise AssertionError()
    return dict(actions)


def _make_lr_1_actions_at_node(
        node:
            _Kernel,
        edge_successors:
            _Kernels,
        actions:
            dict,
        grammar:
            _Grammar,
        first_sets:
            dict
        ) -> None:
    """Add edges from `node`."""
    has_action = (
        edge_successors or
        set(_lu.final_items(node)))
    if not has_action:
        print(_lu.pformat_state(node))
        raise AssertionError()
    # shifts
    for next_node in edge_successors:
        item = _lu.pick_kernel_item(
            next_node)
        symbol = item.done[-1]
        action = _lu.Action(
            state=next_node)
        _add_lr_action(
            node, symbol, action, actions)
    # reductions
    for item in _lu.final_items(node):
        equation = _lu.production_of_dot(item)
        for symbol in item.lookaheads:
            action = _lu.Action(
                equation=equation)
            _add_lr_action(
                node, symbol, action, actions)
    # print(actions)


def _add_lr_action(
        node:
            _Kernel,
        symbol:
            str,
        action:
            _lu.Action,
        actions:
            dict
        ) -> None:
    """Add action, with error message otherwise."""
    key = (node, symbol)
    other = actions.get(key)
    add = (
        other is None or
        (action.state is not None and
         action.state == other.state) or
        (action.equation is not None and
         action.equation == other.equation))
    if add:
        actions[key] = action
        return
    if action.state and other.state:
        raise AssertionError(
            action, other)
    if action.equation and other.equation:
        raise ValueError(
            'reduce-reduce overlap: '
            'reduce using production: '
            f'`{action.equation}`, or '
            'reduce using production: '
            f'`{other.equation}`')
    if action.state:
        node = action.state
        equation = other.equation
    else:
        node = other.state
        equation = action.equation
    raise ValueError(
        'shift-reduce overlap: '
        f'shift symbol: `{symbol}`, or '
        'reduce using production: '
        f'`{equation}`')


def _collect_merged_nodes(
        grammar:
            _Grammar,
        first_sets:
            dict
        ) -> tuple[
            _Kernels,
            dict[
                _Kernel,
                _Kernels]]:
    """Return coalesced LR(1) graph."""
    init_node = _make_init_state(
        grammar.root_symbol)
    symbol_to_successor: dict[
        str, set[_Dot]
        ] = _cl.defaultdict(set)
    replaced = dict()
    nodes = set()
    edges = _cl.defaultdict(set)
    pred = _cl.defaultdict(set)
    todo = {init_node}
    while todo:
        more_todo = set()
        for node in todo:
            if node in nodes or node in replaced:
                continue
            successors = _successors_of_lr_1_node(
                node, nodes, edges, pred,
                symbol_to_successor,
                grammar, first_sets,
                replaced)
            more_todo.update(successors)
            nodes.add(node)
        todo = more_todo
    print(f'{len(nodes) = }')
    print(f'{len(replaced) = }')
    nodes = nodes.difference(replaced)
    print(f'after difference: {len(nodes) = }')
    # rm to-merge nodes
    reachable_nodes = _reachable({init_node}, edges)
    print(f'{len(reachable_nodes) = }')
    edges = _replace_edges(
        edges, replaced)
    _assert_out_edges(edges)
    return nodes, edges


def _assert_out_edges(
        edges):
    """Assert each node has actions.

    A node either has edges,
    or only reduces.
    """
    items = edges.items()
    for node, out_edges in items:
        if out_edges:
            continue
        reduce = _kernel_only_reduces(
            node)
        if reduce:
            continue
        raise AssertionError(
            node, out_edges)


def _kernel_only_reduces(
        kernel):
    """Return `True` if no shift."""
    return all(
        not item.rest
        for item in kernel)


def _successors_of_lr_1_node(
        kernel:
            _Kernel,
        nodes:
            set[_Kernel],
        edges:
            dict[
                _Kernel,
                _Kernels],
        pred:
            dict[
                _Kernel,
                _Kernels],
        symbol_to_successor:
            dict[
                str,
                set[_Kernel]],
        grammar:
            _Grammar,
        first_sets:
            dict,
        replaced:
            dict
        ) -> _abc.Iterable:
    """Nodes at endpoints of edges from node."""
    edges[kernel] = set()
    successors = set()
    # closure = _kernel_closure(
    #     kernel, grammar, first_sets)
    # parts = _partition_kernel_by_shift(
    #     closure)
    # for shift, part in parts.items():
    #     kernel_1 = _shift_dot_in_kernel(part)
    parts = _kernel_closure(
        kernel, grammar, first_sets)
    for shift, kernel_1 in parts.items():
        # if kernel_1 in replaced:
        #     merged = replaced[kernel_1]
        #     while merged in replaced:
        #         merged = replaced[merged]
        #     edges[kernel].add(merged)
        #     pred[merged].add(kernel)
        #     break
        succ = symbol_to_successor[shift]
        for kernel_2 in succ:
            # merge = _mergeable_kernels(
            #     kernel_1, kernel_2)
            merged = _merge_kernels(
                kernel_1, kernel_2)
            if merged is None:
                # print('not merging (1)')
                continue
            # print('merging')
            # `kernel_2` can have been added
            # to `succ` in a previous iteration
            # of the outer `for` loop
            # if kernel_2 in nodes:
            #     nodes.remove(kernel_2)
            edges[kernel].add(merged)
            pred[merged].add(kernel)
            if merged == kernel_2:
                break
            succ.remove(kernel_2)
            succ.add(merged)
            replaced[kernel_2] = merged
            successors.add(merged)
            # not the root node ?
            if kernel_2 in pred:
                pred[merged] |= pred.pop(kernel_2)
            # else:
            #     assert kernel_2 == init_node
            for node in pred[merged]:
                edges[node].discard(kernel_2)
                edges[node].add(merged)
            # _check_successors_of_merged(
            #     kernel_1, kernel_2, merged,
            #     symbol_to_successor,
            #     nodes, edges, grammar, first_sets,
            #     successors)
            break
        else:
            # print('not merging (2)')
            succ.add(kernel_1)
            successors.add(kernel_1)
            edges[kernel].add(kernel_1)
            pred[kernel_1].add(kernel)
    return successors


def _kernel_closure(
        kernel:
            _Kernel,
        grammar:
            _Grammar,
        first_sets:
            dict
        ) -> dict[
            str, _Kernel]:
    """Return kernels from closure."""
    # grouped = _group_items(kernel)
    # assert kernel == grouped
    core_to_ctx = _cl.defaultdict(set)
    for dot_ctx in kernel:
        if not dot_ctx.rest:
            continue
        key = (
            dot_ctx.symbol,
            dot_ctx.done,
            dot_ctx.rest)
        core_to_ctx[key].update(
            dot_ctx.lookaheads)
    todo = {
        (item.rest, item.lookaheads)
        for item in kernel
        if item.rest}
    while todo:
        more_items = set()
        for rest, lookaheads in todo:
            if not rest:
                continue
            shift, *rest = rest
            # leaf ?
            if shift in grammar.leafs:
                continue
            # `shift` is nonleaf
            ctx = _update_lookaheads(
                lookaheads, tuple(rest),
                grammar, first_sets)
            eqs = grammar.groups[shift]
            for eq in eqs:
                key = (
                    eq.symbol,
                    tuple(),
                    eq.expansion)
                symbols = core_to_ctx[key]
                n = len(symbols)
                symbols.update(ctx)
                if len(symbols) == n:
                    continue
                # lookaheads changed
                sym = frozenset(symbols)
                more_items.add(
                    (eq.expansion, sym))
        todo = more_items
    # group items by shift-symbol
    parts = _cl.defaultdict(set)
    items = core_to_ctx.items()
    for (symbol, done, rest), ctx in items:
        if not rest:
            continue
        # shift dot
        shift, *rest = rest
        done = (*done, shift)
        item = _Dot(
            symbol=symbol,
            done=done,
            rest=tuple(rest),
            lookaheads=frozenset(ctx))
        parts[shift].add(item)
    parts = {
        k: frozenset(v)
        for k, v in parts.items()}
    return parts
    # closure = {
    #     _Dot(
    #         symbol=symbol,
    #         done=done,
    #         rest=rest,
    #         lookaheads=frozenset(ctx))
    #     for (symbol, done, rest), ctx in
    #         core_to_ctx.items()}
    # closure_ = _kernel_closure_(
    #     kernel, grammar, first_sets)
    # assert closure == closure_, (
    #     closure - closure_)
    # return closure


def _update_lookaheads(
        lookaheads:
            set[str],
        rest:
            tuple[str],
        grammar:
            _Grammar,
        first_sets:
            dict
        ) -> set[str]:
    """Return lookahead symbols.

    These are the leaf symbols that occur
    first in the sequences formed by
    appending to `rest` each element of
    `lookaheads`.
    """
    ctx = set()
    for symbol in rest:
        current = first_sets[symbol]
        ctx.update(current)
        if _ff._NULL not in current:
            break
    else:
        ctx.update(lookaheads & grammar.leafs)
        for symbol in lookaheads & grammar.nonleafs:
            ctx.update(first_sets[symbol])
    ctx -= grammar.nonleafs
    return frozenset(ctx)


def _group_items(
        dots:
            set[_Dot]
        ) -> set[_Dot]:
    """Return config-groups, each a dot."""
    dot_to_ctx = _cl.defaultdict(set)
    for item in dots:
        item_core = _dot_core(item)
        dot_to_ctx[item_core].update(
            item.lookaheads)
    items = set()
    pairs = dot_to_ctx.items()
    for item_core, ctx in pairs:
        item = _Dot(
            symbol=item_core.symbol,
            done=item_core.done,
            rest=item_core.rest,
            lookaheads=frozenset(ctx))
        items.add(item)
    return items


def _merge_kernels(
        kernel_1,
        kernel_2
        ) -> _Kernel | None:
    """Merge kernels when no overlaps arise."""
    if len(kernel_1) != len(kernel_2):
        return None
    merged = _cl.defaultdict(set)
    for dot in kernel_1:
        key = (
            dot.symbol,
            dot.done,
            dot.rest)
        merged[key].update(dot.lookaheads)
    for dot in kernel_2:
        key = (
            dot.symbol,
            dot.done,
            dot.rest)
        merged[key].update(dot.lookaheads)
    same_len = (
        len(merged) == len(kernel_1) and
        len(merged) == len(kernel_2))
    if not same_len:
        return None
    not_mergeable = (
        not _sets_disjoint(
            merged.values()) and
        _sets_disjoint(
            dot.lookaheads
            for dot in kernel_1) and
        _sets_disjoint(
            dot.lookaheads
            for dot in kernel_2))
    if not_mergeable:
        return None
    merged = frozenset({
        _Dot(
            symbol=key[0],
            done=key[1],
            rest=key[2],
            lookaheads=frozenset(ctx))
        for key, ctx in
            merged.items()})
    return merged


def _sets_disjoint(
        sets):
    accum = set()
    count = 0
    for value in sets:
        count += len(value)
        accum.update(value)
        if count != len(accum):
            return False
    return True


def _reachable(
        initial_nodes,
        edges):
    """Return reachable nodes."""
    reachable = set()
    todo = set(initial_nodes)
    while todo:
        node = todo.pop()
        succ = edges[node]
        todo |= succ - reachable
        reachable.add(node)
    return reachable


def _replace_edges(
        edges:
            dict,
        replaced
        ) -> dict:
    """Replace nodes in edges."""
    print(f'{len(edges)} nodes before projection')
    node_map = dict()
    for u in _itr.chain(edges, replaced):
        v = u
        while v in replaced:
            v = replaced[v]
        node_map[u] = v
    edges_ = dict()
    for u, succ in edges.items():
        v = node_map[u]
        v_succ = {
            node_map[w]
            for w in succ}
        edges_[v] = v_succ
    for succ in edges_.values():
        for w in succ:
            if w in edges_:
                continue
            text = _lu.pformat_state(w)
            raise AssertionError(text)
    print(f'{len(edges_)} nodes after projection')
    return edges_


def _is_kernel(
        items:
            _Kernel
        ) -> bool:
    """Return `True` if a kernel."""
    kernel = set(_lu.kernel_items(
        items))
    return (kernel == items)


def _dot_core(
        dotted:
            _Dot
        ) -> _Dot:
    """Return dotted without lookaheads."""
    return _Dot(
        symbol=dotted.symbol,
        done=dotted.done,
        rest=dotted.rest)


def _make_init_state(
        root_symbol:
            str
        ) -> set:
    """Return kernel of initial state.

    Config-groups are each represented by
    one `_Dot` item.
    """
    expansion = (root_symbol,)
    lookaheads = frozenset({_lu._END})
    item = _Dot(
        symbol=_lu._ROOT,
        rest=expansion,
        lookaheads=lookaheads)
    return frozenset({item})
