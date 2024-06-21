"""Utilities for LR parsers."""
import collections.abc as _abc
import functools as _ft
import itertools as _itr
import textwrap as _tw
import typing as _ty

import parstools._ff as _ff
import parstools._grammars as _grm
import parstools._utils as _u


_ROOT: _ty.Final = _grm.ROOT
_END: _ty.Final = _grm.END
Grammar = _grm.Grammar
_Production = _grm.Production


class Dot(
        _ty.NamedTuple):
    """Dotted LR item.

    For example, the LR(0) item:

    ```
    expression -> number . PLUS number
    ```

    is represented by the instance:

    ```python
    Dot(
        'expression',
        done=('number',),
        rest=('PLUS', 'number'))
    ```

    The lookahead is one of:
    - `None`, for LR(0) items
    - a symbol, for LR(1) items
    - a set of symbols, for the
      alternative implementation
      of LR(1) items.
    """

    symbol: str
    done: tuple[str, ...] = tuple()
    rest: tuple[str, ...] = tuple()
    lookahead: (
        str |
        set[str] |
        None) = None

    def __str__(
            self
            ) -> str:
        return _pformat_dot(self)


def _pformat_dot(
        dot:
            Dot,
        unicode:
            bool=True
        ) -> str:
    """Return text describing `dot`."""
    _u.assert_not_in(' . ', dot.done)
    _u.assert_not_in(' . ', dot.rest)
    def pformat(symbols):
        return ' '.join(map(
            _grm.format_empty_symbol, symbols))
    done = pformat(dot.done)
    rest = pformat(dot.rest)
    if done:
        done = f' {done}'
    VERTICAL_LINE = '\u2502'
    if dot.lookahead:
        lookahead = (
            f'  {VERTICAL_LINE} '
            f'{dot.lookahead}')
    else:
        lookahead = ''
    if unicode:
        subseteq = '\u2287'
    else:
        subseteq = r'\subseteq'
    return (
        f'{dot.symbol} {subseteq} '
        f'{done} . {rest}{lookahead}')


class ProjectedDot(
        Dot):
    """LR item hashed by equation only."""

    def __hash__(
            self
            ) -> int:
        return hash(
            self[:3])


_Dots: _ty.TypeAlias = set[Dot]
_DotIterator: _ty.TypeAlias = _abc.Iterator[
    Dot]


class Action(
        _ty.NamedTuple):
    """Shift-reduce activity."""

    state: (
        set |
        None) = None
        # destination after shifting
    equation: (
        _Production |
        None) = None
        # reduction

    def __str__(
            self
            ) -> str:
        if self.equation is not None:
            return (
                'REDUCE using '
                f'equation:  {self.equation}')
        elif self.state is not None:
            state = pformat_state(self.state)
            return (
                'SHIFT and goto '
                f'state:\n{state}')
        return 'Action(state=None, equation=None)'


def make_init_state(
        root_symbol:
            str,
        lookahead_len:
            int
        ) -> set[Dot]:
    """Return kernel of initial state."""
    if lookahead_len == 0:
        lookahead = None
    elif lookahead_len == 1:
        lookahead = _END
    elif lookahead_len > 1:
        raise NotImplementedError
    eq = _make_root_equation(root_symbol)
    item = Dot(
        symbol=_ROOT,
        rest=tuple(eq.expansion),
        lookahead=lookahead)
    return frozenset({item})


def add_root_equation(
        grammar:
            Grammar
        ) -> Grammar:
    """Augment grammar with a root equation."""
    assert_root_and_end_unused(grammar.equations)
    root_symbol = grammar.root_symbol
    root_eq = _make_root_equation(root_symbol)
    equations = grammar.equations + [root_eq]
    return Grammar(root_symbol, equations)


def _make_root_equation(
        root_symbol:
            str
        ) -> _Production:
    """Return equation for root symbol.

    The name of the root grammar symbol is
    stored in the module constant `_ROOT`.
    """
    expansion = (root_symbol,)
    return _Production(
        symbol=_ROOT,
        expansion=expansion)


def shift_dot_in_items(
        items,
        grammar,
        first_sets):
    result = set()
    for item in items:
        more = shift_dot(item)
        result.update(more)
    return result


def shift_dot(
        item:
            Dot
        ) -> Dot:
    """Move symbol from `rest` to `done`.

    - `item`:
        nonfinal LR-item
    """
    head, *rest = item.rest
    done = (*item.done, head)
    return Dot(
        symbol=item.symbol,
        done=done,
        rest=tuple(rest),
        lookahead=item.lookahead)


def dot_of_production(
        equation:
            _Production
        ) -> Dot:
    r"""Make `Dot` from grammar `equation`.

    ```tla
    /\ dot.symbol = equation.symbol
    /\ dot.done = tuple()
    /\ dot.rest = equation.expansion
    ```
    """
    if not equation.expansion:
        raise ValueError(
            'expected nonempty equality '
            'expansion `equation.expansion`, '
            f'but got: {equation = }')
    return Dot(
        symbol=equation.symbol,
        rest=tuple(equation.expansion))


