"""Shift-reduce parser, bi-stack.


References
==========

* Kuo-Chung Tai
  "Noncanonical SLR(1) grammars"
  ACM Transactions on Programming Languages and Systems
  Volume 1, Issue 2, pages 295--320, 1979
  <https://doi.org/10.1145/357073.357083>

* Daniel J. Salomon and Gordon V. Cormack
  "Scannerless NSLR(1) parsing of programming languages"
  ACM SIGPLAN Conference on Programming Language
    Design and Implementation
  pages 170--178, 1989
  <https://doi.org/10.1145/73141.74833>
"""
import collections.abc as _abc
import collections as _cl
import functools as _ft
import itertools as _itr
import json
import logging
import os
import pprint as _pp
import subprocess as _sbp
import textwrap as _tw
import typing as _ty

import parstools._grammars as _grm
import parstools._lr.utils as _lu
import parstools._utils as _u


SPACE: _ty.Final = '\x20'
INDENT_WIDTH: _ty.Final = 4
INDENT: _ty.Final = INDENT_WIDTH * SPACE
_ROOT: _ty.Final = _grm.ROOT
_END: _ty.Final = _grm.END
_Dot: _ty.TypeAlias = _lu.Dot
_Prints: _ty.TypeAlias = None
maybe_int: _ty.TypeAlias = int | None
_State: _ty.TypeAlias = set[
    _Dot]
_StateSeq: _ty.TypeAlias = list[
    _State]
_StateSymbol: _ty.TypeAlias = tuple[
    _State,
    symbol := str]
_Actions: _ty.TypeAlias = dict[
    _StateSymbol,
    _lu.Action]
_TreeMap: _ty.TypeAlias = dict[
    str, _abc.Callable]
_Item = _ty.TypeVar('_Item')


_log = logging.getLogger(__name__)


class _Stack(
        _cl.UserList):
    """List that only overwrites.

    `pop()` changes the end-index,
    without spending time popping elements.
    """

    end: int
        # `end \in Nat \cup {-1}`

    def __init__(
            self,
            items:
                _abc.Iterable |
                None=None
            ) -> None:
        if items is None:
            self.data = list()
            super().__init__()
        else:
            super().__init__(items)
        self.end = len(self.data)
        self._assert_invariant()

    def __len__(
            self):
        return self.end

    def append(
            self,
            value:
                _ty.Any
            ) -> None:
        self._assert_invariant()
        self.end += 1
        if self.end > len(self.data):
            self.data.append(value)
        else:
            self.data[self.end - 1] = value
        self._assert_invariant()

    def extend(
            self,
            values:
                _abc.Collection
            ) -> None:
        raise NotImplementedError

    def popk(
            self,
            n_items:
                int
            ) -> None:
        self._assert_invariant()
        end = self.end
        self.end -= n_items
        self._assert_invariant()
        return self.data[self.end:end]

    def __getitem__(
            self,
            index:
                int |
                slice):
        match index:
            case int():
                if index < 0:
                    index = self.end + index
                return self.data[index]
            case _:
                raise NotImplementedError

    def _assert_invariant(
            self
            ) -> None:
        """Assert `self.end` is within bounds.

        This is the invariant that
        holds of the index `self.end`.
        """
        expected = (
            0 <= self.end <= len(self.data))
        if expected:
            return
        raise AssertionError(
            self.end,
            len(self.data),
            self.data)


class CachedIterable(
        _ty.Generic[_Item]):
    """The cache is appendable.

    This enables inserting items to
    the sequence, during iteration.
    """

    def __init__(
            self,
            iterable:
                _abc.Iterable[
                    _Item]
            ) -> None:
        self._iterable = iter(iterable)
        self._more = list()

    def peek(
            self
            ) -> _Item | None:
        """Which the next item is."""
        if self._more:
            return self._more[-1]
        try:
            item = next(self._iterable)
        except StopIteration:
            return None
        assert not self._more
            # at most one item from
            # `self._iterable` is in
            # `self._more` at a time
        self._more.append(item)
        return item

    def pop(
            self
            ) -> _Item:
        """Remove and return next item."""
        if self._more:
            return self._more.pop()
        return next(self._iterable)

    def append(
            self,
            item:
                _Item
            ) -> None:
        """Append item to cache.

        The cache is a stack.
        """
        self._more.append(item)


