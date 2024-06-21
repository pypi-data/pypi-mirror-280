"""Tests for module `parstools._lr.lr_merging_opt`."""
import collections as _cl

import parstools._ff as _ff
import parstools._grammars as _grm
import parstools._lr.lr_merging_opt as _lr
import pytest


Dot = _lr._Dot
Prod = _grm.Production


def test_collect_merged_nodes():
    equations = [
        Prod('expr', ['expr', '+', 'A']),
        Prod('expr', ['A']),
        ]
    grammar = _grm.Grammar(
        root_symbol='expr',
        equations=equations)
    first_sets = _ff.compute_first_sets(
        grammar.equations)
    nodes, edges = _lr._collect_merged_nodes(
        grammar, first_sets)
    assert len(nodes) == 5, len(nodes)
    assert len(edges) == 5, len(edges)
    item_1 = Dot(
        symbol=_grm.ROOT,
        done=tuple(),
        rest=('expr',),
        lookaheads=frozenset({
            _grm.END}))
    item_2 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset({
            '+', _grm.END}))
    item_3 = Dot(
        symbol='expr',
        done=('expr', '+'),
        rest=('A',),
        lookaheads=frozenset({
            '+', _grm.END}))
    item_4 = Dot(
        symbol='expr',
        done=('expr', '+', 'A'),
        rest=tuple(),
        lookaheads=frozenset({
            '+', _grm.END}))
    item_5 = Dot(
        symbol=_grm.ROOT,
        done=('expr',),
        rest=tuple(),
        lookaheads=frozenset({
            _grm.END}))
    item_6 = Dot(
        symbol='expr',
        done=('A',),
        rest=tuple(),
        lookaheads=frozenset({
            '+', _grm.END}))
    kernel_1 = frozenset({item_1})
    kernel_2 = frozenset({item_2, item_5})
    kernel_3 = frozenset({item_3})
    kernel_4 = frozenset({item_4})
    kernel_5 = frozenset({item_6})
    # nodes
    assert kernel_1 in nodes, nodes
    assert kernel_2 in nodes, nodes
    assert kernel_3 in nodes, nodes
    assert kernel_4 in nodes, nodes
    assert kernel_5 in nodes, nodes
    # edges
    assert kernel_2 in edges[kernel_1], edges
    assert kernel_5 in edges[kernel_1], edges
    n = len(edges[kernel_1])
    assert n == 2, n
    assert kernel_3 in edges[kernel_2], edges
    n = len(edges[kernel_2])
    assert n == 1, n
    assert kernel_4 in edges[kernel_3], edges
    n = len(edges[kernel_3])
    assert n == 1, n


def test_assert_out_edges():
    # out-edges or reductions
    item_1 = Dot(
        symbol='expr',
        done=('expr', '+', 'A'),
        rest=tuple())
    kernel_1 = frozenset({item_1})
    item_2 = Dot(
        symbol='expr',
        done=('expr', '+'),
        rest=('A',))
    kernel_2 = frozenset({item_2})
    edges = {
        kernel_1: set(),
        kernel_2: {kernel_1}}
    _lr._assert_out_edges(edges)
    # error
    edges = {
        kernel_1: set(),
        kernel_2: set()}
    with pytest.raises(AssertionError):
        _lr._assert_out_edges(edges)


def test_kernel_only_reduces():
    item_1 = Dot(
        symbol='expr',
        done=('NUMBER',),
        rest=tuple(),
        lookaheads=frozenset())
    kernel_1 = {item_1}
    assert _lr._kernel_only_reduces(
        kernel_1)
    item_2 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'NUMBER'),
        lookaheads=frozenset())
    kernel_2 = {item_1, item_2}
    assert not _lr._kernel_only_reduces(
        kernel_2)


def test_successors_of_lr_1_node_shift_reduce():
    equations = [
        Prod('expr', ['expr', '+', 'A']),
        Prod('expr', ['A']),
        ]
    grammar = _grm.Grammar(
        root_symbol='expr',
        equations=equations)
    first_sets = _ff.compute_first_sets(
        equations)
    replaced = dict()
    nodes = set()
    edges = _cl.defaultdict(set)
    pred = _cl.defaultdict(set)
    symbol_to_successor = _cl.defaultdict(set)
    # shift
    item = Dot(
        symbol='expr',
        done=('expr', '+'),
        rest=('A',),
        lookaheads=frozenset({'A', '_END'}))
    kernel = frozenset({item})
    succ = _lr._successors_of_lr_1_node(
        kernel, nodes, edges, pred,
        symbol_to_successor,
        grammar, first_sets, replaced)
    assert len(succ) == 1, succ
    kernel_1, = succ
    item_1 = Dot(
        symbol='expr',
        done=('expr', '+', 'A'),
        lookaheads=frozenset({'A', '_END'}))
    assert kernel_1 == {item_1}, kernel_1
    # reduce
    succ = _lr._successors_of_lr_1_node(
        kernel_1, nodes, edges, pred,
        symbol_to_successor,
        grammar, first_sets, replaced)
    assert not succ, succ


