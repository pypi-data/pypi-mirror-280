"""Tests for `parstools._re`."""
import parstools._grammars as _grm
import parstools._re as _re
import parstools._trees as _tree


def test_lex_regex():
    regex = '(( a* ) & b ) | c'
    tokens = _re.lex_regex(regex)
    symbol_value = [
        ('LPAREN', '('),
        ('LPAREN', '('),
        ('NAME', 'a'),
        ('ASTERISK', '*'),
        ('RPAREN', ')'),
        ('ET', '&'),
        ('NAME', 'b'),
        ('RPAREN', ')'),
        ('PIPE', '|'),
        ('NAME', 'c'),
        ]
    items = zip(tokens, symbol_value)
    for token, (symbol, value) in items:
        assert token.symbol == symbol, (token, symbol)
        assert token.value == value, (token, value)


def test_parse_regex():
    regex = '(( a* ) & b ) | c'
    tree = _re.parse_regex(regex)
    assert tree is not None
    _tree.pprint_tree(tree)


def test_parse_regex_to_result():
    text = '''
        (a*) | b
        '''
    tree = _re.parse_regex_to_result(text)
    assert tree is not None
    _tree.pprint_tree(tree)


def test_regex_to_nfa():
    text = '''
        a
        '''
    nfa = _re.regex_to_nfa(text)
    assert nfa.initial_node == 0, nfa.initial_node
    assert nfa.accepting_nodes == {1}, nfa.accepting_nodes
    edges = {
        0: {'a': {1}}}
    assert nfa.edges == edges, nfa.edges
    # print(nfa)
    # nfa_to_dot(nfa)
    text = '''
        a & b
        '''
    nfa = _re.regex_to_nfa(text)
    assert nfa.initial_node == 0, nfa.initial_node
    assert nfa.accepting_nodes == {3}, nfa.accepting_nodes
    edges = {
        0: {'a': {2}},
        2: {'b': {3}}}
    assert nfa.edges == edges, nfa.edges
    # print(nfa)
    text = '''
        a & b & b*
        '''
    nfa = _re.regex_to_nfa(text)
    assert nfa.initial_node == 0, nfa.initial_node
    assert nfa.accepting_nodes == {4}, nfa.accepting_nodes
    edges = {
        0: {'a': {2}},
        2: {'b': {4}},
        4: {'b': {4}}}
    assert nfa.edges == edges, nfa.edges
    # print(nfa)
    text = '''
        a*
        '''
    nfa = _re.regex_to_nfa(text)
    assert nfa.initial_node == 0, nfa.initial_node
    assert nfa.accepting_nodes == {0}, nfa.accepting_nodes
    edges = {
        0: {'a': {0}}}
    assert nfa.edges == edges, nfa.edges
    # print(nfa)


def test_match_regex():
    regex = ' a & a* '
    text = 'aa'
    pos = _re.match_regex(regex, text)
    assert pos == {1, 2}, pos
    regex = ' a & b* '
    text = 'abbb'
    pos = _re.match_regex(regex, text)
    assert pos == {1, 2, 3, 4}, pos
    regex = ' b & a & b* '
    text = 'abbb'
    pos = _re.match_regex(regex, text)
    assert pos == set(), pos
    regex = ' b & a & b* '
    text = 'babab'
    pos = _re.match_regex(regex, text)
    assert pos == {2, 3}, pos
    regex = ' b & (a | b) '
    text = 'babab'
    pos = _re.match_regex(regex, text)
    assert pos == {2}, pos
    regex = ' a* '
    text = 'a b'
    pos = _re.match_regex(regex, text)
    assert pos == {0, 1}, pos
    regex = ' a* & (b | c) & d '
    text = 'aaaaabd'
    pos = _re.match_regex(regex, text)
    assert pos == {7}, pos
    nfa = _re.regex_to_nfa(regex)
    _re.nfa_to_dot(nfa, 'nfa.pdf')