class Tree(
        _ty.Protocol):
    """Token interface of parser."""

    symbol: str
    value: _ty.Any


class Result(
        _ty.NamedTuple):
    """Parsing result, including tokens.

    The attribute `equation` is
    the grammar equation that produced
    this result during parsing.

    So the attribute `equation` defines
    the derivation constructed by the
    parser.

    The attribute `equation` is useful for
    quotienting the derivation into
    a syntax tree.
    """

    symbol: str
    value: (
        tuple |
        None) = None
    equation: (
        str |
        None) = None
    row: maybe_int = None
    column: maybe_int = None
        # start column


_Results: _ty.TypeAlias = list[
    Result]


class ParserOptimized:
    """Shift-reduce parser."""

    def __init__(
            self,
            initial:
                _State,
            actions:
                _Actions,
            tree_map:
                _TreeMap |
                None=None
            ) -> None:
        """Initialize.

        `tree_map` maps grammar formulas to
        methods that reduce trees.
        """
        self._initial: _State = initial
        self._actions: _Actions = actions
        if tree_map is None:
            self._tree_map = None
            return
        action_to_tree_map = dict()
        for action in actions.values():
            if action.equation is None:
                continue
            eq = str(action.equation)
            method = tree_map[eq]
            action_to_tree_map[action] = method
        self._tree_map = action_to_tree_map

    def nodes(
            parser
            ) -> set[
                _State]:
        """Return nodes of LR machine."""
        return {
            node
            for node, _ in
                parser._actions}

    def parse(
            self,
            items:
                _abc.Iterable[
                    Tree]
            ) -> (
                Result |
                None):
        """Reduce items to a tree."""
        sequence = list(items)
        end = Result(symbol=_END)
        symbols = [end]
        symbols.extend(reversed(sequence))
            # input stack
        results = list()
            # output stack
        path = [self._initial]
        while symbols and path:
            lookahead = symbols[-1].symbol
            action = self._actions.get(
                (path[-1], lookahead))
            if (action is not None and
                    action.state is not None):
                path.append(action.state)
                treelet = symbols.pop()
                results.append(treelet)
            elif (action is not None and
                    action.equation is not None):
                symbol, expansion = action.equation
                n_items = len(expansion)
                trees = results[-n_items:]
                del results[-n_items:]
                del path[-n_items:]
                if self._tree_map is not None:
                    reduce = self._tree_map[action]
                    p = [None, *(
                        u.value
                        for u in trees)]
                    reduce(p)
                    trees = p[0]
                result = Result(
                    symbol=symbol,
                    value=trees)
                symbols.append(result)
            elif action is None:
                if lookahead == _ROOT:
                    results.append(symbols.pop())
                    treelet = symbols.pop()
                    if treelet.symbol != _END:
                        raise AssertionError(_END)
                    path.pop()
                    continue
                else:
                    path.clear()
                    continue
            else:
                raise AssertionError(
                    node, lookahead, action)
        if symbols or path:
            return None
        if len(results) != 1:
            raise AssertionError(results)
        return results[0]