def test_successors_of_lr_1_node_branch():
    equations = [
        Prod('expr', ['expr' '+', 'prod']),
        Prod('expr', ['prod']),
        Prod('prod', ['prod', '*', 'NUM']),
        Prod('prod', ['NUM']),
        ]
    grammar = _grm.Grammar(
        root_symbol='expr',
        equations=equations)
    first_sets = _ff.compute_first_sets(
        equations)
    replaced = dict()
    nodes = set()
    edges = _cl.defaultdict(set)
    pred = _cl.defaultdict(set)
    symbol_to_successor = _cl.defaultdict(set)
    # branching
    item = Dot(
        symbol='prod',
        done=tuple(),
        rest=('prod', '*', 'NUM'),
        lookaheads=frozenset({'+', '_END'}))
    kernel = frozenset({item})
    succ = _lr._successors_of_lr_1_node(
        kernel, nodes, edges, pred,
        symbol_to_successor,
        grammar, first_sets, replaced)
    assert len(succ) == 2, succ
    item_1 = Dot(
        symbol='prod',
        done=('prod',),
        rest=('*', 'NUM'),
        lookaheads=frozenset({
            '*', '+', '_END'}))
    item_2 = Dot(
        symbol='prod',
        done=('NUM',),
        rest=tuple(),
        lookaheads=frozenset({'*'}))
    kernel_1 = frozenset({item_1})
    kernel_2 = frozenset({item_2})
    assert kernel_1 in succ, succ
    assert kernel_2 in succ, succ


def test_kernel_closure():
    equations = [
        Prod('expr', ['expr', '+', 'A']),
        Prod('expr', ['A']),
        ]
    grammar = _grm.Grammar(
        root_symbol='expr',
        equations=equations)
    first_sets = _ff.compute_first_sets(
        equations)
    # leaf symbol next to shift
    item = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset({'+'}))
    kernel = {item}
    parts = _lr._kernel_closure(
        kernel, grammar, first_sets)
    assert len(parts) == 1, parts
    assert '+' in parts, parts
    kernel_1 = parts['+']
    item_1 = Dot(
        symbol='expr',
        done=('expr', '+'),
        rest=('A',),
        lookaheads=frozenset({'+'}))
    assert kernel_1 == {item_1}, kernel_1
    # nonleaf symbol next to shift
    item = Dot(
        symbol='expr',
        done=tuple(),
        rest=('expr', '+', 'A'),
        lookaheads=frozenset({'_END'}))
    kernel = {item}
    parts = _lr._kernel_closure(
        kernel, grammar, first_sets)
    item_1 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset({'+', '_END'}))
    item_2 = Dot(
        symbol='expr',
        done=('A',),
        rest=tuple(),
        lookaheads=frozenset({'+'}))
    kernel_1 = {item_1}
    kernel_2 = {item_2}
    parts_ = {
        'expr': kernel_1,
        'A': kernel_2}
    assert parts == parts_, parts


def test_update_lookaheads():
    # no nullables
    equations = [
        Prod('expr', ['expr', '+', 'A']),
        Prod('expr', ['A']),
        ]
    grammar = _grm.Grammar(
        root_symbol='expr',
        equations=equations)
    first_sets = _ff.compute_first_sets(
        equations)
    lookaheads = {'+'}
    rest = ['expr', '+', 'A']
    ctx = _lr._update_lookaheads(
        lookaheads, rest,
        grammar, first_sets)
    ctx_ = {'A'}
    assert ctx == ctx_, ctx
    # grammar with nullables
    equations = [
        Prod('expr', ['expr', '+', 'A']),
        Prod('expr', ['']),
        ]
    grammar = _grm.Grammar(
        root_symbol='expr',
        equations=equations)
    first_sets = _ff.compute_first_sets(
        equations)
    lookaheads = set()
    rest = ['expr', '+', 'A']
    ctx = _lr._update_lookaheads(
        lookaheads, rest,
        grammar, first_sets)
    ctx_ = {'', '+'}
    assert ctx == ctx_, ctx


