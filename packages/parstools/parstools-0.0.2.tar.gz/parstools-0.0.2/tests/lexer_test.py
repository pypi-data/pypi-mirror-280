"""Test `parstools._lex`."""
import collections.abc as _abc
import logging
import re

import parstools._lex as _lex
import pytest


Token = _lex.Token


def test_check_regex_lexeme_overlap():
    token_to_regex = dict(
        DASH_LINE=
            '-+')
    token_to_lexeme = dict(
        DASHES=
            '----')
    with pytest.raises(ValueError):
        _lex._check_regex_lexeme_overlap(
            token_to_regex,
            token_to_lexeme)


def test_check_regex_regex_overlap():
    token_to_regex = dict(
        DASH_LINE=
            '- & - & - & - & -*',
        DASHES=
            '- & -*')
    with pytest.raises(ValueError):
        _lex.check_regex_regex_overlap(
            token_to_regex)


def test_lexer_parsing():
    log = logging.getLogger(
        'parstools._lex')
    log.setLevel(logging.INFO)
    log.addHandler(
        logging.StreamHandler())
    # define lexer
    token_to_lexeme = dict(
        ET=
            '&',
        PIPE=
            '|',
        EQ=
            '=',
        AND=
            '/\\')
    letter_ = ' [a-zA-Z_] '
    az_num = ' [a-zA-Z_0-9] '
    token_to_regex = {
        'NAME':
            rf' {letter_} '
            rf' ({az_num})* '}
    omit_regex = r' \s* '
    lexer = _lex.Lexer(
        token_to_regex,
        token_to_lexeme=token_to_lexeme,
        omit_regex=omit_regex)
    # parse string
    text = r'''
           equations =
                  equations & AND & equation
                | equation
        /\ equation =
                NAME & EQ & union
        '''
    # occs = [
    #     m.start()
    #     for m in
    #         re.finditer('equations', text)]
    # print(occs)
    tokens = list(lexer.parse(text))
    tokens = _lex.add_row_column(
        text, tokens)
    tokens_ = [
        Token(
            symbol='NAME',
            value='equations',
            row=1,
            column=11,
            start=12),
        Token(
            symbol='EQ',
            value='=',
            row=1,
            column=21,
            start=22),
        Token(
            symbol='NAME',
            value='equations',
            row=2,
            column=18,
            start=42),
        Token(
            symbol='ET',
            value='&',
            row=2,
            column=28,
            start=52),
        Token(
            symbol='NAME',
            value='AND',
            row=2,
            column=30,
            start=54),
        Token(
            symbol='ET',
            value='&',
            row=2,
            column=34,
            start=58),
        Token(
            symbol='NAME',
            value='equation',
            row=2,
            column=36,
            start=60),
        Token(
            symbol='PIPE',
            value='|',
            row=3,
            column=16,
            start=85),
        Token(
            symbol='NAME',
            value='equation',
            row=3,
            column=18,
            start=87),
        Token(
            symbol='AND',
            value='/\\',
            row=4,
            column=8,
            start=104),
        Token(
            symbol='NAME',
            value='equation',
            row=4,
            column=11,
            start=107),
        Token(
            symbol='EQ',
            value='=',
            row=4,
            column=20,
            start=116),
        Token(
            symbol='NAME',
            value='NAME',
            row=5,
            column=16,
            start=134),
        Token(
            symbol='ET',
            value='&',
            row=5,
            column=21,
            start=139),
        Token(
            symbol='NAME',
            value='EQ',
            row=5,
            column=23,
            start=141),
        Token(
            symbol='ET',
            value='&',
            row=5,
            column=26,
            start=144),
        Token(
            symbol='NAME',
            value='union',
            row=5,
            column=28,
            start=146),
        ]
    _check_tokens(tokens, tokens_)
    tokens_ = lex(text)
    _check_tokens(tokens, tokens_)


def _check_tokens(
        tokens:
            _abc.Iterable[
                Token],
        tokens_:
            _abc.Iterable[
                Token]
        ) -> None:
    """Assert sequences are equal."""
    for token, token_ in zip(tokens, tokens_):
        assert token == token_, f'''
            {token = }
            {token_ = }
            '''


def lex(
        text
        ) -> _abc.Iterable[
            Token]:
    """Return tokens with positional info."""
    tokens = split_with_pos_info(text)
    return list(map(lex_token, tokens))


def lex_token(
        token:
            Token
        ) -> Token:
    """Add symbol to token."""
    lexeme_to_token = {
        '/\\':
            'AND',
        '=':
            'EQ',
        '|':
            'PIPE',
        '&':
            'ET'}
    regex = r' [a-zA-Z0-9_]+ '
    result = re.fullmatch(
        regex,
        token.value,
        flags=re.VERBOSE)
    if result is None:
        symbol = lexeme_to_token.get(
            token.value,
            token.value)
    else:
        symbol = 'NAME'
    return Token(
        symbol=symbol,
        value=token.value,
        row=token.row,
        column=token.column,
        start=token.start)