class Parser:
    """Shift-reduce parser.

    Reduces using methods that access
    production items by their numeric
    index.

    Uses two stacks.
    """

    def __init__(
            self,
            initial:
                _State,
            actions:
                _Actions,
            tree_map:
                _TreeMap |
                None=None
            ) -> None:
        """Initialize.

        `tree_map` maps grammar formulas to
        methods that reduce trees.
        """
        self._initial: _State = initial
        self._actions: _Actions = actions
        self._tree_map: _TreeMap | None = tree_map

    def nodes(
            parser
            ) -> set[
                _State]:
        """Return nodes of LR machine."""
        return {
            node
            for node, _ in
                parser._actions}

    def parse(
            self,
            items:
                _abc.Iterable[
                    Tree]
            ) -> (
                Result |
                None):
        """Reduce items to a tree."""
        sequence = list(items)
        end = Result(symbol=_END)
        symbols = [end]
        symbols.extend(reversed(sequence))
            # input stack
        results = list()
            # output stack
        path = [self._initial]
        pop = _ft.partial(
            self._shift_or_reduce,
            symbols=symbols,
            results=results,
            path=path)
        while symbols and path:
            pop()
        if symbols or path:
            return None
        if len(results) != 1:
            raise AssertionError(results)
        return results[0]

    def _shift_or_reduce(
            self,
            symbols,
            results,
            path
            ) -> None:
        """Step of shift-reduce parser."""
        if not path:
            raise AssertionError(path)
        if not symbols:
            raise AssertionError(symbols)
        lookahead = symbols[-1].symbol
        if lookahead == _ROOT:
            results.append(symbols.pop())
            treelet = symbols.pop()
            if treelet.symbol != _END:
                raise AssertionError(_END)
            path.pop()
            return
        node = path[-1]
        key = (node, lookahead)
        action = self._actions.get(key)
        if action is None:
            path.clear()
            return
        if action.equation is not None:
            eq = action.equation
            symbol, expansion = eq
            n_items = len(expansion)
            popk(path, n_items)
            equation = str(eq)
            trees = popk(results, n_items)
            if self._tree_map is not None:
                reduce = self._tree_map[equation]
                p = [None, *(
                    u.value
                    for u in trees)]
                reduce(p)
                trees = p[0]
            result = Result(
                symbol=symbol,
                value=trees,
                equation=equation)
            symbols.append(result)
        elif action.state is not None:
            path.append(action.state)
            treelet = symbols.pop()
            results.append(treelet)
        else:
            raise AssertionError(
                node, lookahead, action)


def check_parser_cache(
        grammar:
            _grm.Grammar,
        cache_filename:
            str |
            None=None
        ) -> (
            Parser |
            None):
    """Load parser, if cached."""
    cache_exists = (
        cache_filename is not None and
        os.path.isfile(cache_filename))
    if not cache_exists:
        print('not using parser cache')
        return None
    grammar_str = _grammar_as_str(grammar)
    with open(cache_filename, 'r') as fd:
        data = json.load(fd)
    grammar_str_ = data.get('grammar_str')
    if grammar_str_ is None:
        raise ValueError(
            'Given file contains no '
            'key `grammar_str`.')
    if grammar_str != grammar_str_:
        print(
            'parser grammar has changed, '
            'compared to cache in file: '
            f'`{cache_filename}`')
        return None
    assert grammar_str == grammar_str_, (
        grammar_str, grammar_str_)
    print(
        'loading parser from '
        f'cache file: `{cache_filename}`')
    initial = data['initial']
    actions = data['actions']
    symbol_indexing = data['symbol_indexing']
    int_to_eq = data['int_to_eq']
    return _parser_from_int_nodes(
        initial, actions,
        symbol_indexing, int_to_eq)


def dump_parser_cache(
        grammar:
            _grm.Grammar,
        parser:
            Parser,
        cache_filename:
            str |
            None=None
        ) -> None:
    """Write parser to file."""
    if cache_filename is None:
        return
    grammar_str = _grammar_as_str(grammar)
    (initial, actions,
     symbol_indexing, int_to_eq
        ) = _nodes_to_int(parser)
    data = dict(
        grammar_str=grammar_str,
        initial=initial,
        actions=actions,
        symbol_indexing=symbol_indexing,
        int_to_eq=int_to_eq)
    if os.path.isfile(cache_filename):
        print(
            'overwriting cache file for '
            f'parser: `{cache_filename}` ')
    with open(cache_filename, 'w') as fd:
        json.dump(data, fd)


