"""FIRST and FOLLOW sets."""
import collections as _cl
import collections.abc as _abc
import datetime as _dt
import functools as _ft
import itertools as _itr
import operator as _op
import pprint as _pp
import time
import textwrap as _tw
import typing as _ty

import parstools._grammars as _grm
import parstools._utils as _u


_NULL = _grm.NULL
Strings: _ty.TypeAlias = set[str]
StringSeq: _ty.TypeAlias = _abc.Sequence[str]
SymbolSets: _ty.TypeAlias = dict[str, Strings]
Productions: _ty.TypeAlias = list[_grm.Production]
_Prints: _ty.TypeAlias = None


def analyze_grammar_recursion(
        grammar:
            _grm.Grammar
        ) -> _Prints:
    """Print whether left/right recursive."""
    left = is_left_recursive(grammar)
    right = is_right_recursive(grammar)
    if left and right:
        message = (
            'The `grammar` is both '
            'left-recursive and right-recursive '
            '(ambi-recursive).')
    elif left:
        message = (
            'The `grammar` is '
            'left-recursive, and '
            'not right-recursive.')
    elif right:
        message = (
            'The `grammar` is '
            'right-recursive, '
            'and not left-recursive.')
    else:
        message = (
            'The `grammar` is '
            '*not* recursive.')
    print(message)


# NOTE:
# - (direct or indirect) left recursion
#   exists in a grammar if and only if there exists
#   a nonleaf symbol `A` with `A \in FIRST(A)`.
#
# - (direct or indirect) right recursion
#   exists in a grammar if and only if there exists
#   a nonleaf symbol `A` with `A \in LAST(A)`.
def is_left_recursive(
        grammar:
            _grm.Grammar
        ) -> bool:
    """Return `True` if `grammar` is left recursive.

    A grammar includes left recursion if
    any nonleaf symbol can appear first in
    its own expansion (transitively).
    """
    equations = grammar.equations
    firsts = compute_first_sets(equations)
    return _is_endpoint_recursive(
        equations, firsts)


def is_right_recursive(grammar) -> bool:
    """Return `True` if `grammar` is right recursive.

    A grammar includes right recursion if
    any nonleaf symbol can appear last in
    its own expansion (transitively).
    """
    equations = grammar.equations
    lasts = compute_last_sets(equations)
    return _is_endpoint_recursive(
        equations, lasts)


def _is_endpoint_recursive(
        equations,
        symbol_sets
        ) -> bool:
    """Test for left or right recursion."""
    nonleafs = _grm.nonleaf_symbols(equations)
    def is_(nonleaf):
        return nonleaf in symbol_sets[nonleaf]
    return any(map(is_, nonleafs))


def compute_precede_sets(
        equations:
            Productions,
        last_sets:
            SymbolSets |
            None=None
        ) -> SymbolSets:
    """Return mapping to PRECEDE sets.

    For each grammar symbol,
    those symbols that can occur adjacently before
    that grammar symbol form its PRECEDE set.

    The returned PRECEDE sets include nonleaf symbols.
    """
    reversed_equations = _grm.reverse_equations(
        equations)
    if last_sets is None:
        last_sets = compute_last_sets(equations)
    return compute_follow_sets(
        reversed_equations,
        last_sets)


def compute_follow_sets(
        equations:
            Productions,
        first_sets:
            SymbolSets
        ) -> SymbolSets:
    """Return mapping to FOLLOW sets.

    In the returned `dict`:
    - keys are grammar symbols
    - values are sets of grammar symbols
    """
    return _compute_follow_sets_simple(
        equations, first_sets)


def _compute_follow_sets_by_squaring(
        equations:
            Productions,
        first_sets:
            SymbolSets
        ) -> SymbolSets:
    """Return `dict` of FOLLOW sets."""
    raise NotImplementedError(
        'apparently impossible this way')
    nulls = nullable_symbols(equations)
    symbols = _grm.symbols_of(equations)
    leafs = _grm.leaf_symbols(equations)
    edges = {k: set() for k in symbols}
    edges[_grm.ROOT] = set()
    for eq in equations:
        follow = {eq.symbol}
        for symbol in reversed(eq.expansion):
            edges[symbol].update(follow)
            if symbol not in nulls:
                follow = set()
            else:
                follow.add(symbol)
        for a, b in _itr.pairwise(eq.expansion):
            edges[a].update(first_sets[b])
    _squaring_closure(edges)
    return edges