def split_with_pos_info(
        text:
            str
        ) -> list[
            Token]:
    """Return tokens with positional information.

    Assumes that blankspace is between
    consecutive lexemes.
    """
    blanks = {'\x20', '\n', '\t'}
    current = ''
    row = 0
    column = 0
    start = 0
    for i, char in enumerate(text):
        match char:
            case '\x20':
                if current:
                    yield _make_token_with_pos(
                        current, row,
                        column, start)
                current = ''
                start = i + 1
                column += 1
            case '\n':
                if current:
                    yield _make_token_with_pos(
                        current, row,
                        column, start)
                current = ''
                start = i + 1
                column = 0
                row += 1
            case _:
                current += char
                column += 1


def _make_token_with_pos(
        value:
            str,
        row:
            int,
        end_column:
            int,
        start:
            int
        ) -> Token:
    """Return token with line and column info."""
    start_column = end_column - len(value)
    # print(f'{value = !r}, {start_column = }')
    return _lex.Token(
        symbol=None,
        value=value,
        row=row,
        column=start_column,
        start=start)


def test_omit_regex():
    token_to_regex = {
        'NAME': r'''
            [a-zA-Z]+
            ''',
        }
    lexer = _lex.Lexer(token_to_regex)
    text = ' abc'
    with pytest.raises(ValueError):
        list(lexer.parse(text))
    text = 'abc'
    token, = list(lexer.parse(text))
    token_ = Token(
        symbol='NAME',
        value='abc',
        row=None,
        column=None,
        start=0)
    assert token == token_, token
    lexer = _lex.Lexer(
        token_to_regex,
        omit_regex=r'\s*')
    text = ' abc'
    token, = list(lexer.parse(text))
    token_ = Token(
        symbol='NAME',
        value='abc',
        row=None,
        column=None,
        start=1)
    assert token == token_, token


def test_lex_delimited():
    token_to_regex = {
        'NAME': r'''
            [a-zA-Z]+
            ''',
        }
    token_to_lexeme = {
        'CIRCUMFLEX_ASTERISK': '^*',
        'CIRCUMFLEX': '^',
        'ASTERISK': '*',
        'LPAREN': '(',
        'RPAREN': ')'}
    lexer = _lex.Lexer(
        token_to_regex,
        token_to_lexeme)
    delimiter_regex = r'''
          \( \*
        | \* \)
        '''
    delimiter_pairs = {
        '(*':
            '*)'}
    delimiter_tokens = {
        '(*':
            'MULTILINE_COMMENT'}
    nestable_delimiters = {
        '(*'}
    text = '(x^*)'
    tokens = _lex.lex_delimited(
        text, delimiter_regex, delimiter_pairs,
        delimiter_tokens, nestable_delimiters,
        lexer)
    for token in tokens:
        print(token)
    tokens_ = [
        Token(
            symbol='LPAREN',
            value='(',
            row=0,
            column=0,
            start=0),
        Token(
            symbol='NAME',
            value='x',
            row=0,
            column=1,
            start=1),
        Token(
            symbol='CIRCUMFLEX_ASTERISK',
            value='^*',
            row=0,
            column=2,
            start=2),
        Token(
            'RPAREN',
            ')',
            row=0,
            column=4,
            start=4),
        ]
    assert tokens == tokens_, tokens
    # delimited span
    text = ''' (*
        x^*)
        '''
    lexer = _lex.Lexer(
        token_to_regex,
        token_to_lexeme,
        omit_regex=r' \s* ')
    tokens = _lex.lex_delimited(
        text, delimiter_regex, delimiter_pairs,
        delimiter_tokens, nestable_delimiters,
        lexer)
    tokens_ = [
        Token(
            symbol='MULTILINE_COMMENT',
            value='(*\n        x^*)',
            row=0,
            column=1,
            start=1),
        ]
    assert tokens == tokens_, tokens
    # multi-line input
    text = '''  (
        a * b
        * c
        )
        '''
    tokens = _lex.lex_delimited(
        text, delimiter_regex, delimiter_pairs,
        delimiter_tokens, nestable_delimiters,
        lexer)
    tokens_ = [
        Token(
            symbol='LPAREN',
            value='(',
            row=0,
            column=2,
            start=2),
        Token(
            symbol='NAME',
            value='a',
            row=1,
            column=8,
            start=12),
        Token(
            symbol='ASTERISK',
            value='*',
            row=1,
            column=10,
            start=14),
        Token(
            symbol='NAME',
            value='b',
            row=1,
            column=12,
            start=16),
        Token(
            symbol='ASTERISK',
            value='*',
            row=2,
            column=8,
            start=26),
        Token(
            symbol='NAME',
            value='c',
            row=2,
            column=10,
            start=28),
        Token(
            symbol='RPAREN',
            value=')',
            row=3,
            column=8,
            start=38),
        ]
    assert tokens == tokens_, tokens