def test_difference():
    initial_node = 1
    accepting_nodes = {2}
    edges = {
        1: {'a': {2}},
        2: {'a': {2}},
        }
    graph = _re.NFA(
        initial_node,
        accepting_nodes,
        edges)
    edges = {
        1: {'a': {2}},
        2: {'a': {3}},
        3: {'a': {4}},
        4: dict(),
        }
    accepting_nodes = {4}
    other_graph = _re.NFA(
        initial_node,
        accepting_nodes,
        edges)
    diff = _re.nfa_difference(
        graph, other_graph)
    assert diff.initial_node == (1, 1), (
        diff.initial_node)
    assert diff.accepting_nodes == {
        (2, 2), (2, 3), (2, 0)
        }, diff.accepting_nodes
    assert diff.edges == {
        (1, 1): {'a': {(2, 2)}},
        (2, 2): {'a': {(2, 3)}},
        (2, 3): {'a': {(2, 4)}},
        (2, 4): {'a': {(2, 0)}},
        (2, 0): {'a': {(2, 0)}},
        }, diff.edges


def test_intersection():
    initial_node = 1
    accepting_nodes = {2}
    edges = {
        1: {'a': {2}},
        2: {'b': {3}},
        3: dict(),
        }
    graph = _re.NFA(
        initial_node,
        accepting_nodes,
        edges)
    edges = {
        1: {'a': {2}},
        2: dict(),
        }
    other_graph = _re.NFA(
        initial_node,
        accepting_nodes,
        edges)
    isect = _re.nfa_intersection(
        graph, other_graph)
    assert isect.initial_node == (1, 1)
    assert isect.accepting_nodes == {(2, 2)}
    assert isect.edges == {
        (1, 1): {'a': {(2, 2)}},
        }, isect.edges


def test_regex_to_nfa_concat():
    Tree = _re.Tree
    # (a | b) & c
    a_tree = Tree(
        symbol='NAME',
        value='a')
    b_tree = Tree(
        symbol='NAME',
        value='b')
    c_tree = Tree(
        symbol='NAME',
        value='c')
    pipe_tree = Tree(
        symbol='|',
        value=(a_tree, b_tree))
    et_tree = Tree(
        symbol='&',
        value=(pipe_tree, c_tree))
    nfa = _re.regex_tree_to_nfa(
        et_tree)
    init = nfa.initial_node
    assert init == 2, init
    accepting_nodes = nfa.accepting_nodes
    assert accepting_nodes == {5}, accepting_nodes
    edges_ = {
        2: {'a': {4}, 'b': {4}},
        4: {'c': {5}},
        }
    assert nfa.edges == edges_, nfa.edges


def test_nfa_to_grammar_a():
    initial_node = 1
    accepting_nodes = {1}
    edges = {
        1: {'a': {1}},
        }
    nfa = _re.NFA(
        initial_node,
        accepting_nodes,
        edges)
    grammar = _re.nfa_to_grammar(nfa)
    assert grammar.root_symbol == 'nonleaf_0', (
        grammar.root_symbol)
    assert len(grammar.equations) == 3, grammar.equations
    eq_1 = _grm.Production(
        symbol='nonleaf_0',
        expansion=['a', 'nonleaf_0'])
    assert eq_1 in grammar.equations, grammar.equations
    eq_2 = _grm.Production(
        symbol='nonleaf_0',
        expansion=['a'])
    assert eq_2 in grammar.equations, grammar.equations
    eq_3 = _grm.Production(
        symbol='nonleaf_0',
        expansion=list())
    assert eq_3 in grammar.equations, grammar.equations


def test_nfa_to_grammar_ab():
    initial_node = 1
    accepting_nodes = {3}
    edges = {
        1: {'a': {2}},
        2: {'b': {3}},
        }
    nfa = _re.NFA(
        initial_node,
        accepting_nodes,
        edges)
    grammar = _re.nfa_to_grammar(nfa)
    assert grammar.root_symbol == 'nonleaf_0', (
        grammar.root_symbol)
    assert len(grammar.equations) == 2, grammar.equations
    eq_1 = _grm.Production(
        symbol='nonleaf_0',
        expansion=['a', 'nonleaf_1'])
    assert eq_1 in grammar.equations, grammar.equations
    eq_2 = _grm.Production(
        symbol='nonleaf_1',
        expansion=['b'])
    assert eq_2 in grammar.equations, grammar.equations