def production_of_dot(
        dot:
            Dot
        ) -> _Production:
    """Make `_Production` from `dot`."""
    # if not dot.done:
    #     raise ValueError(
    #         'expected nonempty LR item '
    #         'accumulator `dot.done`')
    return _Production(
        symbol=dot.symbol,
        expansion=dot.done)


def final_item_of_state(
        state:
            _Dots
        ) -> Dot:
    """Return final item in `state`.

    Asserts that `state` contains
    exactly one final LR(0) item.
    """
    items = final_items(state)
    if not items:
        raise AssertionError(
            'expected some final item')
    if len(items) > 2:
        raise ValueError(
            'reduce/reduce error (?)')
    item, = items
    return item


def final_items(
        items:
            _Dots
        ) -> _abc.Iterator[
            Dot]:
    """Yield LR(0) final items."""
    yield from filter(is_final, items)


def nonfinal_items(
        items:
            _abc.Iterable[
                Dot]
        ) -> _abc.Iterator[
            Dot]:
    """Yield partial LR(0) items."""
    yield from _itr.filterfalse(
        is_final, items)


def is_final(
        item
        ) -> bool:
    """Return `True` if `item` is complete."""
    return not item.rest


def is_empty(
        item:
            Dot
        ) -> bool:
    """Return `True` if `item` has empty expansion."""
    return (
        not item.done and
        not item.rest)


def pick_kernel_item(
        items:
            _abc.Iterable[
                Dot]
        ) -> Dot:
    """Return a non-initial item in `items`."""
    kernel = set(kernel_items(items))
    return _u.pick(kernel)


def kernel_items(
        items:
            _abc.Iterable[
                Dot]
        ) -> _DotIterator:
    """Yield LR kernel items."""
    yield from filter(in_kernel, items)


def partition_kernel(
        items:
            _abc.Iterable[
                Dot]
        ) -> tuple[
            _DotIterator,
            _DotIterator]:
    """Return kernel and nonkernel items."""
    t1, t2 = _itr.tee(items)
    kernel = filter(in_kernel, t1)
    other = _itr.filterfalse(in_kernel, t2)
    return kernel, other


def in_kernel(
        item:
            Dot
        ) -> bool:
    """Return `True` if LR `item` in kernel."""
    return (
        item.done or
        item.symbol == _ROOT)


def assert_root_and_end_unused(
        equations:
            set[
                _Production]
        ) -> None:
    """Assert that the root symbol is unused.

    The name of the root symbol is stored in
    the module constant `_ROOT`.
    """
    symbols = _grm.symbols_of(equations)
    if _ROOT in symbols:
        raise ValueError(
            f'The symbol {_ROOT =} is already used.')
    if _END in symbols:
        raise ValueError(
            f'The symbol {_END =} is already used.')


def assert_lookahead(
        lookahead:
            int
        ) -> None:
    """Assert `lookahead` is as expected."""
    if lookahead < 0:
        raise ValueError(
            r'assumes `lookahead \in Nat` '
            f'(got: `{lookahead = }`')
    if lookahead > 1:
        raise NotImplementedError(
            '`lookahead > 1` will be '
            'implemented '
            f'(got: `{lookahead = }`)')
    if lookahead == 0:
        raise NotImplementedError('TODO')


def show_invisibles(
        string:
            str
        ) -> str:
    """Signify blankspace as per Unicode."""
    if string is None:
        return None
    return string.replace(
        '\u0020', '\u00b7').replace(
        '\n', '\u240a').replace(
        '\t', '\u2409').replace(
        '\u00a0', '\u237d').replace(
        '\r', '\u240d')


def pformat_states(
        states:
            _abc.Iterable
        ) -> str:
    """Return string that shows `states`."""
    states = sorted(
        states,
        key=sorted)
    join = '\n\n'.join
    return join(map(pformat_state, states))


