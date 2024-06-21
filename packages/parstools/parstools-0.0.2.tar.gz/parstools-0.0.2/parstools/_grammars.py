"""Representing grammars.

- leafs symbols:
    those that do not appear as contractions
- nonleaf symbols:
    those that appear as contractions
- root symbols:
    those that do not appear in expansions
    (also known as "start symbols")
"""
import collections as _cl
import collections.abc as _abc
import functools as _ft
import itertools as _itr
import random
import textwrap as _tw
import typing as _ty

import parstools._utils as _u


ROOT: _ty.Final[str] = '_ROOT'
END: _ty.Final[str] = '_END'
NULL: _ty.Final[str] = ''
_UNICODE: _ty.Final[bool] = True
_Prints: _ty.TypeAlias = None


class _ProductionBase(
        _ty.NamedTuple):
    r"""Grammar equation.

    For example, the grammar equation:

    ```tla
    /\ expression =
        number & PLUS & number
    ```

    is represented by the instance:

    ```python
    Production(
        'expression',
        ('number', 'PLUS', 'number'))
    ```
    """

    symbol: str
    expansion: tuple[
        str, ...]


class Production(
        _ProductionBase):
    """Grammar equation."""

    __slots__ = ()

    def __new__(
            cls,
            symbol,
            expansion):
        return super().__new__(
            cls,
            symbol,
            tuple(expansion))

    def __str__(
            self
            ) -> str:
        symbols = map(
            format_empty_symbol,
            self.expansion)
        expansion = '\x20'.join(symbols)
        if _UNICODE:  # TODO: decide API
            subseteq = '\u2287'
        else:
            subseteq = r'\subseteq'
        return (
            f'{self.symbol} {subseteq} '
            f'{expansion}')


def format_empty_symbol(
        symbol:
            str
        ) -> str:
    """Map `''` to `'_EMPTY'`."""
    if symbol == NULL:
        return '_EMPTY'
    return symbol


Productions = list[Production]


class Grammar:
    """Formulas of language."""

    def __init__(
            self,
            root_symbol:
                str,
            equations:
                list[
                    Production]
            ) -> None:
        # source data
        self.root_symbol: str = root_symbol
        self._assert_no_duplicates(
            equations)
        self.equations: list[
            Production
            ] = equations
        # derived attributes
        self.groups:dict[
            str,
            set[Production]
            ] = group_equalities(equations)
        self.leafs: set[str
            ] = leaf_symbols(equations)
        self.nonleafs: set[str
            ] = nonleaf_symbols(equations)
        if root_symbol not in self.nonleafs:
            raise ValueError(
                f'{root_symbol = } not in '
                f'{self.nonleafs = }')
        self.symbols: set[str] = (set()
            | self.leafs
            | self.nonleafs)
        if ROOT in self.leafs:
            raise ValueError(
                f'Symbol `{ROOT}` is a leaf.')

    def __str__(
            self
            ) -> str:
        def pformat(symbols):
            return ', '.join(
                f'`{x}`'
                for x in sorted(symbols))
        leafs = pformat(self.leafs)
        nonleafs = pformat(self.nonleafs)
        return (
            'Grammar\n'
            '-------\n'
            f'root symbol: `{self.root_symbol}`\n'
            f'{len(self.equations)} equations\n'
            f'leaf symbols: {leafs}\n'
            f'nonleaf symbols: {nonleafs}\n')

    def __eq__(
            self,
            other
            ) -> bool:
        return (
            hasattr(other, 'root_symbol') and
            hasattr(other, 'equations') and
            self.root_symbol == other.root_symbol and
            self.equations == other.equations)

    @staticmethod
    def _assert_no_duplicates(
            equations
            ) -> None:
        eq_tuples = set()
        for eq in equations:
            eq_tuple = (
                eq.symbol,
                *eq.expansion)
            if eq_tuple not in eq_tuples:
                eq_tuples.add(eq_tuple)
                continue
            raise ValueError(
                'duplicate production: '
                f'{eq}')


def reverse_grammar(
        grammar:
            Grammar
        ) -> Grammar:
    """Return grammar of reversed language."""
    equations = reverse_equations(
        grammar.equations)
    return Grammar(
        root_symbol=grammar.root_symbol,
        equations=equations)


def reverse_equations(
        equations:
            Productions
        ) -> Productions:
    """Reverse the grammatic expansions."""
    return list(
        map(_reverse_equation, equations))


def _reverse_equation(
        equation:
            Production
        ) -> Production:
    """Reverse the expansion of `equation`."""
    expansion = reversed(equation.expansion)
    return Production(
        symbol=equation.symbol,
        expansion=expansion)


