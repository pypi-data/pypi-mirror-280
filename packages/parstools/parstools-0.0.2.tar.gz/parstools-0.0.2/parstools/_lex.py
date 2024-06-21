"""Lexing infrastructure."""
import collections as _cl
import collections.abc as _abc
import inspect
import logging
import re
import textwrap as _tw
import typing as _ty

import parstools._re as _re


_log = logging.getLogger(__name__)
INITIAL_STATE: _ty.Final = 'initial'


class Token(
        _ty.NamedTuple):
    """Treelet.

    Includes positional information
    for string `value`.
    """

    symbol: str
    value: str
    row: int | None = None
    column: int | None = None
    start: int | None = None


def pprint_token(
        token:
            Token
        ) -> None:
    """Print formatted token."""
    text = pformat_token(token)
    print(text)


def pformat_token(
        token:
            Token
        ) -> str:
    """Return formatted token."""
    return _tw.dedent(f'''\
        Token(
            symbol={token.symbol!r},
            value={token.value!r},
            row={token.row},
            column={token.column},
            start={token.start})\
        ''')


class Lexer:
    """Parsing of regexes.

    Multiple named regexes are joined with `|`.
    """

    def __init__(
            self,
            token_to_regex:
                dict[str, str],
            token_to_lexeme:
                dict[str, str] |
                None=None,
            keywords:
                set[str] |
                None=None,
            omit_regex:
                str |
                None=None,
            diagnostics:
                bool=True
            ) -> None:
        r"""Compile regex.

        `token_to_regex` maps token names to
        regular expressions.

        `token_to_lexeme` maps token names to lexemes
        that may contain unescaped special characters of
        regular expressions, but are not regexes.

        Lexemes in `token_to_lexeme` are sorted in
        descending lexeme length.
        This way, for example `\=\=\=\=+` will come
        before `\=\=` in the sequence of regexes.

        Regular expressions of `token_to_regex`
        are placed before those of `token_to_lexeme`.

        `keywords` is subtracted from the regexes,
        by checking it after regular expressions have
        been matched.

        `omit_regex` matches characters to skip,
        for example blankspace `r' \s* '`.
        """
        if token_to_lexeme is None:
            token_to_lexeme = dict()
        tok_reg = _token_to_regex(
            token_to_regex,
            token_to_lexeme,
            diagnostics)
        pattern = _compile_regex(tok_reg)
        self._token_to_regex = tok_reg
        self._pattern = pattern
        if omit_regex is None:
            omit_pattern = None
        else:
            omit_pattern = re.compile(
                omit_regex,
                flags=re.VERBOSE)
        self._omit_pattern = omit_pattern
        if keywords is None:
            keywords = dict()
        else:
            keywords = {
                v: v
                for v in keywords}
        self._keywords = keywords
        self.token_names = {
            *tok_reg,
            *keywords}

    def parse(
            self,
            text:
                str,
            start:
                int |
                None=None,
            end:
                int |
                None=None
            ) -> _abc.Iterable[
                Token]:
        """Yield tokens from `text`."""
        tokens = _find_iter(
            text, start, end,
            self._pattern,
            self._omit_pattern)
        for token in tokens:
            symbol = self._keywords.get(
                token.value,
                token.symbol)
            if symbol == token.symbol:
                yield token
                continue
            yield Token(
                symbol=symbol,
                value=token.value,
                row=token.row,
                column=token.column,
                start=token.start)


