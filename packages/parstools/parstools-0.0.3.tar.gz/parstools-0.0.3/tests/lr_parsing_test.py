"""Tests of `parstools._lr.lr_merging_opt`."""
import collections as _cl
import os

import parstools._grammars as _grm
import parstools._lr.lr as _lr
import parstools._lr.lr_merging_opt as _lrm
import parstools._lr.parser as _p
import parstools._lr.utils as _lru
import pytest


def test_lr_error_reporting():
    """Generate error messages."""
    grammar_1 = error_grammar_reduce_reduce()
    with pytest.raises(ValueError):
        _lrm.make_parser(grammar_1)
    grammar_2 = error_grammar_reduce_reduce()
    with pytest.raises(ValueError):
        _lrm.make_parser(grammar_2)


def error_grammar_shift_reduce(
        ) -> _grm.Grammar:
    root_symbol = 'expr'
    equations = [
        _grm.Production(
            'expr',
            ['expr', '+', 'expr']),
        _grm.Production(
            'expr',
            ['expr', '*', 'expr']),
        ]
    return _grm.Grammar(
        root_symbol=root_symbol,
        equations=equations)


def error_grammar_reduce_reduce(
        ) -> _grm.Grammar:
    root_symbol = 'expr'
    equations = [
        _grm.Production(
            'expr',
            ['sum_1']),
        _grm.Production(
            'expr',
            ['sum_2']),
        _grm.Production(
            'sum_1',
            ['num', '+', 'expr']),
        _grm.Production(
            'sum_2',
            ['num', '+', 'expr']),
        ]
    return _grm.Grammar(
        root_symbol=root_symbol,
        equations=equations)


def test_compare_parsers():
    """Prove LR-merged simulates LR(1) parser."""
    grammar_2 = grammar_g2_1977_ai()
    print(f'{__file__ = }')
    dir, _ = os.path.split(__file__)
    cache_filename = 'grammar_2_parser.json'
    cache_filepath = os.path.join(
        dir, cache_filename)
    print(f'{cache_filepath = }')
    parser = _lrm.make_parser(
        grammar_2,
        cache_filename=cache_filepath)
    tokens = [
        _p.Result(symbol='(', value='('),
        _p.Result(symbol='0', value='0'),
        _p.Result(symbol=')', value=')'),
        ]
    result = parser.parse(tokens)
    assert result is not None
    # _p.print_parser(parser, grammar_2)
    # compare to LR(1) parser
    lr_parser = _lr.make_parser(grammar_2, 1)
    lr_machine_simulation(
        lr_parser, parser)


def lr_machine_simulation(
        parser,
        other_parser
        ) -> None:
    """Assert merged LR parser simulates LR parser."""
    actions = _action_as_nested_dict(
        parser._actions)
    actions_m = _action_as_nested_dict(
        other_parser._actions)
    init = parser._initial
    init_m = other_parser._initial
    visited = set()
    visited_m = set()
    node_map = _cl.defaultdict(set)
    todo = {(init, init_m)}
    while todo:
        node, node_m = todo.pop()
        visited.add(node)
        visited_m.add(node_m)
        more = set()
        kv = actions[node].items()
        for symbol, action in kv:
            if symbol not in actions_m[node_m]:
                raise AssertionError(symbol, node)
            action_m = actions_m[node_m][symbol]
            if action.state is not None:
                next_node = action.state
                assert (action_m.state
                    is not None), action_m
                next_node_m = action_m.state
                node_map[next_node].add(
                    next_node_m)
                pair = (
                    next_node,
                    next_node_m)
                more.add(pair)
            elif action.equation is not None:
                assert (action_m.equation
                    is not None), action_m
                assert (
                    action.equation ==
                    action_m.equation)
            else:
                raise AssertionError(
                    action, action_m)
        todo.update(
            (u, p)
            for (u, p) in more
            if u not in visited)
    node_map = dict(node_map)
    # _pp.pp(node_map)
    print(f'{visited_m = }')
    node_map_m = _cl.defaultdict(set)
    for node, nodes_m in node_map.items():
        if len(nodes_m) != 1:
            raise AssertionError(
                nodes_m)
        node_m, = nodes_m
        node_map_m[node_m].add(node)
    # assert each equivalence class comprises
    # of mergeable nodes
    for node_m, nodes in node_map_m.items():
        print(
            f'{node_m = } maps to '
            f'{len(nodes)} nodes')
        _assert_all_pairs_mergeable(nodes)


def _assert_all_pairs_mergeable(
        nodes
        ) -> None:
    """Assert distinct nodes are mergeable."""
    for u in nodes:
        for v in nodes:
            if u == v:
                continue
            p = _to_dot_lookaheads(u)
            q = _to_dot_lookaheads(v)
            merged = _lrm._merge_kernels(p, q)
            if merged is None:
                raise AssertionError(p, q)


