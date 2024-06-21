"""LR(1) parser generation.

- LR(0): LR without lookahead
- LR(1): LR with lookahead 1


References
==========

* Donald E. Knuth
  "On the translation of languages from left to right"
  Information and Control
  Volume 8, Issue 6, pages 607--639, 1965
  <https://doi.org/10.1016/S0019-9958(65)90426-2>
"""
import collections as _cl
import collections.abc as _abc
import enum
import functools as _ft
import itertools as _itr
import logging as _log
import math
import pprint as _pp
import textwrap as _tw
import typing as _ty

import parstools._ff as _ff
import parstools._grammars as _grm
import parstools._lr.parser as _p
import parstools._lr.utils as _lu
import parstools._utils as _u


_ROOT: _ty.Final = _grm.ROOT
_END: _ty.Final = _grm.END


_Production = _grm.Production
Grammar = _grm.Grammar
_Dot = _lu.Dot
_State: _ty.TypeAlias = set[_Dot]
_Parser = _p.Parser


logger = _log.getLogger(__name__)


def make_parser(
        grammar:
            Grammar,
        lookahead:
            int=1
        ) -> _p.Parser:
    r"""Return LR(lookahead) state machine.

    ```tla
    ASSUMPTION
        lookahead \in Nat
    ```
    """
    match lookahead:
        case 0:
            return _make_lr_0_tables(grammar)
        case 1:
            return _make_lr_1_tables(grammar)
        case _:
            raise NotImplementedError(lookahead)


def _make_lr_1_tables(
        grammar:
            Grammar
        ) -> _Parser:
    grammar = _lu.add_root_equation(grammar)
    first_sets = _ff.compute_first_sets(
        grammar.equations)
    initial = _make_initial_lr_1_node(
        grammar, first_sets)
    actions = _make_lr_1_action_table(grammar)
    return _p.Parser(initial, actions)


def _make_initial_lr_1_node(
        grammar,
        first_sets):
    initial = _lu.make_init_state(
        grammar.root_symbol, 1)
    initial = _closure_lr_1(
        initial, grammar, first_sets)
    return frozenset(initial)


def _make_lr_1_action_table(
        grammar:
            Grammar
        ) -> dict:
    """Return LR(1) state machine."""
    first_sets = _ff.compute_first_sets(
        grammar.equations)
    states = _collect_lr_1_states(
        grammar, first_sets)
    # print('\n' + 40 * '-')
    # print('LR(1) states:')
    # string = _lu.pformat_states(states)
    # print(string)
    # print(40 * '-' + '\n')
    actions = _u.MonotonicDict()
    for state in states:
        _make_lr_1_actions_at_state(
            state, actions,
            grammar, first_sets)
    return dict(actions)


def _make_lr_1_actions_at_state(
        state:
            set,
        actions:
            dict,
        grammar:
            Grammar,
        first_sets:
            dict
        ) -> None:
    """Add to `actions` those at `state`."""
    # shifts
    successors = _successors_of_lr_1_state(
        state, grammar, first_sets)
    for next_state in successors:
        item = _lu.pick_kernel_item(next_state)
        symbol = item.done[-1]
            # leaf (lexer token or `_END`), or
            # nonleaf (results from reduction)
        actions[state, symbol] = _lu.Action(
            state=next_state)
    # reductions
    for item in _lu.final_items(state):
        equation = _lu.production_of_dot(item)
        symbol = item.lookahead
        actions[state, symbol] = _lu.Action(
            equation=equation)


def _collect_lr_1_states(
        grammar:
            Grammar,
        first_sets:
            dict[
                str,
                set[
                    str]]
        ) -> set:
    """Return LR(1) canonical collection.

    In this implementation
    each lookahead is a symbol.
    """
    state = _lu.make_init_state(
        grammar.root_symbol, 1)
    state = _closure_lr_1(
        state, grammar, first_sets)
    state = frozenset(state)
    states = {state}
    todo = {state}
    while todo:
        state = todo.pop()
        successors = _successors_of_lr_1_state(
            state, grammar, first_sets)
        todo |= successors - states
        states.add(state)
        # print(
        #     'Number of LR(1) '
        #     f'nodes: {len(states)}')
    return states


def _successors_of_lr_1_state(
        state:
            set,
        grammar:
            Grammar,
        first_sets:
            dict[
                str,
                set[
                    str]]
        ) -> set[
            frozenset]:
    """Yield next LR(1) kernels."""
    closure = _closure_lr_1(
        state, grammar, first_sets)
    successors = set()
    for part in _partition_lr_state(closure):
        part = set(map(_lu.shift_dot, part))
        if None in part:
            raise AssertionError(part)
        # NOTE: `_closure_lr_1()` updates
        # the lookaheads of only initial
        # items just added to the closure
        part = _closure_lr_1(
            part, grammar, first_sets)
        next_state = frozenset(part)
        successors.add(next_state)
    return successors