def _compute_follow_sets_simple(
        equations:
            Productions,
        first_sets:
            SymbolSets
        ) -> SymbolSets:
    """Return FOLLOW sets, as `dict`."""
    follow_sets = _cl.defaultdict(set)
    follow_sets[_grm.ROOT].add(_grm.END)
    new = None
    old = dict()
    while old != (old := new):
        _fixpoint_iteration_for_follow_sets(
            follow_sets, first_sets, equations)
        new = _u.dict_value_len(follow_sets)
    return dict(follow_sets)


def _fixpoint_iteration_for_follow_sets(
        follow_sets:
            SymbolSets,
        first_sets:
            SymbolSets,
        equations:
            Productions):
    for eq in equations:
        follow = follow_sets[eq.symbol]
        _follow_set_of_expansion(
            eq.expansion, set(follow),
            follow_sets, first_sets)


def _follow_set_of_expansion(
        expansion:
            StringSeq,
        symbol_follow_set:
            Strings,
        follow_sets:
            SymbolSets,
        first_sets:
            SymbolSets):
    def step(accum, symbol):
        follow_sets[symbol].update(accum)
        firsts = set(first_sets[symbol])
        if _NULL not in firsts:
            accum = set()
        accum.update(firsts)
        accum.discard(_NULL)
        return accum
    accum = set(symbol_follow_set)
    _ft.reduce(
        step, reversed(expansion), accum)


# PROOF:
# prove that this computation is correct
# (i.e., that this computation indeed computes
# the sets of LAST symbols).
def compute_last_sets(
        equations:
            Productions
        ) -> SymbolSets:
    """Return `dict` that maps to LAST sets.

    For each grammar symbol,
    those symbols that can occur last in
    that symbol's expansion form its LAST set.

    The returned LAST sets include nonleaf symbols.
    """
    reversed_equations = _grm.reverse_equations(
        equations)
    return compute_first_sets(
        reversed_equations)


def compute_first_sets(
        equations:
            Productions
        ) -> SymbolSets:
    """Return mapping to FIRST sets.

    These FIRST sets include nonleaf symbols.
    """
    return _compute_first_sets_simple(
        equations)


def compute_first_sets_timed(
        equations:
            Productions
        ) -> SymbolSets:
    """Compare squaring and linear computation."""
    t1 = time.perf_counter()
    firsts = _compute_first_sets_by_squaring(
            equations)
    t2 = time.perf_counter()
    firsts_ = _compute_first_sets_simple(
        equations)
    t3 = time.perf_counter()
    t12 = _pformat_time(t2 - t1)
    t23 = _pformat_time(t3 - t2)
    print(_tw.dedent(f'''
        first sets by:
            squaring: {t12}
            simple: {t23}
        '''))
    if firsts == firsts_:
        return firsts
    _pp.pp(firsts)
    _pp.pp(firsts_)
    raise AssertionError(
        firsts, firsts_)


def _pformat_time(
        seconds:
            float
        ) -> str:
    dt = _dt.timedelta(seconds=seconds)
    return (
        f'{dt.seconds} sec, '
        f'{dt.microseconds} microseconds')


# TODO: precompute SCCs
def _compute_first_sets_by_squaring(
        equations:
            Productions
        ) -> SymbolSets:
    """Return FIRST sets, as `dict`."""
    symbols = _grm.symbols_of(equations)
    leafs = _grm.leaf_symbols(equations)
    # a `defaultdict` here would induce
    # verbosity later below
    edges = {k: set() for k in symbols}
    edges.update((k, {k}) for k in leafs)
    edges[_NULL] = {_NULL}
    nulls = nullable_symbols(equations)
    for k in nulls:
        edges[k].add(_NULL)
    for eq in equations:
        n_items = 1 + _u.ilen(_itr.takewhile(
            nulls.issuperset, eq.expansion))
        prefix = eq.expansion[:n_items]
        edges[eq.symbol].update(prefix)
    _squaring_closure(edges)
    return dict(edges)


def _squaring_closure(
        edges:
            dict
        ) -> None:
    """Compute transitive closure."""
    n_iter = 0
    old_n = None
    while old_n != (old_n := _u.value_len(edges)):
        n_iter += 1
        for reach in edges.values():
            reach.update(
                *(edges[u]
                for u in reach))
    # print(f'{n_iter} iterations via squaring')