class Lexer(
        _lex.MethodsLexer):
    """Lexer with `t_*` methods."""

    def t_NAME(
            self,
            token):
        r' [a-zA-Z]+ '
        return Token(
            symbol=token.symbol,
            value=token.value,
            row=1,
            start=token.start)

    t_PLUS = r' \+ '
    t_omit = r' \s* '


def test_methods_lexer():
    lexer = Lexer()
    text = '''
        x + y
        '''
    tokens = list(
        lexer.parse(text))
    tokens_ = [
        Token(
            symbol='NAME',
            value='x',
            row=1,
            start=9),
        Token(
            symbol='PLUS',
            value='+',
            start=11),
        Token(
            symbol='NAME',
            value='y',
            row=1,
            start=13),
        ]
    assert tokens == tokens_, tokens


class StatefulLexer(
        _lex.StatefulLexer):
    """Lexer with state and `t_*` methods."""

    lexing_states = {
        'initial',
        'other'}

    def t_LPAREN(
            self,
            token):
        r' \( '
        self.lexing_state = 'other'
        return token

    def t_other_RPAREN(
            self,
            token):
        r' \) '
        self.lexing_state = 'initial'
        return token

    def t_other_ALPHA(
            self,
            token):
        r' [a-zA-Z]+ '
        return token


def test_stateful_lexer_2_states():
    lexer = StatefulLexer()
    text = '(abc)(abc)'
    tokens = list(
        lexer.parse(text))
    tokens_ = [
        Token(
            symbol='LPAREN',
            value='(',
            start=0),
        Token(
            symbol='ALPHA',
            value='abc',
            start=1),
        Token(
            symbol='RPAREN',
            value=')',
            start=4),
        Token(
            symbol='LPAREN',
            value='(',
            start=5),
        Token(
            symbol='ALPHA',
            value='abc',
            start=6),
        Token(
            symbol='RPAREN',
            value=')',
            start=9),
        ]
    assert tokens == tokens_, tokens


class StatefulLexerStrings(
        _lex.StatefulLexer):
    """Lexer for strings."""

    lexing_states = {
        'initial',
        'string'}

    t_omit = r' \s* '

    def t_opening_string(
            self,
            token):
        r' " '
        self.lexing_state = 'string'
        self._string_start = token.start

    def t_string_escaped_quote(
            self,
            token):
        r' \\ " '

    def t_string_other_char(
            self,
            token):
        r' [^"\\]+ '

    def t_string_quote(
            self,
            token):
        r' " '
        self.lexing_state = 'initial'
        start = self._string_start
        end = token.start + len(token.value)
        span = self.input_text[
            start:end]
        return Token(
            symbol='STRING',
            value=span,
            start=start)


def test_stateful_lexer_omit_pattern():
    lexer = StatefulLexerStrings()
    text = ' "abc"  "def" '
    tokens = list(
        lexer.parse(text))
    tokens_ = [
        Token(
            symbol='STRING',
            value='"abc"',
            start=1),
        Token(
            symbol='STRING',
            value='"def"',
            start=8),
        ]
    assert tokens == tokens_, tokens


class StatefulLexerBlanks(
        _lex.StatefulLexer):

    lexing_states = {
        'letters',
        'numerals'}

    t_omit = r' \s* '
    t_letters_omit = r' \s* '
    t_numerals_omit = r' \s* '

    def t_opening_letters(
            self,
            token):
        r' \[ '
        self.lexing_state = 'letters'
        self._span_start = token.start

    def t_letters_contents(
            self,
            token):
        r' [a-zA-Z]+ '

    def t_letters_bracket(
            self,
            token):
        r' \] '
        self.lexing_state = 'initial'
        start = self._span_start + 1
        end = token.start
        span = self.input_text[start:end]
        return Token(
            symbol='LETTERS',
            value=span,
            start=start)

    def t_opening_numerals(
            self,
            token):
        r' \( '
        self.lexing_state = 'numerals'
        self._span_start = token.start

    def t_numerals_contents(
            self,
            token):
        r' [0-9]+ '

    def t_numerals_parenthesis(
            self,
            token):
        r' \) '
        self.lexing_state = 'initial'
        start = self._span_start
        end = token.start + 1
        span = self.input_text[start:end]
        return Token(
            symbol='NUMERALS',
            value=span,
            start=start)


def test_stateful_lexer_3_states():
    lexer = StatefulLexerBlanks()
    text = '''
        [abc]
        (123)
        [def]
        '''
    tokens = list(
        lexer.parse(text))
    tokens_ = [
        Token(
            symbol='LETTERS',
            value='abc',
            start=10),
        Token(
            symbol='NUMERALS',
            value='(123)',
            start=23),
        Token(
            symbol='LETTERS',
            value='def',
            start=38),
        ]
    assert tokens == tokens_, tokens


if __name__ == '__main__':
    # test_check_regex_regex_overlap()
    # test_lex_delimited()
    # test_omit_regex()
    # test_methods_lexer()
    test_stateful_lexer_3_states()
    # test_stateful_lexer_omit_pattern()