def _root_symbols(
        equations:
            list[
                Production]
        ) -> set[
            str]:
    """Return root symbols.

    Root symbols are nonleafs that
    appear not in expansions.
    """
    return (
        nonleaf_symbols(equations) -
        _expansion_symbols(equations))


def group_equalities(
        equations:
            list[
                Production]
        ) -> dict[
            str,
            set[
                Production]]:
    """Group by nonleaf (as keys)."""
    grouped = _cl.defaultdict(set)
    for eq in equations:
        grouped[eq.symbol].add(eq)
    return dict(grouped)


def leaf_symbols(
        equations:
            list[
                Production]
        ) -> set[
            str]:
    """Return leaf symbols.

    Leaf symbols appear in expansions and
    not in contractions.
    """
    symbols = _expansion_symbols(equations)
    if END in symbols:
        raise ValueError(
            f'Symbol `{END}` is already used '
            'in the given grammar productions.')
    symbols.add(END)
    nonleafs = (eq.symbol for eq in equations)
    return symbols.difference(nonleafs)


def symbols_of(
        equations:
            list[
                Production]
        ) -> set[
            str]:
    """Return `set` of grammar symbols.

    The returned set contains both
    leaf and expandable symbols.
    """
    return (
        nonleaf_symbols(equations) |
        _expansion_symbols(equations))


def _expansion_symbols(
        equations:
            list[
                Production]
        ) -> set[
            str]:
    """Return symbols present in expansions."""
    expansions = (
        eq.expansion
        for eq in equations)
    return set().union(*expansions)


def nonleaf_symbols(
        equations:
            list[
                Production]
        ) -> set[
            str]:
    """Return `set` of expandable symbols."""
    return {eq.symbol for eq in equations}


def pprint_grammar(
        grammar:
            Grammar
        ) -> _Prints:
    """Print `grammar` for humans to read."""
    formatted = pformat_grammar(grammar)
    print(formatted)


def pformat_grammar(
        grammar:
            Grammar
        ) -> str:
    """Return formatted `grammar`."""
    GRAMMAR = 'grm'
    symbol_expansions = dict()
    for symbol, equations in grammar.groups.items():
        expansions = list()
        for equation in equations:
            symbol_, expansion = equation
            assert symbol == symbol_, (
                symbol, symbol_)
            expansions.append(expansion)
        def pformat_symbol(
                symbol:
                    str
                ) -> str:
            if symbol[0].isalpha():
                return f'{GRAMMAR}.{symbol}'
            else:
                escaped_symbol = symbol.replace(
                    '"', r'\"')
                return f'tok("{escaped_symbol}")'
        def pformat_expansion(
                expansion:
                    list[str]
                ) -> str:
            formatted_expansion = ' & '.join(map(
                pformat_symbol,
                expansion))
            # empty expansion ?
            if not formatted_expansion:
                formatted_expansion = 'tok("")'
            return f'\n| {formatted_expansion}'
        formatted_expansions = map(
            pformat_expansion,
            expansions)
        pipes = ''.join(sorted(
            formatted_expansions,
            key=len,
            reverse=True))
        symbol_expansions[symbol] = pipes
    def pformat_conjunct(
            symbol:
                str,
            pipes:
                str
            ) -> str:
        indented_pipes = _tw.indent(
            pipes,
            prefix=_u.INDENT)
        formatted_symbol = pformat_symbol(symbol)
        return (
            rf'/\ {formatted_symbol} ='
            f'{indented_pipes}')
    pformatted_grammar = '\n'.join(_itr.starmap(
        pformat_conjunct,
        symbol_expansions.items()))
    pformatted_grammar = _tw.indent(
        pformatted_grammar,
        prefix=_u.INDENT)
    pformatted_grammar = (
        f'is_given_grammar({GRAMMAR}) ==\n'
        f'{pformatted_grammar}')
    return pformatted_grammar


def pick_random_string(
        grammar:
            Grammar,
        symbol:
            str |
            None=None
        ) -> str:
    """Return string in language of `grammar`.

    The string is randomly derived.
    """
    tree = pick_random_tree(grammar, symbol)
    def to_str(tree):
        match tree:
            case list():
                return '\x20'.join(map(
                    to_str, tree))
            case _:
                return tree
    return to_str(tree)


def pick_random_tree(
        grammar:
            Grammar,
        symbol:
            str |
            None=None
        ) -> (
            list |
            str):
    """Return random syntax tree.

    The syntax tree represents a derivation.
    This function is recursively implemented.

    - `symbol`:
        grammar symbol at the root of
        the returned tree
    """
    if symbol is None:
        symbol = grammar.root_symbol
    if symbol in grammar.leafs:
        return symbol
    equations = grammar.groups[symbol]
    equation = random.choice(list(equations))
    expansion = equation.expansion
    recurse = _ft.partial(
        pick_random_tree, grammar)
    return list(map(
        recurse, expansion))