def test_group_items():
    # merging 2 items
    item_1 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset({'+'}))
    item_2 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset({'_END'}))
    items = {item_1, item_2}
    kernel = _lr._group_items(items)
    item = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset(
            {'+', '_END'}))
    kernel_ = {item}
    assert kernel == kernel_, kernel
    # not merging
    item_1 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset({'+', '_END'}))
    item_2 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('-', 'A'),
        lookaheads=frozenset({'-', '_END'}))
    items = {item_1, item_2}
    kernel = _lr._group_items(items)
    assert kernel == items, kernel


def test_merge_kernels():
    # mergeable kernels
    item_1 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset({'+'}))
    item_2 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset({'_END'}))
    kernel_1 = {item_1}
    kernel_2 = {item_2}
    merged = _lr._merge_kernels(
        kernel_1, kernel_2)
    item_3 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset(
            {'+', '_END'}))
    merged_ = {item_3}
    assert merged == merged_, merged
    # same kernel
    merged = _lr._merge_kernels(
        kernel_1, kernel_1)
    assert merged == kernel_1, merged
    # not mergeable kernels
    # due to lookaheads
    item_4 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('-', 'A'),
        lookaheads=frozenset({'+'}))
    kernel_3 = {item_4}
    result = _lr._merge_kernels(
        kernel_1, kernel_3)
    assert result is None, result
    # not mergeable kernels
    # due to number of items
    item_5 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('*', 'B'),
        lookaheads=frozenset({'*'}))
    kernel_4 = {item_2, item_5}
    result = _lr._merge_kernels(
        kernel_1, kernel_4)
    assert result is None, result


def test_merge_kernels_with_overlaps():
    # mergeable due to overlap
    # before merging
    item_1 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset({'_END'}))
    item_2 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('-', 'A'),
        lookaheads=frozenset({'_END'}))
    item_3 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset({'+'}))
    item_4 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('-', 'A'),
        lookaheads=frozenset({'-'}))
    kernel_1 = {item_1, item_2}
    kernel_2 = {item_3, item_4}
    merged = _lr._merge_kernels(
        kernel_1, kernel_2)
    item_5 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookaheads=frozenset(
            {'+', '_END'}))
    item_6 = Dot(
        symbol='expr',
        done=('expr',),
        rest=('-', 'A'),
        lookaheads=frozenset(
            {'-', '_END'}))
    merged_ = {item_5, item_6}
    assert merged == merged_, merged


def test_sets_disjoint():
    sets = [
        {1, 2}, {2, 3}]
    assert not _lr._sets_disjoint(sets)
    sets = [
        {1, 2}, {3, 4}]
    assert _lr._sets_disjoint(sets)


def test_reachable():
    init_node = 1
    edges = {
        1: {2},
        2: {4, 5},
        3: {6},
        4: set(),
        5: set()}
    reachable = _lr._reachable(
        {init_node}, edges)
    reachable_ = {1, 2, 4, 5}
    assert reachable == reachable_, reachable


def test_replace_edges():
    edges = {1: {2, 3}, 2: {3}}
    replaced = {1: 5, 2: 3, 3: 4}
    new_edges_ = {5: {4}, 4: {4}}
    new_edges = _lr._replace_edges(
        edges, replaced)
    assert new_edges == new_edges_, new_edges


def test_is_kernel():
    # root item (empty)
    item = Dot(
        symbol=_grm.ROOT,
        done=tuple(),
        rest=tuple())
    items = {item}
    assert _lr._is_kernel(items)
    # item with `done` symbols
    item = Dot(
        symbol='expr',
        done=('expr', '+'),
        rest=('NUMBER',))
    items = {item}
    assert _lr._is_kernel(items)
    # not kernel
    item_2 = Dot(
        symbol='expr',
        done=tuple(),
        rest=('expr', '+', 'NUMBER'))
    items = {item, item_2}
    assert not _lr._is_kernel(items)


def test_dot_core():
    item = Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'NUMBER'),
        lookaheads={'_END', '+'})
    dot = _lr._dot_core(item)
    assert dot.lookaheads is None, dot


def test_make_init_state():
    root_symbol = 'expr'
    node = _lr._make_init_state(root_symbol)
    assert isinstance(node, frozenset), node
    assert len(node) == 1, node
    item, = node
    item_ = Dot(
        symbol=_grm.ROOT,
        done=tuple(),
        rest=(root_symbol,),
        lookaheads={_grm.END})
    assert item == item_, item


if __name__ == '__main__':
    test_collect_merged_nodes()