def test_nfa_to_grammar_a_or_b():
    initial_node = 1
    accepting_nodes = {2, 3}
    edges = {
        1: {'a': {2}, 'b': {3}},
        }
    nfa = _re.NFA(
        initial_node,
        accepting_nodes,
        edges)
    grammar = _re.nfa_to_grammar(nfa)
    assert grammar.root_symbol == 'nonleaf_0', (
        grammar.root_symbol)
    assert len(grammar.equations) == 2, grammar.equations
    eq_1 = _grm.Production(
        symbol='nonleaf_0',
        expansion=['a'])
    assert eq_1 in grammar.equations, grammar.equations
    eq_2 = _grm.Production(
        symbol='nonleaf_0',
        expansion=['b'])
    assert eq_2 in grammar.equations, grammar.equations


def test_is_regular_grammar():
    grammar = grammar_an_b_am()
    assert _re.is_regular_grammar(grammar)
    Prod = _grm.Production
    equations = [
        Prod('S', ['S', 'a']),
        Prod('S', ['a']),
        ]
    root_symbol = 'S'
    grammar = _grm.Grammar(
        root_symbol, equations)
    assert not _re.is_regular_grammar(grammar)


def test_grammar_to_regex_a_or_b():
    # a | b
    grammar = grammar_a_or_b()
    regex = _re.grammar_to_regex(grammar)
    regex_1 = '(((a)) | ((b)))'
    regex_2 = '(((b)) | ((a)))'
    assert (
        regex == regex_1 or
        regex == regex_2), regex


def test_grammar_to_regex_an_a():
    # a* & a
    grammar = grammar_an_a()
    regex = _re.grammar_to_regex(grammar)
    regex_ = '(( ((a))* )) & (((a)))'
    assert regex == regex_, regex


def test_grammar_to_regex_an_b():
    # a* & a
    grammar = grammar_an_b()
    regex = _re.grammar_to_regex(grammar)
    regex_ = '(( ((a))* )) & (((b)))'
    assert regex == regex_, regex


def test_grammar_to_regex_an_b_am():
    # a* & a & b & a* & a
    grammar = grammar_an_b_am()
    regex = _re.grammar_to_regex(grammar)
    # regex_ = (
    #     '(( ((a))* )) & (((a) & '
    #     '((((b) & ((( ((a))* )) & (((a)))))))))')
    # regex = (
    #     '(( ((a))* )) & (((a) & '
    #     '((((b) & (( ((a))* ) & (((a)))))))))')
    # assert regex == regex_, regex
    nfa = _re.regex_to_nfa(regex)
    # _re.nfa_to_dot(nfa, 'nfa.pdf')
    assert nfa.initial_node == 2, nfa.initial_node
    assert nfa.accepting_nodes == {9}, nfa.accepting_nodes
    edges_ = {
        2: {'a': {2, 4}},
        4: {'b': {8}},
        8: {'a': {8, 9}}}
    assert nfa.edges == edges_, nfa.edges


def grammar_a_or_b(
        ) -> _grm.Grammar:
    Prod = _grm.Production
    root_symbol = 'S'
    equations = [
        Prod('S', ['a']),
        Prod('S', ['b']),
        ]
    return _grm.Grammar(
        root_symbol, equations)


def grammar_an_a(
        ) -> _grm.Grammar:
    Prod = _grm.Production
    root_symbol = 'S'
    equations = [
        Prod('S', ['a', 'S']),
        Prod('S', ['a']),
        ]
    return _grm.Grammar(
        root_symbol, equations)


def grammar_an_b(
        ) -> _grm.Grammar:
    Prod = _grm.Production
    root_symbol = 'S'
    equations = [
        Prod('S', ['a', 'S']),
        Prod('S', ['b']),
        ]
    return _grm.Grammar(
        root_symbol, equations)


def grammar_an_b_am(
        ) -> _grm.Grammar:
    Prod = _grm.Production
    root_symbol = 'S'
    equations = [
        Prod('S', ['a', 'S']),
        Prod('S', ['a', 'B']),
        Prod('B', ['b', 'C']),
        Prod('C', ['a', 'C']),
        Prod('C', ['a']),
        ]
    return _grm.Grammar(
        root_symbol, equations)


if __name__ == '__main__':
    # test_match_regex()
    test_grammar_to_regex_an_b()
    # test_grammar_to_regex()
    # test_regex_to_nfa_concat()