class MethodsLexer(
        Lexer):
    r"""Lexer with methods.

    `t_*` attributes define regular expressions.
    The attribute name `t_token_name` defines the
    token `token_name`.
    Attributes that are methods have their
    docstrings as regular expressions.

    Regexes of methods are placed before regexes
    of attributes that are not methods.
    Method regexes are sorted by line number.
    Attributes are sorted by length of regex.

    `t_omit` defines a regex of what to skip,
    for example blankspace `t_omit = ' \s* '`.
    """

    def __init__(
            self):
        # lexing attributes and methods
        methods = list()
        attrs = list()
        items = dir(self)
        for name in items:
            if not name.startswith('t_'):
                continue
            attr = getattr(self, name)
            name_attr = (name[2:], attr)
            if isinstance(attr, str):
                attrs.append(name_attr)
            elif inspect.ismethod(attr):
                methods.append(name_attr)
            else:
                raise ValueError(name, attr)
        methods = sorted(
            methods,
            key=_method_line_number)
        # token mappings
        token_to_method = dict()
        token_to_regex = dict()
        for name, method in methods:
            docstring = method.__doc__
            if docstring is None:
                raise ValueError(name, method)
            if not name:
                raise ValueError(name)
            token_to_regex[name] = docstring
            token_to_method[name] = method
        self._token_to_method = token_to_method
        attrs = sorted(
            attrs,
            key=lambda x: x[1],
            reverse=True)
        for name, attr in attrs:
            if not isinstance(attr, str):
                raise ValueError(attr)
            if not name:
                raise ValueError(name)
            token_to_regex[name] = attr
        # omit-pattern
        if 'omit' in token_to_regex:
            omit_regex = token_to_regex['omit']
            token_to_regex.pop('omit')
        else:
            omit_regex = None
        super().__init__(
            token_to_regex=token_to_regex,
            omit_regex=omit_regex)

    def parse(
            self,
            text:
                str,
            start:
                int |
                None=None,
            end:
                int |
                None=None
            ) -> _abc.Iterable[
                Token]:
        """Yield tokens from `text`."""
        yield from _find_iter(
            text, start, end,
            self._pattern,
            self._omit_pattern,
            self._token_to_method)


class StatefulLexer:
    """Lexer with states.

    Similar to `MethodsLexer`. The names of `t_*`
    methods can include the name of a lexer state.
    For example `t_statename_*` are methods active
    in the state named `statename`.

    The names of the states are defined in
    the parameter `lexing_states`.
    The default state is named `'initial'`.

    Methods can change the lexer state by
    setting the attribute `self.lexing_state`.
    At the start of lexing, the state is
    `'initial'`.

    No token is returned for methods that
    return `None`.

    `self.input_text` is while parsing the
    input text (useful for methods that form
    tokens that are spans).
    """

    def __init__(
            self,
            lexing_states:
                set[str] |
                None=None
            ) -> None:
        # lexing states
        if lexing_states is None:
            lexing_states = set()
        if hasattr(self, 'lexing_states'):
            lexing_states = self.lexing_states
        if INITIAL_STATE not in lexing_states:
            lexing_states.add(INITIAL_STATE)
        # lexing attributes and methods
        state_to_methods = _cl.defaultdict(list)
        state_to_attrs = _cl.defaultdict(list)
        items = dir(self)
        for name in items:
            # lexing method ?
            if not name.startswith('t_'):
                continue
            # attribute
            attr = getattr(self, name)
            # which lexer state ?
            _, second, *_ = name.split('_')
            if second in lexing_states:
                state_name = second
                _, _, *rest = name.split('_')
                token_name = '_'.join(rest)
            else:
                state_name = INITIAL_STATE
                _, *rest = name.split('_')
                token_name = '_'.join(rest)
            name_attr = (token_name, attr)
            if isinstance(attr, str):
                mapping = state_to_attrs
            elif inspect.ismethod(attr):
                mapping = state_to_methods
            else:
                raise ValueError(name, attr)
            mapping[state_name].append(name_attr)
        # mappings
        self._token_to_method = dict()
        self._patterns = dict()
        self._omit_patterns = dict()
        for lexing_state in lexing_states:
            attrs = state_to_attrs[lexing_state]
            methods = state_to_methods[lexing_state]
            self._compile_state(
                lexing_state, attrs, methods)
        # lexing states
        self.lexing_states = lexing_states
        self.lexing_state = INITIAL_STATE

    def _compile_state(
            self,
            lexing_state,
            attrs:
                list,
            methods:
                list
            ) -> None:
        if not methods and not attrs:
            raise ValueError(
                'No lexing methods and attributes '
                f'for lexing state: `{lexing_state}`')
        methods = sorted(
            methods,
            key=_method_line_number)
            # NOTE: auto-generated lexing methods
            # have all the same line number.
        # token mappings
        token_to_method = dict()
        token_to_regex = dict()
        for name, method in methods:
            docstring = method.__doc__
            if docstring is None:
                raise ValueError(name, method)
            if not name:
                raise ValueError(name)
            token_to_regex[name] = docstring
            token_to_method[name] = method
        attrs = sorted(
            attrs,
            key=lambda x: x[1],
            reverse=True)
        for name, attr in attrs:
            if not isinstance(attr, str):
                raise ValueError(attr)
            if not name:
                raise ValueError(name)
            token_to_regex[name] = attr
        # omit-pattern
        if 'omit' in token_to_regex:
            omit_regex = token_to_regex['omit']
            token_to_regex.pop('omit')
            omit_pattern = re.compile(
                omit_regex,
                flags=re.VERBOSE)
        else:
            omit_pattern = None
        # compile patterns
        # tok_reg = _token_to_regex(
        #     token_to_regex, dict())
            # TODO: error checking
        pattern = _compile_regex(token_to_regex)
        # define lexing state
        self._patterns[
            lexing_state] = pattern
        self._omit_patterns[
            lexing_state] = omit_pattern
        self._token_to_method[
            lexing_state] = token_to_method

    def parse(
            self,
            text:
                str
            ) -> _abc.Iterable[
                Token]:
        """Yield tokens from `text`."""
        self.input_text = text
        self.lexing_state = 'initial'
        start = 0
        while start < len(text):
            omit_pattern = self._omit_patterns[
                self.lexing_state]
            if omit_pattern is not None:
                omit = omit_pattern.match(
                    text, start)
            else:
                omit = None
            if omit is not None:
                start = omit.end()
            if start >= len(text):
                break
            pattern = self._patterns[
                self.lexing_state]
            occ = pattern.match(
                text, start)
            # unrecognized text ?
            if occ is None:
                span = text[start:]
                raise ValueError(
                    'Unrecognized characters '
                    f'at: {span!r}\n'
                    f'{self.lexing_state = }')
            # unconsumed text ?
            occ_start, occ_end = occ.span()
            if occ_start == occ_end:
                raise ValueError(occ)
            # make token
            symbol = occ.lastgroup
            span = occ.group()
            token = Token(
                symbol=symbol,
                value=span,
                start=start)
            token_to_method = self._token_to_method[
                self.lexing_state]
            if symbol in token_to_method:
                method = token_to_method[symbol]
                token = method(token)
            start = occ_end
            if token is not None:
                yield token


