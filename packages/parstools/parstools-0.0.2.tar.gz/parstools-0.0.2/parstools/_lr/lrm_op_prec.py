"""LR(1) with state merging and operator precedence."""
import time
import typing as _ty

import parstools._ff as _ff
import parstools._grammars as _grm
import parstools._lr.lr_merging_opt as _lrm
import parstools._lr.parser as _p
import parstools._lr.utils as _lu


_Grammar = _grm.Grammar
_Kernel: _ty.TypeAlias = set[_lrm._Dot]
_Kernels: _ty.TypeAlias = set[_Kernel]


def make_parser(
        grammar:
            _Grammar,
        operator_precedence:
            list[
                tuple[str]] |
            None=None,
        cache_filename:
            str |
            None=None
        ) -> _p.Parser:
    """Return LR-merged parser.

    If `operator_precedence is not None`,
    use to resolve shift/reduce ambiguities.

    `operator_precedence` contains tuples of
    associativity and operator names, where:
    - associativity is `'left'`, `'nonassoc'`,
      or `'right'`.
    - operator names are strings

    Example:

    ```py
    operator_precedence = [
        ('left', 'PLUS', 'MINUS'),
        ('left', 'ASTERISK', 'DIV')]
    ```

    If `cache_filename is not None`,
    use to store parser, attempting to
    load the parser first from file (JSON).
    """
    parser = _p.check_parser_cache(
        grammar, cache_filename)
    if parser is not None:
        return parser
    if operator_precedence is None:
        operator_precedence = list()
    parser = make_lr_1_tables(
        grammar, operator_precedence)
    _p.dump_parser_cache(
        grammar, parser, cache_filename)
    return parser


def make_lr_1_tables(
        grammar:
            _Grammar,
        operator_precedence:
            list[
                tuple[str]]
        ) -> _p.Parser:
    t1 = time.perf_counter()
    grammar = _lu.add_root_equation(grammar)
    first_sets = _ff.compute_first_sets(
        grammar.equations)
    nodes, edges = _lrm._collect_merged_nodes(
        grammar, first_sets)
    all_kernels = all(map(
        _lrm._is_kernel, nodes))
    if not all_kernels:
        raise AssertionError(all_kernels)
    # text = _lu.pformat_states(nodes)
    # print(text)
    actions = _make_lr_1_action_table(
        edges, grammar, first_sets,
        operator_precedence)
    initial = _lrm._make_init_state(
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
            dict,
        operator_precedence:
            list[
                tuple[str]]
        ) -> dict[
            tuple[_Kernel, str],
            _lu.Action]:
    """Return parser-actions table."""
    op_to_prec = dict()
    enum = enumerate(operator_precedence)
    for i, items in enum:
        assoc, *operators = items
        if not operators:
            raise ValueError(items)
        for operator in operators:
            op_to_prec[operator] = (i, assoc)
    print(op_to_prec)
    # compute actions
    actions = dict()
    for node, succ in edges.items():
        _make_lr_1_actions_at_node(
            node, succ, actions,
            grammar, first_sets,
            op_to_prec)
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
    return actions


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
            dict,
        op_to_prec:
            dict[
                str,
                tuple[int, str]]
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
            node, symbol, action, actions,
            op_to_prec)
    # reductions
    for item in _lu.final_items(node):
        equation = _lu.production_of_dot(item)
        for symbol in item.lookaheads:
            action = _lu.Action(
                equation=equation)
            _add_lr_action(
                node, symbol, action, actions,
                op_to_prec)
    # print(actions)


def _add_lr_action(
        node:
            _Kernel,
        symbol:
            str,
        action:
            _lu.Action,
        actions:
            dict,
        op_to_prec:
            dict[
                str,
                tuple[int, str]]
        ) -> None:
    """Add action, with error message otherwise."""
    key = (node, symbol)
    other = actions.get(key)
    if other is None:
        actions[key] = action
        return
    # a shift already exists
    symbol_prec = op_to_prec.get(symbol)
    expansion = action.equation.expansion
    prec = map(op_to_prec.get, expansion)
    prec = list(filter(None, prec))
    if symbol_prec is None or not prec:
        _raise_overlap_error(
            symbol, action, other)
    exp_prec = max(
        prec,
        key=lambda x: x[0])
    # shift instead of reduce ?
    shift = (
        symbol_prec[0] > exp_prec[0] or
        (symbol_prec[0] == exp_prec[0] and
        exp_prec[1] == 'right'))
        # cases: left, nonassoc, right
    if shift:
        return
    # reduce instead of shift
    actions[key] = action


def _raise_overlap_error(
        symbol,
        action,
        other):
    """Raise exception for overlap error."""
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