def pformat_state(
        state,
        *,
        equation_groups:
            dict |
            None=None,
        closure:
            bool=False,
        boxed:
            bool=True
        ) -> str:
    """Return string that shows `state`.

    If `closure is True`, then complete
    the itemset `state`, using `grammar`.
    """
    if closure and not equation_groups:
        raise ValueError(
            'need `equation_groups` when '
            'given `closure=True`')
    if closure:
        import parstools._lr.lr as _lr
        state = _lr.closure_lr_0(
            state, equation_groups)
            # TODO: handle also LR(1),
            # LALR(1), SLR(1) states here
    kernel, other_items = partition_kernel(state)
    other_items = list(other_items)
    kernel = list(kernel)
    n_kernel = 1 + len(kernel)
        # +1 for the box's top boundary
    sort = _ft.partial(
        sorted,
        reverse=True)
    vstack = '\n'.join
    def stack_items(
            items:
                _abc.Iterable[
                    str]
            ) -> str:
        return _u.pipe(
            items,
            _pformat_items,
            sort,
            vstack)
    kernel = stack_items(kernel)
    other = stack_items(other_items)
    stacked_items = vstack([kernel, other])
    if not boxed:
        return stacked_items
    # First box, then insert dash line,
    # so that line width measured over
    # all lines that go inside the box.
    box = _box_frame(stacked_items)
    lines = box.splitlines()
    assert lines, lines
    upper = len(lines) - 1
    inv = 0 < n_kernel <= upper
    assert inv, (n_kernel, len(lines))
    width = len(lines[0])
    assert width >= 2, (lines[0], width)
    LINE = '\u2500'
    VERTICAL_LINE = '\u2502'
    HALF_LINE = '\u2574'
    middle = HALF_LINE * (width - 2)
    dashed_line = _vliner(middle)
    assert len(dashed_line) == width, (
        dashed_line, len(dashed_line), width)
    SPACE = '\x20'
    spaces = SPACE * len(middle)
    empty_line = _vliner(spaces)
    kernel_lines = lines[:n_kernel]
    ARROW = '\u21aa'
    label = f'{ARROW}(kernel) '
    label_len = len(label)
    before = empty_line[:-label_len - 1]
    after = empty_line[-1]
    kernel_label = f'{before}{label}{after}'
    other_lines = lines[n_kernel:]
    kernel_part = vstack(kernel_lines)
    other_part = vstack(other_lines)
    if len(other_items) == 0:
        tail = (
            other_part,)
    else:
        tail = (
            kernel_label,
            dashed_line,
            empty_line,
            other_part)
    parts = (
        kernel_part,
        *tail)
    indent = _ft.partial(
        _tw.indent,
        prefix=_u.INDENT)
    return _u.pipe(
        parts,
        vstack,
        indent)


def _box_frame(
        string:
            str
        ) -> str:
    """Return `string` within a rectangle.

    <https://en.wikipedia.org/wiki/Box-drawing_character>
    """
    LINE = '\u2500'
    VERTICAL_LINE = '\u2502'
    BOTTOM_LEFT_CORNER = '\u2514'
    TOP_LEFT_CORNER = '\u250c'
    TOP_RIGHT_CORNER = '\u2510'
    BOTTOM_RIGHT_CORNER = '\u2518'
    lines = string.splitlines()
    n_lines = len(lines)
    line_width = max(map(len, lines))
    horizontal_line = line_width * LINE
    vertical_line = n_lines * VERTICAL_LINE
    box_top = (
        TOP_LEFT_CORNER +
        horizontal_line +
        TOP_RIGHT_CORNER)
    box_bottom = (
        BOTTOM_LEFT_CORNER +
        horizontal_line +
        BOTTOM_RIGHT_CORNER)
    padder = _ft.partial(
        _pad,
        filler=' ',
        width=line_width)
    padded_lines = map(padder, lines)
    box_lines = map(_vliner, padded_lines)
    box_middle = '\n'.join(box_lines)
    return '\n'.join([
        box_top,
        box_middle,
        box_bottom])


def _vliner(
        string:
            str
        ) -> str:
    r"""Prepend and append `'\u2502'`."""
    VERTICAL_LINE = '\u2502'
    return _enside(string, VERTICAL_LINE)


def _enside(
        middle:
            str,
        side:
            str
        ) -> str:
    """Prepend and append `side` to `middle`."""
    return f'{side}{middle}{side}'


def _pad(
        string:
            str,
        filler:
            str,
        width:
            int
        ) -> str:
    r"""Return string padded with filler.

    ```tla
    ASSUME Precondition ==
        /\ len(filler) = 1
        /\ width >= len(string)
    ```

    ```tla
    THEOREM Postcondition ==
        /\ returned_string.startswith(string)
        /\ LET
              start == len(string)
              end == width - 1
              slice == start..end
              tail == returned_string[slice]
           IN
              set(tail) = filler
        /\ len(returned_string) = width
    ```
    """
    if len(filler) != 1:
        raise ValueError(
            'expected `len(filler) == 1`, '
            f'got: {len(filler) = }')
    if width < len(string):
        raise ValueError(
            'expected `width >= len(string)`, '
            f'got: {width = } and '
            f'{len(string) = }')
    assert (
        len(filler) == 1 and
        width >= len(string)), (
            filler, width, string)
    n_padding = width - len(string)
    padding = n_padding * filler
    return f'{string}{padding}'


def _pformat_items(
        items:
            _Dots
        ) -> _abc.Iterator[
            Dot]:
    """Yield formatted LR(0) `items`.

    The formatting aligns the dots
    across the items (when each line
    contains one item).
    """
    items, items_ = _itr.tee(items)
    def depth(
            item
            ) -> str:
        """Return index before dot."""
        dotted_item = str(item)
        return dotted_item.index(' . ')
    depths = map(depth, items)
    dot_depth = 1 + max(depths, default=0)
    def shift(
            item
            ) -> str:
        """Format `item`, aligning dot."""
        dotted_item = str(item)
        depth = dotted_item.index(' . ')
        diff = dot_depth - depth
        padding = diff * ' '
        return f'{padding}{dotted_item}'
    yield from map(shift, items_)