def _grammar_as_str(
        grammar:
            _grm.Grammar
        ) -> str:
    """Return sorted grammar formulas."""
    eqs = sorted(
        str(eq)
        for eq in grammar.equations)
    root_symbol = grammar.root_symbol
    return f'{root_symbol = }, {eqs = }'


class DebugParser:
    """Shift-reduce parser with

    printing of parsing as it evolves.
    """

    def __init__(
            self,
            initial:
                _State,
            actions:
                _Actions,
            tree_map:
                _TreeMap |
                None=None
            ) -> None:
        self._initial: _State = initial
        self._actions: _Actions = actions
        self._tree_map: _TreeMap | None = tree_map

    @classmethod
    def from_parser(
            cls,
            parser
            ) -> 'DebugParser':
        return cls(
            initial=parser._initial,
            actions=parser._actions,
            tree_map=parser._tree_map)

    def __str__(
            self
            ) -> str:
        states = {
            state
            for state, _ in self._actions}
        n_states = len(states)
        n_edges = len(self._actions)
        return (
            'LR parser, with:\n'
            f'    {n_states} states\n'
            f'    {n_edges} edges')

    def nodes(
            parser
            ) -> set[
                _State]:
        """Return nodes of LR machine.

        The edges are `self._actions`.
        """
        return {
            node
            for node, _ in
                parser._actions}

    def parse(
            self,
            sequence:
                _abc.Sequence[
                    Result],
            debug:
                bool=False
            ) -> (
                Result |
                None):
        """Map `sequence` to a tree.

        `sequence` contains items with
        attributes `symbol` and `value`
        (both `str`).
        """
        return _parse_debug(
            sequence,
            self._initial,
            self._actions,
            self._tree_map)


def _parse_debug(
        sequence:
            _abc.Sequence[
                Result],
        initial_state:
            _State,
        actions:
            _Actions,
        tree_map:
            _TreeMap
        ) -> (
            Result |
            None):
    """Shift-reduce recognizer."""
    sequence = list(sequence)
        # cache for printing later below
    end = Result(symbol=_END)
    symbols = [end]
    symbols.extend(reversed(sequence))
        # stack of grammar symbols
        # (Reversed because
        #  appending to lists is
        #  more efficient than
        #  prepending to lists.
        #  A deque could be used
        #  instead.)
    path = [initial_state]
        # stack of LR(1) states
    results = list()
        # accumulator of output
    done = list()
    rest = list(
        reversed(sequence))
    pop = _ft.partial(
        _shift_or_reduce_debug,
        symbols=symbols,
        path=path,
        results=results,
        actions=actions,
        tree_map=tree_map,
        done=done,
        rest=rest)
    while symbols and path:
        print('')
        print(
            f'{symbols = }\n'
            f'{len(path) = }\n'
            f'{results = }')
        pop()
            # pop either:
            # - the symbol stack
            #   (also known as a "shift",
            #    because the popped symbol
            #    is appended to the results
            # - the state stack
            #   (also known as "reduce",
            #    because the pop generates
            #    a nonleaf symbol that
            #    is appended to the
            #    symbol stack)
        # terminates if either:
        # - not symbols: meaning that
        #   all input has been consumed
        # - not path: meaning that
        #   we reduced to the root symbol
    # unconsumed input or
    # not reduced to root symbol ?
    if symbols or path:
        # nonempty `symbols` implies
        # unconsumed input tokens
        #
        # nonempty `path` implies
        # that the reduction did not
        # produce a derivation from
        # the root symbol (whose name
        # is stored in the module
        # constant `_ROOT`)
        print(
            'Pattern did not match sequence. '
            'Current state:\n'
            # f'    {symbols = }\n'
            f'    {len(path) = }\n'
            f'    {results = }')
        # NOTE: instead of raising an exception,
        # we return `None`, similarly to
        # CPython's module `re`.
        return None
    if len(results) != 1:
        raise AssertionError(results)
    return results[0]


