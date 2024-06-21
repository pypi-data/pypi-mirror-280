"""Foliage, measuring, pprint trees."""
import collections.abc as _abc
import typing as _ty


class Tree(
        _ty.NamedTuple):

    symbol: str
    value: str | list
    row: int | None = None
    column: int | None = None


def tree_len(
        tree,
        attribute_name:
            str
        ) -> int:
    """Return number of nodes (treelets).

    `attribute_name` is where the successor
    nodes are stored.
    """
    count = 0
    todo = [tree]
    while todo:
        t = todo.pop()
        count += 1
        succ = getattr(t, attribute_name)
        is_leaf = (
            isinstance(succ, str) or
            succ is None)
        if is_leaf:
            continue
        todo.extend(succ)
    return count


def foliage(
        tree:
            Tree |
            None
        ) -> str | None:
    """Return concatenated leafs.

    Maps a syntax trees to a
    lexeme sequence, with blankspace
    inserted.
    """
    if tree is None:
        return None
    if isinstance(tree.value, str):
        return tree.value
    return '\x20'.join(map(
        foliage, tree.value))


def pprint_tree(
        tree
        ) -> None:
    """Print tree."""
    lines = pformat_tree(tree)
    text = '\n'.join(lines)
    text = f'{tree.symbol}\n{text}'
    print(text)


def pformat_tree(
        tree
        ) -> _abc.Iterator[str]:
    """Iterator of lines showing `tree`."""
    for i, u in enumerate(tree.value):
        prefix = '├──' if i < len(tree.value) - 1 else '└──'
        if isinstance(u.value, str):
            yield f'{prefix} {u.symbol}:{u.value}'
            continue
        else:
            yield f'{prefix} {u.symbol}'
        prefix = '│' if i < len(tree.value) - 1 else ' '
        for line in pformat_tree(u):
            yield f'{prefix}   {line}'
