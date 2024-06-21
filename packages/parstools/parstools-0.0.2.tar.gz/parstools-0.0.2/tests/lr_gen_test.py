"""Test LR parser generation."""
import parstools._grammars as _grm
import parstools._lr.lr as _lr
import parstools._lr.utils as _lu


ROOT = _grm.ROOT
END = _grm.END


def test_make_lr_1_action_table():
    grammar, _ = _make_grammar_expr_plus()
    states = _collect_lr_1_states()
    (state_1, state_2, state_3,
        state_4, state_5) = map(frozenset, states)
    actions = _lr._make_lr_1_action_table(grammar)
    assert len(actions) == 9, len(actions)
    # state 1
    action = _lu.Action(state=state_2)
    assert actions[state_1, 'expr'] == action
    action = _lu.Action(state=state_5)
    assert actions[state_1, 'A'] == action
    # state 2
    action = _lu.Action(state=state_3)
    assert actions[state_2, '+'] == action
    # state 3
    action = _lu.Action(state=state_4)
    assert actions[state_3, 'A'] == action
    # reductions
    # state 2
    eq = _grm.Production(
        ROOT,
        ['expr'])
    action = _lu.Action(equation=eq)
    assert actions[state_2, END] == action
    # state 4
    eq = _grm.Production(
        'expr',
        ['expr', '+', 'A'])
    action = _lu.Action(equation=eq)
    assert actions[state_4, '+'] == action
    assert actions[state_4, END] == action
    # state 5
    eq = _grm.Production(
        'expr',
        ['A'])
    action = _lu.Action(equation=eq)
    assert actions[state_5, '+'] == action
    assert actions[state_5, END] == action


def test_collect_lr_1_states():
    _collect_lr_1_states()


def _collect_lr_1_states():
    grammar, first_sets = _make_grammar_expr_plus()
    states = _lr._collect_lr_1_states(
        grammar, first_sets)
    assert len(states) == 5, len(states)
    item_1 = _lu.Dot(
        symbol=ROOT,
        done=tuple(),
        rest=('expr',),
        lookahead=END)
    state_1 = _lr._closure_lr_1(
        {item_1}, grammar, first_sets)
    assert state_1 in states, states
    item_2 = _lu.Dot(
        symbol=ROOT,
        done=('expr',),
        rest=tuple(),
        lookahead=END)
    item_3 = _lu.Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookahead='+')
    item_4 = _lu.Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'A'),
        lookahead='_END')
    items = {item_2, item_3, item_4}
    state_2 = _lr._closure_lr_1(
        items, grammar, first_sets)
    assert state_2 in states, states
    item_5 = _lu.Dot(
        symbol='expr',
        done=('expr', '+'),
        rest=('A',),
        lookahead='+')
    item_6 = _lu.Dot(
        symbol='expr',
        done=('expr', '+'),
        rest=('A',),
        lookahead='_END')
    items = {item_5, item_6}
    state_3 = _lr._closure_lr_1(
        items, grammar, first_sets)
    assert state_3 in states, states
    item_7 = _lu.Dot(
        symbol='expr',
        done=('expr', '+', 'A'),
        rest=tuple(),
        lookahead='+')
    item_8 = _lu.Dot(
        symbol='expr',
        done=('expr', '+', 'A'),
        rest=tuple(),
        lookahead='_END')
    items = {item_7, item_8}
    state_4 = _lr._closure_lr_1(
        items, grammar, first_sets)
    assert state_4 in states
    item_9 = _lu.Dot(
        symbol='expr',
        done=('A',),
        rest=tuple(),
        lookahead='+')
    item_10 = _lu.Dot(
        symbol='expr',
        done=('A',),
        rest=tuple(),
        lookahead='_END')
    items = {item_9, item_10}
    state_5 = _lr._closure_lr_1(
        items, grammar, first_sets)
    assert state_5 in states
    return [
        state_1, state_2, state_3,
        state_4, state_5]


def _make_grammar_expr_plus():
    root_symbol = 'expr'
    equations = [
        _grm.Production(
            ROOT,
            ['expr']),
        _grm.Production(
            'expr',
            ['A']),
        _grm.Production(
            'expr',
            ['expr', '+', 'A']),
        ]
    grammar = _grm.Grammar(
        root_symbol=root_symbol,
        equations=equations)
    first_sets = {
        'expr': {'expr', 'A'},
        '+': {'+'},
        'A': {'A'}}
    first_sets[END] = {END}
    return grammar, first_sets


def test_successors_of_lr_1_state():
    item = _lu.Dot(
        symbol=ROOT,
        done=tuple(),
        rest=('expr',),
        lookahead=END)
    state = {item}
    grammar, first_sets = _make_grammar()
    successors = _lr._successors_of_lr_1_state(
        state, grammar, first_sets)
    assert len(successors) == 1, successors
    next_state, = successors
    item_root = _lu.Dot(
        symbol=ROOT,
        done=('expr',),
        rest=tuple(),
        lookahead=END)
    item_plus = _lu.Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'expr'),
        lookahead='+')
    item_end = _lu.Dot(
        symbol='expr',
        done=('expr',),
        rest=('+', 'expr'),
        lookahead=END)
    next_state_ = {item_root, item_plus, item_end}
    assert next_state == next_state_, next_state


def test_closure_lr_1():
    item = _lu.Dot(
        symbol=ROOT,
        done=tuple(),
        rest=('expr',),
        lookahead=END)
    items = {item}
    grammar, first_sets = _make_grammar()
    closure = _lr._closure_lr_1(
        items, grammar, first_sets)
    item_plus = _lu.Dot(
        symbol='expr',
        done=tuple(),
        rest=('expr', '+', 'expr'),
        lookahead='+')
    item_end = _lu.Dot(
        symbol='expr',
        done=tuple(),
        rest=('expr', '+', 'expr'),
        lookahead=END)
    closure_ = {
        item, item_plus, item_end}
    assert closure == closure_, closure


def _make_grammar():
    root_symbol = 'expr'
    equations = [
        _grm.Production(
            'expr',
            ['expr', '+', 'expr']),
        ]
    grammar = _grm.Grammar(
        root_symbol=root_symbol,
        equations=equations)
    first_sets = {
        'expr': {'expr'},
        '+': {'+'}}
    first_sets[END] = {END}
    return grammar, first_sets


def test_partition_lr_state():
    item_plus = _lu.Dot(
        symbol='expr',
        done=tuple(),
        rest=('+', 'expr'),
        lookahead='a')
    item_minus = _lu.Dot(
        symbol='expr',
        done=tuple(),
        rest=('-', 'expr'),
        lookahead='a')
    state = {item_plus, item_minus}
    parts = list(_lr._partition_lr_state(state))
    assert len(parts) == 2, parts
    parts_ = [{item_plus}, {item_minus}]
    for part in parts:
        parts_.remove(part)
    assert not parts_, parts


if __name__ == '__main__':
    test_make_lr_1_action_table()
    # test_collect_lr_1_states()
    # test_successors_of_lr_1_state()
    # test_closure_lr_1()
    # test_partition_lr_state()