def _shift_or_reduce_debug(
        symbols:
            _Results,
        path:
            _StateSeq,
        results:
            _Results,
        actions:
            _Actions,
        tree_map:
            _TreeMap,
        done:
            _Results,
        rest:
            _Results
        ) -> None:
    """Step of LR(1) parser."""
    _print_prefix_parsed(done, rest)
    if not path:
        raise AssertionError(
            path)
    if not symbols:
        raise AssertionError(
            symbols)
    state = path[-1]
    lookahead = symbols[-1].symbol
    if lookahead == _ROOT:
        results.append(symbols.pop())
        treelet = symbols.pop()
        if treelet.symbol != _END:
            raise AssertionError(_END)
        path.pop()
            # pop the initial state
        return
    # for key, todo in actions.items():
    #     print('state:')
    #     print(key)
    #     print(todo)
    #     print('---------------')
    key = (
        state,
        lookahead)
    if key not in actions:
        # impossible to match sequence
        print(path)
        path.clear()
        return
    action = actions[key]
    if action.equation is not None:
        _log.info(_tw.dedent(f'''
            reduce using equation:
            {INDENT}{action.equation}
            '''))
        symbol, expansion = action.equation
        n_items = len(expansion)
        print(f'will pop {n_items} items')
        popk(path, n_items)
            # retract
        equation = str(action.equation)
        # construct syntax tree
        trees = popk(results, n_items)
        if tree_map is not None:
            reduce = tree_map[equation]
            p = [None, *(
                u.value
                for u in trees)]
            reduce(trees)
            trees = p[0]
        result = Result(
            symbol=symbol,
            value=trees,
            equation=equation)
        symbols.append(result)
    elif action.state is not None:
        _log.info(
            'goto state: '
            f'{action.state}')
        path.append(action.state)
        treelet = symbols.pop()
        print(
            'popped input treelet:\n'
            f'{INDENT}{treelet.symbol!r}')
        results.append(treelet)
        is_input_symbol = (
            rest and
            treelet.value == rest[-1].value)
        if is_input_symbol:
            done.append(rest.pop())
    else:
        raise AssertionError(
            state, lookahead, action)


def popk(
        items:
            list[
                _Item],
        n_items:
            int
        ) -> list[
            _Item]:
    """Pop and return last `n_items`."""
    if n_items < 0:
        raise AssertionError(
            f'Cannot pop {n_items} items.')
    if n_items > len(items):
        raise AssertionError(
            'Cannot pop more items than '
            'the contents of the list:\n'
            f'    {len(items) = }\n'
            f'    {n_items = }')
    popped = items[-n_items:]
    del items[-n_items:]
    return popped


def _print_prefix_parsed(
        done,
        rest
        ) -> _Prints:
    def join(results):
        return ' '.join(
            symbol.value
            for symbol in results)
    prefix = INDENT + join(done)
    suffix = join(reversed(rest))
    prefix_2 = SPACE * len(prefix)
    here = 3 * SPACE
    n_arrows = len(here)
    hands = '\u261D' * n_arrows
    assert len(here) == len(hands), (
        here, hands)
    arrows = '^' * n_arrows
    assert len(here) == len(arrows), (
        here, arrows)
    LINE_WIDTH = 40
    LINE = LINE_WIDTH * '\u2500'
    print(_tw.dedent(f'''
        {LINE}
        where we are in the input:

        {prefix} {here} {suffix}
        {prefix_2} {hands}
        {LINE}'''))