def _method_line_number(
        x:
            tuple
        ) -> int:
    """Return start line of method."""
    _, attr = x
    _, start_line = inspect.getsourcelines(
        attr)
    return start_line


def _token_to_regex(
        token_to_regex:
            dict[str, str],
        token_to_lexeme:
            dict[str, str],
        diagnostics:
            bool=True
        ) -> dict[str, str]:
    r"""Return token to regex mapping.

    Sorts `token_to_lexemes` by lexeme length.

    Read `Lexer.__init__()`.
    """
    tok_reg = dict(token_to_regex)
    token_to_lexeme = dict(token_to_lexeme)
    _assert_nonempty_kv(token_to_lexeme)
    _check_regex_overlap(
        tok_reg, token_to_lexeme,
        diagnostics)
    # sort by lexeme
    lexemes = _sort_lexemes(
        token_to_lexeme.values())
    lexeme_to_token = {
        v: k
        for k, v in token_to_lexeme.items()}
    tok_reg.update(
        (lexeme_to_token[lexeme],
            re.escape(lexeme))
        for lexeme in lexemes)
    _assert_token_names(tok_reg)
    m = len(token_to_regex)
    n = len(token_to_lexeme)
    k = len(tok_reg)
    sum_len = (m + n == k)
    if not sum_len:
        raise AssertionError(
            m, n, k)
    return tok_reg


def _compile_regex(
        token_to_regex:
            dict[str, str]
        ) -> re.Pattern:
    """Return one regex with named cases."""
    if not token_to_regex:
        raise ValueError(token_to_regex)
    pairs = token_to_regex.items()
    regexes = list()
    for token, regex in pairs:
        named_regex = rf' (?P<{token}> {regex} )'
        regexes.append(named_regex)
    regex = '\n|'.join(regexes)
    _log.info(regex)
    return re.compile(
        regex,
        flags=re.VERBOSE)


def _assert_token_names(
        tokens
        ) -> None:
    """Assert no blankspace in token names."""
    regex = r'''
          \x20
        | \n
        | \t
        | \r
        '''
    pattern = re.compile(
        regex,
        flags=re.VERBOSE)
    for token in tokens:
        if pattern.search(token) is None:
            continue
        raise ValueError(
            'Token name contains blankspace: '
            f'{token = }')


