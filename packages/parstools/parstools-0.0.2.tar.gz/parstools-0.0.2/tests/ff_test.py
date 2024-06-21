"""Tests for module `parstools._ff`."""
import parstools._ff as _ff
import parstools._grammars as _grm


ROOT = _grm.ROOT
END = _grm.END
Prod = _grm.Production


def test_compute_first_sets():
    equations = [
        Prod('expr', ['expr', '+', 'A']),
        Prod('expr', ['B']),
        ]
    first_sets = _ff.compute_first_sets(equations)
    first_sets_ = {
        'expr': {'expr', 'B'},
        '+': {'+'},
        'A': {'A'},
        'B': {'B'},
        '': {''}}
    first_sets_[END] = {END}
    assert first_sets == first_sets_, first_sets


def test_compute_follow_sets():
    equations = [
        Prod('expr', ['expr', '+', 'A']),
        Prod('expr', ['B']),
        ]
    first_sets = _ff.compute_first_sets(equations)
    follow_sets = _ff.compute_follow_sets(
        equations, first_sets)
    follow_sets_ = {
        'expr': {'+'},
        '+': {'A'},
        'A': {'+'},
        'B': {'+'}}
    follow_sets_[ROOT] = {END}
    assert follow_sets == follow_sets_, follow_sets


def test_is_left_recursive():
    equations = [
        Prod('expr', ['expr', '+', 'A']),
        Prod('expr', ['A']),
        ]
    grammar = _grm.Grammar(
        root_symbol='expr',
        equations=equations)
    assert _ff.is_left_recursive(grammar)
    assert not _ff.is_right_recursive(grammar)
    equations = [
        Prod('expr', ['A', '+', 'expr']),
        Prod('expr', ['A']),
        ]
    grammar = _grm.Grammar(
        root_symbol='expr',
        equations=equations)
    assert not _ff.is_left_recursive(grammar)
    assert _ff.is_right_recursive(grammar)


if __name__ == '__main__':
    test_compute_first_sets()
    test_compute_follow_sets()
    test_is_left_recursive()