def print_parser(
        parser:
            Parser,
        grammar:
            _grm.Grammar
        ) -> _Prints:
    """Print the tables of LR `parser`."""
    WIDTH = 40
    DASH_LINE = '-' * WIDTH
    print(DASH_LINE)
    print('LR state machine:')
    grammar = _lu.add_root_equation(grammar)
    grammar_symbols = {
        _grm.END,
        *grammar.symbols}
    equations = {
        str(eq):
            f'eq-{str(index)}'
        for index, eq in
            enumerate(grammar.equations)}
    states = lr_parser_states(parser._actions)
    states = {
        state:
            f'st-{str(index)}'
        for index, state in
            enumerate(states)}
    table = _cl.defaultdict(dict)
    for key, action in parser._actions.items():
        if action.state is not None:
            todo = states[action.state]
        elif action.equation is not None:
            eq = str(action.equation)
            todo = equations[eq]
        else:
            raise AssertionError(action)
        state, symbol = key
        assert (
            symbol in grammar_symbols or
            symbol == ''), (symbol, key)
        src_hash = states[state]
        table[src_hash][symbol] = todo
    for state, state_hash in states.items():
        if state_hash not in table:
            raise AssertionError(
                state_hash, table)
        state_actions = table[state_hash]
        for symbol in grammar_symbols:
            if symbol in state_actions:
                continue
            assert symbol not in state_actions
            state_actions[symbol] = '\u2027'
    width = _max_symbol_width(
        grammar_symbols, table)
    n_columns = 1 + len(grammar_symbols)
    HLINE = n_columns * width * _u.HLINE_PIECE
    SEP = '\u2502  '
    print(HLINE)
    for eq, index in equations.items():
        print(f'{index}: {eq}')
    print(HLINE)
    print(''.ljust(width), end=SEP)
    symbols = sorted(grammar_symbols)
    for symbol in symbols:
        name = _grm.format_empty_symbol(symbol)
        show = name.ljust(width)
        print(show, end='')
    print('')
    state_names = sorted(states.values())
    for src_hash in state_names:
        row = table[src_hash]
        print(src_hash.ljust(width), end=SEP)
        for symbol in symbols:
            todo = row.get(symbol, '')
            show = todo.ljust(width)
            print(show, end='')
        print()
    print(HLINE)
    DOUBLED_LINE = '=' * WIDTH
    print(DOUBLED_LINE)


def lr_parser_states(
        actions:
            dict
        ) -> set:
    """Return states of shift-reduce parser."""
    return {
        node
        for node, _ in
            actions}


def _max_symbol_width(
        symbols:
            set[
                str],
        table:
            dict[
                str,
                dict]
        ) -> int:
    """Return length of widest symbol."""
    symbols = {
        _grm.format_empty_symbol(symbol)
        for symbol in symbols}
    strings = _itr.chain(
        table.keys(),
        *(u.values() for u in table.values()),
        symbols)
    # width
    return 2 + max(map(len, strings))


def dump_parser_pdf(
        parser:
            Parser
        ) -> _Prints:
    """Write LR state-machine as PDF file."""
    actions = parser._actions
    nodes = {
        node
        for node, _ in actions}
    node_labels = dict()
    edges = _cl.defaultdict(set)
    node_indices = dict()
    def make_index(node):
        return node_indices.setdefault(
            node, len(node_indices))
    for (node, symbol), action in actions.items():
        node_index = make_index(node)
        node_labels[node_index] = _lu.pformat_state(
            node, boxed=False)
        if action.state is None:
            continue
        next_node_index = make_index(action.state)
        edges[node_index, next_node_index].add(symbol)
    # form DOT
    dot_code = [
        'digraph parser_lr_graph {\n'
        'graph [fontname="Symbol"];']
    for node_index, label in node_labels.items():
        dot_code.append(
            f'{node_index} [shape=box,'
            f'label="{label}", labeljust=l];')
    for (start, end), symbols in edges.items():
        ctx = ', '.join(symbols)
        ctx = '{' + ctx + '}'
        dot_code.append(
            f'{start} -> {end} '
            f'[label="{ctx}"];')
    init_label = _tw.dedent(_lu.pformat_state(
        parser._initial))
    init_index = make_index(parser._initial)
    start_node = (
        f'{init_index} [label="{init_label}", '
        'style=filled, fillcolor=gray];')
    dot_code.append(start_node)
    dot_code.append('}')
    dot_code = '\n'.join(dot_code)
    # dump DOT file, convert to PDF
    pdf_filename = 'lr_graph.pdf'
    filename, _ = os.path.splitext(
        pdf_filename)
    dot_filename = f'{filename}.dot'
    with open(dot_filename, 'wt') as fd:
        fd.write(dot_code)
    cmd = [
        'dot', '-Tpdf',
        dot_filename,
        '-o', pdf_filename]
    retcode = _sbp.call(cmd)
    if retcode != 0:
        raise AssertionError(
            retcode, cmd)


