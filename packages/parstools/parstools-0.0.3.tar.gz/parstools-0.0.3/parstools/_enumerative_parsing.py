"""Parsing by enumeration of all derivation trees.

The enumerative pattern-matching algorithm of
this module is intended for testing purposes.
"""
import collections as _cl
import collections.abc as _abc

import parstools._grammars as _grm


def parse(
        text,
        grammar:
            _grm.Grammar
        ) -> tuple:
    r"""Return a derivation tree for `text`.

    The derivation is found by enumeration of
    derivations in increasing length of foliage,
    until the sequence `text` is matched.

    Non-blankspace symbols in `text` are
    assumed to be joined by one space `\x20`.
    """
    trees = enumerate_trees(grammar)
    for tree in trees:
        foliage = _foliage(tree)
        # print(seq)
        if foliage == text:
            return tree


def enumerate_trees(
        grammar:
            _grm.Grammar
        ) -> _abc.Iterable:
    """Enumerate all sequences of `grammar`."""
    groups = _cl.defaultdict(list)
    items = grammar.groups.items()
    for nonleaf, eqs in items:
        for eq in eqs:
            head = eq.expansion[0]
            if head in grammar.leafs:
                groups[nonleaf].append(eq)
    items = grammar.groups.items()
    for nonleaf, eqs in items:
        for eq in eqs:
            head = eq.expansion[0]
            if head in grammar.nonleafs:
                groups[nonleaf].append(eq)
    groups = dict(groups)
    yield from _enumerate_trees(
        grammar.root_symbol, groups)


def _enumerate_trees(
        symbol:
            str,
        groups:
            dict
        ) -> _abc.Iterable:
    """Enumerate all trees for `symbol`."""
    # leaf ?
    if symbol not in groups:
        yield symbol
        return
    # nonleaf
    eqs = groups[symbol]
    expansions = list()
    for eq in eqs:
        expansion = eq.expansion
        enum = _enumerate_expansion(
            expansion, groups)
        expansions.append(enum)
    while expansions:
        expansions_ = list()
        for enum in expansions:
            try:
                yield next(enum)
                expansions_.append(enum)
            except StopIteration:
                pass
        expansions = expansions_


def _enumerate_expansion(
        expansion,
        groups):
    """Enumerate all expansions."""
    if not expansion:
        yield tuple()
        return
    head, *rest = expansion
    trees = _enumerate_trees(head, groups)
    tails = _enumerate_expansion(rest, groups)
    for tail in tails:
        for tree in trees:
            yield (tree, *tail)


def _foliage(
        tree):
    """Join leafs, with spaces in-between."""
    if isinstance(tree, str):
        return tree
    return '\x20'.join(map(_foliage, tree))


def _test_enumerate_trees():
    grammar = _test_grammar()
    text = 'A - A + A + A + A + A'
    tree = parse(text, grammar)
    print(tree)
    seq = _foliage(tree)
    print(seq)


def _test_grammar(
        ) -> _grm.Grammar:
    """Return sample grammar."""
    root_symbol = 'expr'
    equations = [
        _grm.Production(
            'expr',
            ['expr', '+', 'A']),
        _grm.Production(
            'expr',
            ['expr', '-', 'A']),
        _grm.Production(
            'expr',
            ['A']),
        ]
    return _grm.Grammar(
        root_symbol=root_symbol,
        equations=equations)


if __name__ == '__main__':
    _test_enumerate_trees()