def _assert_nonempty_kv(
        kv:
            dict
        ) -> None:
    """Assert no empty keys nor values."""
    for key, value in kv.items():
        if key and value:
            continue
        raise ValueError(
            'Empty key or value: '
            f'{key = }, {value = }')


def _check_regex_overlap(
        token_to_regex:
            dict[str, str],
        token_to_lexeme:
            dict[str, str],
        diagnostics:
            bool
        ) -> None:
    """Assert no pattern overlaps."""
    if not diagnostics:
        return
    _check_regex_lexeme_overlap(
        token_to_regex,
        token_to_lexeme)
    _check_lexeme_lexeme_overlap(
        token_to_lexeme)


def check_regex_regex_overlap(
        token_to_regex:
            dict[str, str]
        ) -> None:
    """Assert regexes pairwise disjoint."""
    _assert_bijection(token_to_regex)
    regexes = set(
        token_to_regex.values())
    while regexes:
        regex = regexes.pop()
        for other in regexes:
            _assert_no_regex_overlap(
                regex, other)


def _assert_no_regex_overlap(
        regex:
            str,
        other:
            str
        ) -> None:
    """Assert regexes do not overlap."""
    if regex == other:
        raise AssertionError(regex)
    nfa_1 = _re.regex_to_nfa(regex)
    nfa_2 = _re.regex_to_nfa(other)
    nfa = _re.nfa_intersection(
        nfa_1, nfa_2)
    is_empty = _re.is_empty_nfa(nfa)
    if is_empty:
        return
    raise ValueError(_tw.dedent(f'''
        regular expressions overlap:
            `{regex}`
            `{other}`
        '''))


def _check_regex_lexeme_overlap(
        token_to_regex:
            dict[str, str],
        token_to_lexeme:
            dict[str, str]
        ) -> None:
    """Assert regexes and lexemes do not overlap."""
    items = token_to_regex.items()
    for token_name, regex in items:
        pattern = re.compile(
            regex,
            flags=re.VERBOSE)
        kv = token_to_lexeme.items()
        for tok, lexeme in kv:
            occ = pattern.match(lexeme)
            if occ is None:
                continue
            raise ValueError(_tw.dedent(f'''
                token:
                    `{token_name}`
                has regex:
                    `{regex}`
                which overlaps with the lexeme:
                    `{lexeme}`
                of the token:
                    `{tok}`
                '''))


def _check_lexeme_lexeme_overlap(
        token_to_lexeme:
            dict[str, str]
        ) -> None:
    """Warn if lexemes overlap."""
    _assert_bijection(
        token_to_lexeme)
    lexeme_to_token = {
        v: k
        for k, v in
            token_to_lexeme.items()}
    # group
    first_char_map = _cl.defaultdict(set)
    lexemes = token_to_lexeme.values()
    for lexeme in lexemes:
        char = lexeme[0]
        first_char_map[char].add(lexeme)
    for lexemes in first_char_map.values():
        _warn_lexemes_overlap(
            lexemes, lexeme_to_token)


def _warn_lexemes_overlap(
        lexemes:
            set[str],
        lexeme_to_token:
            dict[str, str]
        ) -> None:
    """Warn if pairwise overlap."""
    for lexeme in lexemes:
        for other_lexeme in lexemes:
            if lexeme == other_lexeme:
                # `lexeme_to_token` is
                # a bijection
                continue
            is_prefix = other_lexeme.startswith(
                lexeme)
            if not is_prefix:
                continue
            token = lexeme_to_token[lexeme]
            other_token = lexeme_to_token[
                other_lexeme]
            print(_tw.dedent(f'''
                WARNING:
                token:
                    `{token}`
                has lexeme:
                    `{lexeme}`
                which overlaps with the lexeme:
                    `{other_lexeme}`
                of the token
                    `{other_token}`
                '''))


def _assert_bijection(
        token_to_lexeme:
            dict[str, str]
        ) -> None:
    """Assert `token_to_lexeme` is a bijection."""
    lexeme_to_token = {
        v: k
        for k, v in
            token_to_lexeme.items()}
    kv_n = len(token_to_lexeme)
    vk_n = len(lexeme_to_token)
    if kv_n == vk_n:
        return
    lexeme_to_token = dict()
    items = token_to_lexeme.items()
    for token, lexeme in items:
        if lexeme not in lexeme_to_token:
            lexeme_to_token[lexeme] = token
            continue
        assert lexeme in lexeme_to_token
        prev_token = lexeme_to_token[lexeme]
        raise ValueError(_tw.dedent(f'''
            tokens:
                `{token}`
            and:
                `{prev_token}`
            have the same pattern:
                `{lexeme}`
            '''))


