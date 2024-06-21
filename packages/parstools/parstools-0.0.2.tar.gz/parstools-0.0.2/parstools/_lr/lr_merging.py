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
import parstools._introspection as _intro
import parstools._lr.lr as _lr
import parstools._lr.parser as _p
import parstools._lr.utils as _lu
import parstools._tla_grammars as _tla_grm
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


def make_lr_1_tables(
        grammar:
            _Grammar
        ) -> dict:
    t1 = time.perf_counter()
    grammar = _lu.add_root_equation(grammar)
    first_sets = _ff.compute_first_sets(
        grammar.equations)
    nodes, edges = _collect_merged_nodes(
        grammar, first_sets)
    all_kernels = all(map(
        _is_kernel, nodes))
    print(f'{all_kernels = }')
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
        actions[node, symbol] = _lu.Action(
            state=next_node)
    # reductions
    for item in _lu.final_items(node):
        equation = _lu.production_of_dot(item)
        for symbol in item.lookaheads:
            actions[node, symbol] = _lu.Action(
                equation=equation)
    # print(actions)


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
                replaced, init_node)
            more_todo.update(successors)
            nodes.add(node)
        todo = more_todo
    print(f'{len(nodes) = }')
    print(f'{len(replaced) = }')
    nodes = nodes.difference(replaced)
    print(f'after difference: {len(nodes) = }')
    # rm to-merge nodes
    reachable_nodes = _reachable(init_node, edges)
    print(f'{len(reachable_nodes) = }')
    edges = _replace_edges(
        edges, replaced)
    _assert_out_edges(edges)
    return nodes, edges


def _assert_out_edges(
        edges):
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
            dict,
        init_node
        ) -> _abc.Iterable:
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
        ) -> _Kernel:
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


def _kernel_closure_simple(
        kernel:
            _Kernel,
        grammar:
            _Grammar,
        first_sets:
            dict
        ) -> _Kernel:
    # grouped = _group_items(kernel)
    # assert kernel == grouped
    closure = set(kernel)
    todo = set(kernel)
    while todo:
        more_items = set()
        for item in todo:
            if not item.rest:
                continue
            shift, *rest = item.rest
            # leaf ?
            if shift in grammar.leafs:
                continue
            # `shift` is nonleaf
            ctx = _update_lookaheads(
                item.lookaheads, rest,
                grammar, first_sets)
            eqs = grammar.groups[shift]
            more_items.update(
                _Dot(
                    symbol=eq.symbol,
                    rest=eq.expansion,
                    lookaheads=ctx)
                for eq in eqs)
        todo = more_items - closure
        closure |= more_items
    closure = _group_items(closure)
    return closure


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
    """Return lookahead symbols."""
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


def _update_lookaheads_simple(
        lookaheads:
            set[str],
        rest:
            tuple[str],
        grammar:
            _Grammar,
        first_sets:
            dict
        ) -> set[str]:
    # NOTE: another implementation
    for ahead in lookaheads:
        seq = (*rest, ahead)
        firsts = _ff.firsts_of_seq(
            seq, first_sets)
        firsts -= grammar.nonleafs
        ctx |= firsts
    return frozenset(ctx)


def _partition_kernel_by_shift(
        kernel:
            _Kernel
        ) -> _abc.Iterable[
            tuple[str, _Kernel]]:
    """Group items by to-shift symbol."""
    parts = _cl.defaultdict(set)
    for item in kernel:
        if not item.rest:
            continue
        shift = item.rest[0]
        parts[shift].add(item)
    # assert already grouped
    # for part in parts.values():
    #     grouped = _group_items(part)
    #     if grouped == part:
    #         continue
    #     raise AssertionError(
    #         f'{grouped}\n{part}')
    #
    # group
    # parts = {
    #     k: _group_items(part)
    #     for k, part in
    #         parts.items()}
    return parts


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


