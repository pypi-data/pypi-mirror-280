"""Generating parsers from grammars specified in TLA+."""
import collections.abc as _abc
import itertools as _itr
import typing as _ty

import parstools._grammars as _grm
import parstools._lex as _lex
import parstools._lr.lr as _lr
import parstools._lr.parser as _p


_Item = _ty.TypeVar('_Item')
_Production = _grm.Production
_Grammar = _grm.Grammar
_Result = _p.Result
_Parser = _p.Parser


def bootstrap_tla_grammar_parser(
        ) -> _Parser:
    lexer = make_lexer()
    parser_1 = _bootstrap_stage_1(lexer)
    parser_2 = _bootstrap_stage_2(lexer, parser_1)
    print('bootstrapping:')
    print('parser 1:')
    print(parser_1)
    print('parser 2:')
    print(parser_2)
    return parser_2


def _bootstrap_stage_1(
        lexer:
            _lex.Lexer
        ) -> _Parser:
    grammar = stage_1_tla_as_grammar()
    parser = _lr.make_lr_tables(grammar, 1)
    # make parser from `str`
    grammar_string = stage_1_tla_as_str()
    tokens = lexer.parse(grammar_string)
    tree = parser.parse(tokens)
    if tree is None:
        raise AssertionError(tree)
    grammar_ = derivation_to_grammar(tree)
    if grammar != grammar_:
        raise AssertionError(grammar, grammar_)
    return parser


def _bootstrap_stage_2(
        lexer:
            _lex.Lexer,
        parser_1:
            _Parser
        ) -> _Parser:
    grammar_string = stage_2_tla_as_str()
    tokens = lexer.parse(grammar_string)
    tree = parser_1.parse(tokens)
    if tree is None:
        raise AssertionError(tree)
    grammar = derivation_to_grammar(tree)
    return _lr.make_lr_tables(grammar, 1)


def stage_1_tla_as_grammar(
        ) -> _Grammar:
    """Grammar that of language for writing grammars.

    This is the start of developing bootstrapping.
    """
    root_symbol = 'equations'
    equations = [
        _Production(
            'equations',
            ['equations', 'AND', 'equation']),
        _Production(
            'equations',
            ['equation']),
        _Production(
            'equation',
            ['NAME', 'EQ', 'union']),
        _Production(
            'union',
            ['union', 'PIPE', 'join']),
        _Production(
            'union',
            ['join']),
        _Production(
            'join',
            ['join', 'ET', 'NAME']),
        _Production(
            'join',
            ['NAME']),
        ]
    return _Grammar(
        root_symbol,
        equations)


def stage_1_tla_as_str(
        ) -> str:
    """Conjunction of `= | &`."""
    return r'''
           equations =
                  equations & AND & equation
                | equation
        /\ equation =
                NAME & EQ & union
        /\ union =
                  union & PIPE & join
                | join
        /\ join =
                  join & ET & NAME
                | NAME
        '''


def stage_2_tla_as_str(
        ) -> str:
    """Dotted identifiers."""
    return r'''
           conjunction =
                  conjunction & AND & conjunct
                | conjunct
        /\ conjunct =
                symbol & EQ & union
        /\ union =
                  union & PIPE & cat
                | cat
        /\ cat =
                  cat & ET & symbol
                | symbol
        /\ symbol =
                  NAME & DOT & NAME
                | NAME
        '''


def lex_kw_as_name(
        text:
            str,
        keywords_as_names
        ) -> _abc.Iterable[
            _lex.Token]:
    """Return tokens."""
    tla_tokens = lex(text)
    tokens = list()
    for token in tla_tokens:
        if token.value in keywords_as_names:
            symbol = 'NAME'
        else:
            symbol = token.symbol
        token = _lex.Token(
            symbol=symbol,
            value=token.value,
            row=token.row,
            column=token.column)
        tokens.append(token)
    return tokens


def lex(
        text:
            str
        ) -> _abc.Iterable[
            _lex.Token]:
    """Return tokens for `text`."""
    lexer = make_lexer()
    tokens = lexer.parse(text)
    return list(field_follows_dot(
        tokens, lexer))


def make_lexer(
        ) -> _lex.Lexer:
    """Return lexer."""
    token_to_lexeme = {
        'AND':
            '/\\',
        'DOUBLE_EQ':
            '==',
        'EQ':
            '=',
        'PIPE':
            '|',
        'ET':
            '&',
        'DOT':
            '.'}
    token_to_regex = {
        'NAME':
            ' [a-zA-Z0-9_]+ '}
    keywords = {
        'LET', 'IN'}
    return _lex.Lexer(
        token_to_regex,
        token_to_lexeme=token_to_lexeme,
        keywords=keywords)


def field_follows_dot(
        tokens:
            _abc.Iterable[
                _lex.Token],
        lexer:
            _lex.Lexer
        ) -> _abc.Iterable[
            _lex.Token]:
    """Each `.` is followed by a field `NAME`."""
    prev_is_dot = False
    for token in tokens:
        if token.value == '.':
            prev_is_dot = True
            yield token
            continue
        elif (prev_is_dot and
                token.value in lexer._keywords):
            symbol = 'NAME'
            token = _lex.Token(
                symbol=symbol,
                value=token.value,
                row=token.row,
                column=token.column)
        yield token
        prev_is_dot = False


def derivation_to_grammar(
        derivation:
            _Result
        ) -> _Grammar:
    tree = derivation_to_syntax_tree(derivation)
    return syntax_tree_to_grammar(tree)


def derivation_to_syntax_tree(
        derivation:
            _Result
        ) -> _Result:
    """Return syntax tree."""
    value = derivation.value
    # leaf ?
    if isinstance(value, str):
        return derivation
    conv = derivation_to_syntax_tree
    match len(value):
        case 1:
            # unit production: contractible
            u, = value
            return conv(u)
        case 3:
            u, op, v = value
            if not isinstance(op.value, str):
                raise AssertionError(op)
            p = conv(u)
            q = conv(v)
            return _Result(
                symbol=op.value,
                value=(p, q))
    raise AssertionError(
        len(value), derivation.symbol)


def syntax_tree_to_grammar(
        stx_tree:
            _Result
        ) -> _Grammar:
    """Return grammar for parser generator."""
    equations = _conv_stx_to_grm(stx_tree)
    # for eq in equations:
    #     print(repr(eq))
    start_eq = equations[0]
    root_symbol = start_eq.symbol
    return _Grammar(
        root_symbol,
        equations)


def _conv_stx_to_grm(
        stx_tree:
            _Result
        ) -> list[_Production]:
    """Return grammar from syntax tree."""
    # leaf ?
    if isinstance(stx_tree.value, str):
        return [_Production(None, [stx_tree.value])]
    conv = _conv_stx_to_grm
    items = list(map(
        conv, stx_tree.value))
    match stx_tree.symbol:
        case '/\\':
            return _flatten_list(items)
        case '=':
            (nonleaf,), productions = items
            return [
                _Production(
                    nonleaf.expansion[0],
                    eq.expansion)
                for eq in productions]
        case '|':
            return _flatten_list(items)
        case '&':
            expansion = list()
            for eq in _itr.chain(*items):
                expansion.extend(eq.expansion)
            return [_Production(None, expansion)]
    raise AssertionError(
        stx_tree.symbol)


def _flatten_list(
        items:
            list[list[_Item]]
        ) -> list[_Item]:
    """Unnest list of lists."""
    result = list()
    for span in items:
        if not isinstance(span, list):
            result.append(span)
            continue
        result.extend(span)
    return result
