"""Simple LR parser generation.

- SLR(1): simple LR with lookahead 1
"""
import typing as _ty

import parstools._ff as _ff
import parstools._grammars as _grm
import parstools._lr.lr as _lr
import parstools._lr.parser as _p
import parstools._lr.utils as _lu
import parstools._utils as _u


Grammar = _grm.Grammar
Parser = _p.Parser
_Action = _lu.Action


def make_slr_tables(
        grammar:
            Grammar,
        lookahead:
            int=1
        ) -> Parser:
    r"""Return SLR(lookahead) state machine.

    ```tla
    ASSUME
        lookahead \in Nat
    ```
    """
    _assert_lookahead(lookahead)
    grammar = _lr.add_root_equation(grammar)
    initial = _lr.make_init_state(
        grammar.root_symbol, 0)
    actions = _make_slr_1_action_table(grammar)
    return Parser(initial, actions)


def _make_slr_1_action_table(
        grammar:
            Grammar
        ) -> dict[
            tuple[
                state := _ty.Any,
                symbol := str],
            _Action]:
    """Return SLR(1) state machine."""
    first_sets = _ff.compute_first_sets(
        grammar.equations)
    follow_sets = _ff.compute_follow_sets(
        grammar.equations, first_sets)
    actions = _u.MonotonicDict()
    states = _lr._collect_lr_0_states(
        grammar.groups)
    for state in states:
        _make_slr_1_actions_at_state(
            state, actions,
            grammar, follow_sets)
    return dict(actions)


def _make_slr_1_actions_at_state(
        state:
            set,
        actions:
            dict,
        grammar:
            Grammar,
        follow_sets:
            dict
        ) -> None:
    """Add to `actions` those at `state`."""
    # shifts
    successors = _successors_of_lr_0_state(
        state, grammar.groups)
    for next_state in successors:
        item = _u.pick(next_state)
            # suffices because each LR(0) item
            # is represented by its kernel
        symbol = item.done[-1]
        actions[state, symbol] = _Action(
            state=next_state)
    # reductions
    for item in _lu.final_items(state):
        equation = _lu.production_of_dot(item)
        action = _p._Action(equation=equation)
        # {leafs \in FOLLOW(item):
        #     item \in
        #         final_items(state),
        #     state \in states}
        follow_symbols = (
            follow_sets[item.symbol].difference(
                grammar.nonleafs))
                # This keeps `_END`
        for leaf in follow_symbols:
            actions[state, leaf] = action