def dump_lr_dot(
        parser:
            Parser
        ) -> None:
    """Write LR state machine as DOT file.

    Layout the DOT as PDF,
    using GraphViz `dot`.
    """
    (init_json, actions_json
        ) = dumps_lr_state_machine_json(parser)
    actions = json.loads(actions_json)
    equation_nodes = dict()
    def make_index(equation):
        return equation_nodes.setdefault(
            equation,
            len(actions) + len(equation_nodes))
    edges = _cl.defaultdict(set)
    node_labels = dict()
    for node, out_edges in actions.items():
        for lookahead, todo in out_edges.items():
            if isinstance(todo[1], list):
                symbol, expansion = todo
                equation = (
                    f'{symbol} = ' +
                    ' '.join(expansion))
                next_node = make_index(equation)
                label = equation
            else:
                assert todo[0] == 'state', todo
                next_node = todo[1]
                label = str(next_node)
            node_labels[next_node] = label
            key = (node, next_node)
            edges[key].add(lookahead)
    dot_code = [
        'digraph parser {']
    for node, label in node_labels.items():
        dot_code.append(
            f'{node} '
            f'[label="{label}"];')
    for (start, end), symbols in edges.items():
        lookahead = ', '.join(symbols)
        lookahead = '{' + lookahead + '}'
        dot_code.append(
            f'{start} -> {end} '
            f'[label="{lookahead}"];')
    start_node = (
        f'{init_json} ['
        'style=filled '
        'fillcolor=gray];')
    dot_code.append(start_node)
    dot_code.append('}')
    dot_code = '\n'.join(dot_code)
    # write files
    dot_filename = 'lr_graph.dot'
    pdf_filename = 'lr_graph.pdf'
    with open(dot_filename, 'wt') as fd:
        fd.write(dot_code)
    cmd = [
        'dot', '-Tpdf',
        dot_filename,
        '-o', pdf_filename]
    r = _sbp.call(cmd)
    if r != 0:
        raise AssertionError(r, cmd)


def pprint_lr_state_machine_json(
        parser:
            Parser
        ) -> _Prints:
    initial_json, actions_json = (
        dumps_lr_state_machine_json(parser))
    pprint_json_parser(
        initial_json, actions_json)


def pprint_json_parser(
        initial_json:
            str,
        actions_json:
            str
        ) -> _Prints:
    """Print LR parser given as JSON.

    - `initial_json`:
      initial state
    - `actions_json`:
      transitions of LR state machine
    """
    WIDTH = 40
    print('\n' * 2 + '-' * WIDTH)
    print('JSON export:')
    print('-' * WIDTH)
    print('initial state as JSON:')
    print(initial_json)
    print('actions as JSON:')
    print(actions_json)
    print('prettyprinted actions from JSON:')
    actions = json.loads(actions_json)
    _pp.pp(actions)
    print('=' * WIDTH)


def dumps_lr_state_machine_json(
        parser:
            Parser
        ) -> tuple[
            str,
            str]:
    """Return JSON strings for LR state machine."""
    initial, actions = _nodes_to_int(parser)
    initial_json = json.dumps(initial)
    actions_json = json.dumps(actions)
    return (
        initial_json,
        actions_json)