def _sort_lexemes(
        lexemes:
            _abc.Iterable[
                str]
        ) -> list[
            str]:
    """Sort in descending length."""
    return sorted(
        lexemes,
        key=len,
        reverse=True)


def _find_iter(
        text:
            str,
        start:
            int |
            None,
        end:
            int |
            None,
        pattern:
            re.Pattern,
        omit_pattern:
            bool |
            None,
        token_to_method:
            dict |
            None=None
        ) -> _abc.Iterable[
            Token]:
    """Return tokens with start index."""
    omit = None
    if start is None:
        start = 0
    if end is None:
        end = len(text)
    while start < end:
        if omit_pattern is not None:
            omit = omit_pattern.match(
                text, start, end)
        if omit is not None:
            start = omit.end()
        if start >= end:
            break
        occ = pattern.match(
            text, start, end)
        # unrecognized text ?
        if occ is None:
            span = text[start:]
            raise ValueError(
                'Unrecognized characters '
                f'at: {span!r}')
        # unconsumed text ?
        occ_start, occ_end = occ.span()
        if occ_start == occ_end:
            raise ValueError(occ)
        # make token
        symbol = occ.lastgroup
        span = occ.group()
        token = Token(
            symbol=symbol,
            value=span,
            start=start)
        has_method = (
            token_to_method and
            symbol in token_to_method)
        if has_method:
            method = token_to_method[symbol]
            token = method(token)
        if token is not None:
            yield token
        start = occ_end


def lex_delimited(
        text:
            str,
        delimiter_regex:
            str,
        delimiter_pairs:
            dict[str, str],
        delimiter_tokens:
            dict[str, str],
        nestable_delimiters:
            set[str],
        lexer:
            Lexer
        ) -> list[
            Token]:
    r"""Lex between delimited spans.

    Spans do not overlap.
    Spans of `nestable_delimiters` can be nested.
    Each delimited span becomes a token.

    `lexer` is used to tokenize characters between
    delimited spans.

    `delimiter_regex` is a regular expression
    that matches opening and closing delimiters

    Escape sequences need using `StatefulLexer`,
    i.e., string syntax requires defining a lexer
    with states, if `\\` and other such sequences
    have meaning when inside the string.

    `delimiter_pairs` maps opening delimiters
    to closing delimiters (lexemes), e.g.,
    `'(*'` to `'*)'`.

    `delimiter_tokens` maps opening delimiters
    to token names, e.g., `'(*'` to
    `'MULTILINE_COMMENT'`.

    `nestable_delimiters` contains opening delimiters
    that can be nested, and need be balanced,
    for example `(*  (*  *)  *)`.
    """
    _assert_lex_delimited_input(
        delimiter_pairs, delimiter_tokens,
        nestable_delimiters)
    tokens = list()
    delimiter_pattern = re.compile(
        delimiter_regex,
        flags=re.VERBOSE)
    state = 'init'
    opening_delimiter = None
    nesting_depth = 0
    start = 0
    delimiter_start = 0
    while start < len(text):
        assert nesting_depth >= 0, nesting_depth
        delimiter = delimiter_pattern.search(
            text, delimiter_start)
        if delimiter is None:
            # span = text[start:]
            # _lex_span(span, start, tokens, lexer)
            _lex_span(
                text, start, len(text),
                tokens, lexer)
            start = len(text)
            break
        assert delimiter is not None
        start_, end = delimiter.span()
        delimiter_start = end
        delimiter_str = delimiter.group()
        if state == 'init':
            if delimiter_str not in delimiter_pairs:
                continue
            # span = text[start:start_]
            # _lex_span(span, start, tokens, lexer)
            _lex_span(
                text, start, start_,
                tokens, lexer)
            start = start_
            state = 'delimited'
            opening_delimiter = delimiter_str
            nesting_depth = 1
        elif state == 'delimited':
            if delimiter is None:
                raise ValueError(
                    'unmatched opening delimiter: '
                    f'{opening_delimiter}')
            closing_delimiter = delimiter_pairs.get(
                opening_delimiter)
            if delimiter_str == closing_delimiter:
                nesting_depth -= 1
            elif (delimiter_str == opening_delimiter and
                    delimiter_str in nestable_delimiters):
                nesting_depth += 1
            if nesting_depth > 0:
                continue
            symbol = delimiter_tokens[
                opening_delimiter]
            span = text[start:delimiter_start]
            token = Token(
                symbol=symbol,
                value=span,
                start=start)
            tokens.append(token)
            start = delimiter_start
            state = 'init'
        else:
            raise AssertionError(
                state)
    _assert_lex_delimited_loop_end(
        text, opening_delimiter,
        start, nesting_depth)
    return add_row_column(
        text, tokens)


