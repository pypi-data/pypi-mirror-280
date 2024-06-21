"""Tests for `parstools._grammars`."""
import itertools as _itr

import parstools._grammars as _grm
import parstools._lex as _lex
import parstools._lr.lr as _lr
import pytest


def test_grammar_init():
    prod_1 = _grm.Production(
        'sum',
        ['sum', '+', 'product'])
    prod_2 = _grm.Production(
        'sum',
        ['product'])
    prod_3 = _grm.Production(
        'product',
        ['product', '*', 'number'])
    prod_4 = _grm.Production(
        'product',
        ['number'])
    equations = [
        prod_1, prod_2, prod_3, prod_4]
    grammar = _grm.Grammar(
        root_symbol='sum',
        equations=equations)
    assert grammar.root_symbol == 'sum', grammar.root_symbol
    assert grammar.equations == equations, grammar.equations
    leafs = {'number', '+', '*', _grm.END}
    assert grammar.leafs == leafs, grammar.leafs
    nonleafs = {'sum', 'product'}
    assert grammar.nonleafs == nonleafs, grammar.nonleafs
    symbols = leafs | nonleafs
    assert grammar.symbols == symbols, grammar.symbols
    groups = dict(
        sum={prod_1, prod_2},
        product={prod_3, prod_4})
    assert grammar.groups == groups, grammar.groups


def test_duplicate_productions():
    equations = [
        _grm.Production('sum', ['sum', '+', 'product']),
        _grm.Production('sum', ['sum', '+', 'product']),
        ]
    with pytest.raises(ValueError):
        _grm.Grammar(
            root_symbol='sum',
            equations=equations)


def test_root_symbol():
    equations = [
        _grm.Production('sum', ['sum', '+', 'product']),
        _grm.Production('sum', ['product']),
        ]
    with pytest.raises(ValueError):
        _grm.Grammar(
            root_symbol='expr',
            equations=equations)


def test_predefined_symbols():
    equations = [
        _grm.Production('sum', [_grm.ROOT]),
        _grm.Production('sum', ['sum', '+', 'product']),
        ]
    with pytest.raises(ValueError):
        _grm.Grammar(
            root_symbol='sum',
            equations=equations)
    equations = [
        _grm.Production('sum', [_grm.END]),
        ]
    with pytest.raises(ValueError):
        _grm.Grammar(
            root_symbol='sum',
            equations=equations)


def test_pick_random_tree():
    equations = [
        _grm.Production('sum', ['sum', '+', 'number']),
        _grm.Production('sum', ['number']),
        ]
    grammar = _grm.Grammar(
        root_symbol='sum',
        equations=equations)
    tree = _grm.pick_random_tree(grammar, 'sum')
    print(tree)
    def flatten(
            tree:
                list
            ) -> list:
        match tree:
            case str():
                return [tree]
            case list():
                results = list()
                for node in tree:
                    results.extend(
                        flatten(node))
                return results
            case _:
                raise ValueError(tree)
    flat = flatten(tree)
    print(flat)
    last_item = '+'
    for item in flat:
        assert item in {'number', '+'}, item
        assert last_item != item, item
        last_item = item


def test_pick_random_string():
    equations = [
        _grm.Production(
            'sum',
            ['sum', 'PLUS', 'product']),
        _grm.Production(
            'sum',
            ['product']),
        _grm.Production(
            'product',
            ['product', 'ASTERISK', 'number']),
        _grm.Production(
            'product',
            ['number']),
        ]
    grammar = _grm.Grammar(
        root_symbol='sum',
        equations=equations)
    text = _grm.pick_random_string(grammar, 'sum')
    print(text)
    assert 'number' in text, text
    parser = _lr.make_parser(grammar)
    tokens = list(_lex_sum_product(text))
    for token in tokens:
        print(token)
    tree = parser.parse(tokens)
    assert tree is not None
    print(tree)


def _lex_sum_product(
        text):
    token_to_lexeme = {
        'PLUS':
            'PLUS',
        'ASTERISK':
            'ASTERISK',
        'number':
            'number'}
    lexer = _lex.Lexer(
        token_to_lexeme,
        omit_regex=r' \s* ')
    return lexer.parse(text)


if __name__ == '__main__':
    test_pick_random_string()