def _compute_first_sets_simple(
        equations:
            Productions
        ) -> SymbolSets:
    leafs = _grm.leaf_symbols(equations)
    first_sets = _cl.defaultdict(set)
    first_sets |= {k: {k} for k in leafs}
    first_sets[_NULL] = {_NULL}
    first_sets[_grm.END] = {_grm.END}
        # TODO:
        # can we handle `END` and
        # `_NULL` elsewhere ?
        # At the grammar level ?
    n_iter = 0
    new = None
    old = dict()
    while old != (old := new):
        n_iter += 1
        _fixpoint_iteration_for_first_sets(
            first_sets, equations)
        new = _u.dict_value_len(first_sets)
    # print(f'{n_iter} iterations via stepwise')
    return dict(first_sets)


def _fixpoint_iteration_for_first_sets(
        first_sets:
            SymbolSets,
        equations:
            Productions
        ) -> None:
    for eq in equations:
        nonleaf = eq.symbol
        firsts = first_sets[nonleaf]
        _first_set_of_expansion(
            eq.expansion,
            firsts,
            first_sets)


def _first_set_of_expansion(
        expansion:
            StringSeq,
        firsts:
            Strings,
        first_sets:
            SymbolSets
        ) -> None:
    fs = map(
        first_sets.get,
        expansion)
    for symbol in expansion:
        firsts.add(symbol)
        if symbol not in first_sets:
            return
        more = first_sets[symbol]
        firsts |= more
        if _NULL not in more:
            return
    firsts.add(_NULL)


def firsts_of_seq(
        symbols:
            StringSeq,
        first_sets:
            SymbolSets
        ) -> Strings:
    """Return FIRST(symbols)."""
    firsts = set()
    for symbol in symbols:
        current = first_sets[symbol]
        firsts |= current
        if _NULL not in current:
            break
    return firsts


def nullable_symbols(
        equations:
            Productions
        ) -> set[str]:
    """Return `set` of nullable grammar symbols.

    The returned set always contains the
    empty string `''`.
    """
    nulls = _nulls_using_memoization(equations)
    nulls_ = _nulls_fixpoint(equations)
    assert nulls == nulls_, (nulls, nulls_)
    return nulls


# NOTE:
# squaring seems impossible to do here
def _nulls_using_memoization(
        equations:
            Productions
        ) -> Strings:
    grouped = _grm.group_equalities(equations)
    nulls = {_NULL}
    def is_nullable(symbol):
        return any(
            nulls.issuperset(eq.expansion)
            for eq in grouped[symbol])
    todo = {eq.symbol for eq in equations}
    old_n = None
    while old_n != (old_n := len(todo)):
        todo, yes = _u.partition(is_nullable, todo)
        nulls |= yes
    return nulls


def _nulls_fixpoint(
        equations:
            Productions
        ) -> Strings:
    r"""Nonleaf symbols that can expand to `NULL`.

    ASSUMPTION
        Leaf symbols are not nullable.

    ```tla
    LET
        nullable_nonleafs(nullables) ==
            LET
                NULL == ""
                null == {NULL} | nullables
                eqs == {eq \in equations:
                    range(eq.expansion)
                        \subseteq null}
            IN
                {eq.symbol: eq \in eqs}
    IN
        least_fixpoint(nullable_nonleafs)
    ```
    """
    def nullable_nonleafs(nulls):
        nulls.add(_NULL)
        yield from (
            eq.symbol
            for eq in equations
            if nulls.issuperset(eq.expansion))
    return _u.least_fixpoint(nullable_nonleafs)


def is_finite_language(
        grammar
        ) -> bool:
    """Return `True` when sequences are finite.

    Returns `False` if `grammar`
    describes a language that
    contains any infinite sequences.
    """
    def finite_len(symbols):
        symbols.update(grammar.leafs)
        yield from (
            eq.symbol
            for eq in grammar.equations
            if symbols.issuperset(eq.expansion))
    symbols = _u.least_fixpoint(finite_len)
    return symbols == grammar.symbols


def print_symbol_sets(
        mapping:
            dict,
        title:
            str
        ) -> _Prints:
    """Show sets of symbols, keyed by symbol.

    Intended for printing the sets of symbols
    that comprise the mappings FIRST, FOLLOW,
    LAST, and PRECEDE.
    """
    LINE_WIDTH = 40
    print(_u.HLINE_PIECE * LINE_WIDTH)
    print(title)
    toprint = list()
    for symbol, set_of_symbols in mapping.items():
        toprint.append(
            f'{symbol!r}: {set_of_symbols!r}')
    toprint = '\n'.join(toprint)
    toprint = _tw.indent(
        toprint,
        prefix=_u.INDENT)
    print(toprint)
    print(_u.HLINE_PIECE * LINE_WIDTH)