def add_row_column(
        text:
            str,
        tokens:
            list[
                Token]
        ) -> list[
            Token]:
    """Add row-column information.

    Sets `token.row` and `token.column`
    based on `token.start` and occurrences of
    newlines in `text`. Returns new tokens.
    """
    newlines = re.finditer(
        '\n', text)
    newline_ends = [0, *(
        nw.start() + 1
        for nw in newlines)]
    index = 0
    tokens_pos = list()
    for token in tokens:
        start = token.start
        while True:
            next_index = index + 1
            brk = (
                next_index == len(newline_ends) or
                newline_ends[next_index] > start)
            if brk:
                break
            index += 1
        newline_end = newline_ends[index]
        row = index
        column = token.start - newline_end
        token_pos = Token(
            symbol=token.symbol,
            value=token.value,
            row=row,
            column=column,
            start=token.start)
        tokens_pos.append(token_pos)
    return tokens_pos


def _assert_lex_delimited_input(
        delimiter_pairs:
            dict[str, str],
        delimiter_tokens:
            dict[str, str],
        nestable_delimiters:
            set[str]
        ) -> None:
    """Assert precondition."""
    if None in delimiter_pairs:
        raise ValueError(
            delimiter_pairs)
    if None in delimiter_tokens:
        raise ValueError(
            delimiter_tokens)
    if set(delimiter_pairs) != set(
            delimiter_tokens):
        raise ValueError(
            delimiter_pairs,
            delimiter_tokens)
    for delimiter in nestable_delimiters:
        closing_delimiter = delimiter_pairs.get(
            delimiter)
        if closing_delimiter is None:
            raise ValueError(
                delimiter, delimiter_pairs)
        if delimiter == closing_delimiter:
            raise ValueError(
                'same opening and closing delimiter, '
                f'cannot be nested: {delimiter}')


def _assert_lex_delimited_loop_end(
        text:
            str,
        opening_delimiter:
            str |
            None,
        start:
            int,
        nesting_counter:
            int
        ) -> None:
    """Assert expected values after `for`."""
    if nesting_counter != 0:
        raise AssertionError(
            nesting_counter)
    if start != len(text):
        raise AssertionError(
            start, len(text))


def _lex_span(
        text:
            str,
        start:
            int,
        end:
            int,
        tokens:
            list,
        lexer:
            Lexer
        ) -> None:
    """Lex tokens in `span`."""
    tokens.extend(lexer.parse(
        text, start, end))


def join_tokens(
        tokens:
            list
        ) -> str:
    """Return text from `tokens`.

    `row` and `column` attribute are
    used to join the tokens.
    """
    spans = list()
    last_token = make_none_token()
    for token in tokens:
        # insert blankspace between tokens
        last_row = last_token.row
        # new line ?
        if last_row < token.row:
            l_rows = last_token.value.count('\n')
            n_rows = (
                token.row
                - last_row
                - l_rows)
            newlines = n_rows * '\n'
            spaces = token.column * '\x20'
            spans.extend((
                newlines,
                spaces))
        elif last_row > token.row:
            raise AssertionError(
                last_row, token.row)
        else:
            # same line
            n_spaces = (
                token.column
                - len(last_token.value)
                - last_token.column)
            spaces = n_spaces * '\x20'
            spans.append(spaces)
        # add non-blankspace
        spans.append(token.value)
        last_token = token
    return ''.join(spans)


def make_none_token(
        ) -> Token:
    """Return token at start."""
    return Token(
        symbol=None,
        value='',
        start=0,
        row=0,
        column=0)