def _merge_kernels_2(
        kernel_1,
        kernel_2):
    eq_to_ctx = _cl.defaultdict(set)
    _accumulate_kernel(
        kernel_1, eq_to_ctx)
    _accumulate_kernel(
        kernel_2, eq_to_ctx)
    return frozenset(
        _Dot(
            symbol=symbol,
            done=done,
            rest=rest,
            lookaheads=frozenset(ctx))
        for (symbol, done, rest), ctx in
            eq_to_ctx.items())


def _accumulate_kernel(
        kernel:
            _Kernel,
        eq_to_ctx:
            dict[
                tuple,
                set[str]]
        ) -> None:
    """Add lookaheads keyed by equation."""
    for dot in kernel:
        eq_to_ctx[
            dot.symbol,
            dot.done,
            dot.rest].update(dot.lookaheads)


def _merge_kernels_simple(
        kernel_1:
            _Kernel,
        kernel_2:
            _Kernel
        ) -> _Kernel:
    """Return merged kernel, i.e.,

    kernel with coalesced lookaheads.
    """
    # if not _mergeable_kernels(
    #         kernel_1, kernel_2):
    #     raise ValueError(
    #         kernel_1, kernel_2)
    # reminds of mergesort
    kernel = set()
    eq_to_ctx_1 = _dot_to_ctx(kernel_1)
    eq_to_ctx_2 = _dot_to_ctx(kernel_2)
    for eq, ctx_1 in eq_to_ctx_1.items():
        ctx_2 = eq_to_ctx_2[eq]
        ctx = ctx_1 | ctx_2
        dot_ctx = _Dot(
            symbol=eq.symbol,
            done=eq.done,
            rest=eq.rest,
            lookaheads=ctx)
        kernel.add(dot_ctx)
    return frozenset(kernel)


def _merge_kernels(
        kernel_1,
        kernel_2
        ) -> _Kernel | None:
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
        # assert not mergeable_
        return None
    disj = (
        not _sets_intersect(
            merged.values()) or
        _sets_intersect(
            dot.lookaheads
            for dot in kernel_1) or
        _sets_intersect(
            dot.lookaheads
            for dot in kernel_2))
    if not disj:
        # assert not mergeable_
        return None
    # assert mergeable_
    merged = frozenset({
        _Dot(
            symbol=key[0],
            done=key[1],
            rest=key[2],
            lookaheads=frozenset(ctx))
        for key, ctx in
            merged.items()})
    # check result
    # merged_ = _merge_kernels_simple(
    #     kernel_1, kernel_2)
    # assert merged == merged_, (merged, merged_)
    return merged


def _sets_intersect(
        sets):
    accum = set()
    count = 0
    for value in sets:
        count += len(value)
        accum.update(value)
        if count != len(accum):
            return False
    return True


def _mergeable_kernels_2(
        kernel_1:
            _Kernel,
        kernel_2:
            _Kernel
        ) -> bool:
    """Return `True` if kernels can be merged."""
    # _assert_kernel_partitioned(kernel_1)
    # _assert_kernel_partitioned(kernel_2)
    # core_1 = _kernel_core(kernel_1)
    # core_2 = _kernel_core(kernel_2)
    # if core_1 != core_2:
    #     return False
    if len(kernel_1) != len(kernel_2):
        return False
    dot_to_ctx_1 = _dot_to_ctx(kernel_1)
    dot_to_ctx_2 = _dot_to_ctx(kernel_2)
    if len(dot_to_ctx_1) != len(dot_to_ctx_2):
        return False
    for dot in dot_to_ctx_1:
        if dot not in dot_to_ctx_2:
            return False
    for dot_1 in dot_to_ctx_1:
        for dot_2 in dot_to_ctx_2:
            if dot_1 == dot_2:
                continue
            ctx_1 = dot_to_ctx_1[dot_1]
            ctx_2 = dot_to_ctx_2[dot_2]
            # ctx_3 = dot_to_ctx_2[dot_1]
            # ctx_4 = dot_to_ctx_1[dot_2]
            disjoint = (
                not (ctx_1 & ctx_2))
            if disjoint:
                continue
            # already intersect ?
            ctx_1 = dot_to_ctx_1[dot_1]
            ctx_2 = dot_to_ctx_1[dot_2]
            intersect = ctx_1 & ctx_2
            if intersect:
                continue
            ctx_1 = dot_to_ctx_2[dot_1]
            ctx_2 = dot_to_ctx_2[dot_2]
            intersect = ctx_1 & ctx_2
            if intersect:
                continue
            return False
    return True