def _to_dot_lookaheads(
        dot_items):
    """Return kernel.

    Each dotted item has lookaheads.
    """
    kernel = _lru.kernel_items(dot_items)
    eq_to_ctx = _cl.defaultdict(set)
    for item in kernel:
        key = (
            item.symbol,
            item.done,
            item.rest)
        eq_to_ctx[key].add(item.lookahead)
    items = set()
    for eq, ctx in eq_to_ctx.items():
        symbol, done, rest = eq
        dot = _lrm._Dot(
            symbol=symbol,
            done=done,
            rest=rest,
            lookaheads=frozenset(ctx))
        items.add(dot)
    return frozenset(items)


def _action_as_nested_dict(
        actions:
            dict
        ) -> dict:
    """Return actions keyed by node."""
    actions_nested = _cl.defaultdict(dict)
    kv = actions.items()
    for (node, symbol), action in kv:
        actions_nested[node][symbol] = action
    return dict(actions_nested)


def grammar_g2_1977_ai(
        ) -> _grm.Grammar:
    """Grammar G_2 of Figure 3, on page 37 of

    David Pager
    "Eliminating Unit Productions from LR Parsers"
    Acta Informatica
    pages 31--59, 1977
    """
    root_symbol = 'PARAMETER'
    _Production = _grm.Production
    equations = [
        _Production('PARAMETER', ['EXPR']),
        _Production('PARAMETER', ['BOOLEXPR']),
        _Production('PARAMETER', ['FUNCTIONID']),
        _Production('PARAMETER', ['ARRAYID']),
        _Production('EXPR', ['EXPR', '+', 'TERM']),
        _Production('EXPR', ['EXPR', '-', 'TERM']),
        _Production('EXPR', ['+', 'TERM']),
        _Production('EXPR', ['TERM']),
        _Production('TERM', ['TERM', '*', 'PRIMARY']),
        _Production('TERM', ['TERM', '/', 'PRIMARY']),
        _Production('TERM', ['PRIMARY']),
        _Production('PRIMARY', ['(', 'EXPR', ')']),
        _Production('PRIMARY', ['ARITHID']),
        _Production('PRIMARY', ['ARITHCONST']),
        _Production(
            'PRIMARY',
            ['FUNCTIONID', '(', 'PARAMETERLIST', ')']),
        _Production(
            'PRIMARY',
            ['ARRAYID', '(', 'SUBSCRIPTLIST', ')']),
        _Production(
            'BOOLEXPR',
            ['EXPR', 'RELOP', 'EXPR']),
        _Production(
            'BOOLEXPR',
            ['BOOLFACTOR', '=', 'BOOLFACTOR']),
        _Production(
            'BOOLEXPR',
            ['BOOLFACTOR', '~=', 'BOOLFACTOR']),
        _Production(
            'BOOLEXPR',
            ['BOOLFACTOR']),
        _Production(
            'BOOLFACTOR',
            ['BOOLFACTOR', '+', 'BOOLTERM']),
        _Production(
            'BOOLFACTOR',
            ['BOOLFACTOR', r'\oplus', 'BOOLTERM']),
        _Production(
            'BOOLFACTOR',
            ['BOOLTERM']),
        _Production(
            'BOOLTERM',
            ['BOOLTERM', '.', 'BOOLSECONDARY']),
        _Production(
            'BOOLTERM',
            ['BOOLSECONDARY']),
        _Production(
            'BOOLSECONDARY',
            ['~', 'BOOLPRIMARY']),
        _Production(
            'BOOLSECONDARY',
            ['BOOLPRIMARY']),
        _Production(
            'BOOLPRIMARY',
            ['(', 'BOOLEXPR', ')']),
        _Production(
            'BOOLPRIMARY',
            ['BOOLID']),
        _Production(
            'BOOLPRIMARY',
            ['0']),
        _Production(
            'BOOLPRIMARY',
            ['1']),
        _Production(
            'RELOP',
            ['=']),
        _Production(
            'RELOP',
            ['~=']),
        _Production(
            'RELOP',
            ['>']),
        _Production(
            'RELOP',
            ['>=']),
        _Production(
            'RELOP',
            ['<']),
        _Production(
            'RELOP',
            ['<=']),
        _Production(
            'ARITHID',
            ['LETTER', 'DIGIT']),
        _Production(
            'ARITHID',
            ['LETTER']),
        _Production(
            'ARRAYID',
            ['LETTER', 'LETTER', 'DIGIT']),
        _Production(
            'FUNCTIONID',
            ['FN', 'LETTER']),
        # _Production(
        #     'LETTER',
        #     ['A']),
        # _Production(
        #     'LETTER',
        #     ['B']),
        # ...
        # same for DIGIT
        _Production(
            'PARAMETERLIST',
            ['PARAMETERLIST PARAMETER']),
        _Production(
            'PARAMETERLIST',
            ['PARAMETER']),
        ]
    return _grm.Grammar(
        root_symbol,
        equations)


if __name__ == '__main__':
    test_lr_error_reporting()