def _closure_lr_1(
        items:
            set,
        grammar:
            Grammar,
        first_sets:
            dict[
                str,
                set[
                    str]]
        ) -> set:
    """Return closure of LR(1) item.

    - `items`:
      nonfinal LR(1) items
      (i.e., with nonempty
      `item.rest`)
    """
    items = set(items)
    n = 0
    while n != (n := len(items)):
        for item in set(items):
            if not item.rest:
                continue
            symbol, *rest = item.rest
            # leaf ?
            if symbol in grammar.leafs:
                continue
            # `symbol` is nonleaf
            lookahead = item.lookahead
            rest.append(lookahead)
            firsts = _ff.firsts_of_seq(
                rest, first_sets)
            firsts.difference_update(
                grammar.nonleafs)
            eqs = grammar.groups[symbol]
            items |= {
                _Dot(
                    symbol=symbol,
                    rest=eq.expansion,
                    lookahead=leaf)
                for eq in eqs
                for leaf in firsts}
    return items


def _make_lr_0_tables(
        grammar:
            Grammar
        ) -> _Parser:
    grammar = _lu.add_root_equation(grammar)
    initial = _lu.make_init_state(
        grammar.root_symbol, 0)
    initial = frozenset({initial})
    actions = _make_lr_0_action_table(grammar)
    return _Parser(initial, actions)


def _make_lr_0_action_table(
        grammar:
            Grammar
        ) -> dict:
    """Return LR(0) state machine."""
    actions = _u.MonotonicDict()
    states = _collect_lr_0_states(grammar.groups)
    for state in states:
        _make_lr_0_actions_at_state(
            state, actions, grammar)
    return dict(actions)


def _make_lr_0_actions_at_state(
            state:
                set,
            actions:
                dict,
            grammar:
                Grammar
            ) -> None:
    """Add to `actions` those at `state`."""
    successors = _successors_of_lr_0_state(
        state, grammar.groups)
    for next_state in successors:
        item = _lu.pick_kernel_item(next_state)
        symbol = item.done[-1]
        actions[state, symbol] = _lu.Action(
            state=next_state)
    for item in _lu.final_items(state):
        equation = _lu.production_of_dot(item)
        action = _lu.Action(
            equation=equation)
        for symbol in grammar.leafs:
            actions[state, symbol] = action


def _make_lr_0_state_transitions(
        states:
            set,
        equation_groups:
            dict
        ) -> _u.DiGraph:
    """Return `DiGraph` of labeled edges."""
    graph = _u.DiGraph()
    for state in states:
        successors = _successors_of_lr_0_state(
            state, equation_groups)
        for other in successors:
            core = _lu.kernel_items(other)
            item = _u.pick(core)
            label = item.done[-1]
            graph.add_edge(
                state, other, label)
    return graph


def _collect_lr_0_states(
        equation_groups:
            dict
        ) -> set[_State]:
    """Return LR(0) canonical collection."""
    op = _ft.partial(
        _successors_of_lr_0_states,
        equation_groups=equation_groups)
    return _u.least_fixpoint(op)


def _successors_of_lr_0_states(
        states:
            set,
        equation_groups:
            dict[
                str,
                list[
                    _Production]]
        ) -> _abc.Iterator[
            frozenset]:
    """Yield successor states of `states`."""
    roots = equation_groups[_ROOT]
    if len(roots) != 1:
        raise ValueError(equation_groups)
    root, = roots
    dotted = _Dot(
        _ROOT,
        rest=root.expansion)
    start = {dotted}
    yield frozenset(start)
    for state in set(states):
        yield from _successors_of_lr_0_state(
            state, equation_groups)


def _successors_of_lr_0_state(
        state:
            set,
        equation_groups:
            dict[
                str,
                list[
                    _Production]]
        ) -> _abc.Iterator[
            frozenset]:
    """Yield next LR(0) kernels."""
    closure = _closure_lr_0(
        state, equation_groups)
    for part in _partition_lr_state(closure):
        part = set(map(_lu.shift_dot, part))
        if None in part:
            part.remove(None)
        yield frozenset(part)


def _partition_lr_state(
        state:
            set
        ) -> _abc.Iterator[
            set[
                _Dot]]:
    """Group items by next symbol."""
    parts = _cl.defaultdict(set)
    for item in state:
        # final item ?
        if not item.rest:
            continue
        ahead = item.rest[0]
        parts[ahead].add(item)
    yield from parts.values()


def _closure_lr_0(
        core:
            _State,
        equation_groups:
            dict[
                str,
                list[
                    _Production]]
        ) -> _State:
    """Return closure of core items."""
    refine = _ft.partial(
        _refine_lr_0_state,
        source=core,
        equation_groups=equation_groups)
    return _u.least_fixpoint(refine)


def _refine_lr_0_state(
        state:
            _State,
        source:
            _State,
        equation_groups:
            dict[
                str,
                set[
                    _Production]]
        ) -> _abc.Iterator[
            _Dot]:
    """Yield items of refinement of `state`.

    - `source`:
      set of items from where the fixpoint
      iteration starts
    """
    yield from source
    for item in set(state):
        yield from _refine_lr_0_item(
            item, equation_groups)


def _refine_lr_0_item(
        item:
            _Dot,
        equation_groups:
            dict[
                str,
                set]
        ) -> _abc.Iterator[
            _Dot]:
    """Yield grammar items that refine `item`.

    Also yield `item` itself.
    """
    yield item
    if not item.rest:
        return
    symbol = item.rest[0]
    eqs = equation_groups.get(symbol, set())
    for eq in eqs:
        yield _Dot(
            symbol,
            rest=eq.expansion)