def _mergeable_kernels_simple(
        kernel_1:
            _Kernel,
        kernel_2:
            _Kernel
        ) -> bool:
    """Return `True` if kernels can be merged."""
    _assert_kernel_partitioned(kernel_1)
    _assert_kernel_partitioned(kernel_2)
    core_1 = _kernel_core(kernel_1)
    core_2 = _kernel_core(kernel_2)
    if core_1 != core_2:
        return False
    dot_to_ctx_1 = _dot_to_ctx(kernel_1)
    dot_to_ctx_2 = _dot_to_ctx(kernel_2)
    for dot_1 in dot_to_ctx_1:
        for dot_2 in dot_to_ctx_2:
            if dot_1 == dot_2:
                continue
            ctx_1 = dot_to_ctx_1[dot_1]
            ctx_2 = dot_to_ctx_2[dot_2]
            ctx_3 = dot_to_ctx_2[dot_1]
            ctx_4 = dot_to_ctx_1[dot_2]
            disjoint = (
                not (ctx_1 & ctx_2) and
                not (ctx_3 & ctx_4))
            if disjoint:
                continue
            # already intersect ?
            ctx_1 = dot_to_ctx_1[dot_1]
            ctx_2 = dot_to_ctx_1[dot_2]
            intersect = ctx_1 & ctx_2
            if intersect:
                continue
            ctx_1 = dot_to_ctx_2[dot_1]
            ctx_2 = dot_to_ctx_2[dot_2]
            intersect = ctx_1 & ctx_2
            if intersect:
                continue
            return False
    return True


def _reachable(
        init_node,
        edges):
    """Return reachable nodes."""
    reachable = set()
    todo = {init_node}
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
    """Project keys and values."""
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


def _assert_kernel_partitioned(
        kernel:
            _Kernel
        ) -> None:
    """Assert `kernel` is partitioned.

    A kernel is partitioned as one
    `_Dot` item per config-group.
    """
    core = _kernel_core(kernel)
    if len(core) != len(kernel):
        raise AssertionError(f'''
            {core = },
            {kernel = }
            ''')


def _is_kernel(
        items:
            _Kernel
        ) -> bool:
    """Return `True` if a kernel."""
    kernel = set(_lu.kernel_items(
        items))
    return (kernel == items)


def _kernel_core(
        kernel:
            _Kernel
        ) -> _Core:
    """Return items without lookaheads."""
    core = set()
    for dot_ctx in kernel:
        dot = _dot_core(dot_ctx)
        core.add(dot)
    return core


def _dot_core(
        dotted:
            _Dot
        ) -> _Dot:
    """Return dotted without lookaheads."""
    return _Dot(
        symbol=dotted.symbol,
        done=dotted.done,
        rest=dotted.rest)


def _dot_to_ctx(
        kernel:
            _Dot
        ) -> dict[
            _Dot, set[str]]:
    """Map equation to lookaheads.

    Maps dot-core to its context.
    """
    return {
        _dot_core(dot):
            dot.lookaheads
        for dot in kernel}


def _shift_dot_in_kernel(
        kernel:
            _Kernel
        ) -> _Kernel:
    """Return kernel with shifted dot.

    Asserts that shifting is possible.
    """
    return frozenset(map(
        _shift_dot,
        kernel))


def _shift_dot(
        item:
            _Dot
        ) -> _Dot:
    """Move dot towards end."""
    if not item.rest:
        raise ValueError(item)
    ahead, *rest = item.rest
    done = (*item.done, ahead)
    return _Dot(
        symbol=item.symbol,
        done=done,
        rest=tuple(rest),
        lookaheads=item.lookaheads)


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