def _nodes_to_int(
        parser:
            Parser
        ) -> tuple[
            int,
            dict[
                int,
                dict[
                    str,
                    _ty.Any]],
            dict,
            dict]:
    """Represent nodes as `int`.

    Intended for JSON files.
    """
    actions = parser._actions
    # map nodes to integers
    lr_nodes = sorted({
        lr_node
        for lr_node, _ in actions})
    lr_node_indices = {
        lr_node: index
        for index, lr_node in
            enumerate(lr_nodes)}
    n_nodes = len(lr_nodes)
    n_node_indices = len(lr_node_indices)
    if n_nodes != n_node_indices:
        raise AssertionError(
            n_nodes, n_node_indices)
    # map symbols to integers
    symbols = sorted({
        symbol
        for _, symbol in actions})
    symbol_indexing = {
        symbol: index
        for index, symbol in
            enumerate(symbols)}
    # map equations to integers
    eq_indexing = dict()
    int_to_eq = dict()
    for _, action in actions.items():
        eq = action.equation
        if eq is None:
            continue
        if eq in eq_indexing:
            continue
        index = (
            n_nodes +
            len(eq_indexing))
            # for nonoverlap of indices
            # for shifts and reductions
        eq_indexing[eq] = index
        # store equation
        int_to_eq[index] = (
            eq.symbol,
            eq.expansion)
    # map edges to integers
    int_actions = _cl.defaultdict(dict)
    kvs = actions.items()
    for (lr_node, symbol), action in kvs:
        index = lr_node_indices[lr_node]
        node_actions = int_actions[index]
        both = (
            action.state is not None and
            action.equation is not None)
        if both:
            raise ValueError(action)
        if action.state is not None:
            index = lr_node_indices[
                action.state]
            value = index
        elif action.equation is not None:
            eq = action.equation
            value = eq_indexing[eq]
        else:
            raise ValueError(action)
        symbol_index = symbol_indexing[symbol]
        node_actions[symbol_index] = value
    # map initial node to integer
    int_initial = lr_node_indices[
        parser._initial]
    return (
        int_initial,
        int_actions,
        symbol_indexing,
        int_to_eq)


def _parser_from_int_nodes(
        initial:
            int,
        actions:
            dict[
                int,
                dict[
                    str,
                    _ty.Any]],
        symbol_indexing:
            dict,
        int_to_eq:
            dict
        ) -> Parser:
    """Return LR state machine,

    from JSON node representation.
    """
    index_to_symbol = {
        v: k
        for k, v in
            symbol_indexing.items()}
    index_to_eq = {
        int(k): v
        for k, v in
            int_to_eq.items()}
    actions_nd_sym = dict()
    kvs = actions.items()
    for node, sym_action in kvs:
        kv = sym_action.items()
        for symbol_index, value in kv:
            _make_action_at_node(
                node, symbol_index, value,
                actions_nd_sym,
                index_to_symbol,
                index_to_eq)
    _assert_next_nodes_exist(
        actions_nd_sym)
    return Parser(
        initial=initial,
        actions=actions_nd_sym)


def _make_action_at_node(
        node,
        symbol_index,
        index,
        actions_nd_sym,
        index_to_symbol,
        index_to_eq
        ) -> None:
    """Add action at `node`."""
    if index in index_to_eq:
        nonleaf, expansion = index_to_eq[index]
        eq = _grm.Production(
            symbol=nonleaf,
            expansion=expansion)
        action = _lu.Action(
            equation=eq)
    else:
        action = _lu.Action(
            state=index)
    symbol = index_to_symbol[
        int(symbol_index)]
    key = (
        int(node),
        symbol)
    if key in actions_nd_sym:
        raise AssertionError(
            f'key already exists: {key = }`')
    actions_nd_sym[key] = action


def _assert_next_nodes_exist(
        actions):
    """Assert each next node is a node."""
    nodes = {
        node
        for node, _ in
            actions.items()}
    next_nodes = {
        action.state
        for _, action in
            actions.items()
        if action.state is not None}
    for next_node in nodes:
        if next_node not in nodes:
            raise AssertionError(
                next_node, nodes)
