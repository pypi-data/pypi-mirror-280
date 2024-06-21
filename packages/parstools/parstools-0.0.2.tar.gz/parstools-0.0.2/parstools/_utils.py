"""Utilities."""
import collections.abc as _abc
import collections as _cl
import functools as _ft
import itertools as _itr
import json
import operator as _op
import pprint as _pp
import typing as _ty


HLINE_PIECE: _ty.Final[str] =\
    '\u2500'
SPACE: _ty.Final[str] =\
    '\x20'
INDENT: _ty.Final[str] =\
    4 * SPACE


_Item = _ty.TypeVar('_Item')
_Key = _ty.TypeVar('_Key')
_Value = _ty.TypeVar('_Value')


class DiGraph:
    """Directed graph.

    Implements part of the `networkx` API.
    """

    def __init__(
            self
            ) -> None:
        self._nodes = set()
        self._edges = _cl.defaultdict(dict)
            # node key ->
            # node key ->
            #     edge label

    def __iter__(
            self
            ) -> _abc.Iterator:
        """Return iterator over nodes."""
        return self.nodes()

    def add_edge(
            self,
            node:
                _abc.Hashable,
            other:
                _abc.Hashable,
            label:
                _ty.Any |
                None=None
            ) -> None:
        """Add edge from `node` to `other`.

        Annotate this edge with `label`.
        """
        self._nodes.update((node, other))
        self._edges[node][other] = label

    def nodes(self) -> _abc.Iterator:
        """Yield nodes."""
        yield from self._nodes

    def edges(
            self,
            data:
                bool=False
            ) -> _abc.Iterator[
                tuple]:
        """Yield edges.

        If `data`, then yield triplets that
        include the label as last item.
        """
        edges = self._edges.items()
        for node, other_label in edges:
            yield from self._labeled_edges(
                node, other_label, data)

    def _labeled_edges(
            self,
            node,
            other_label,
            data
            ) -> (
                _abc.Iterator[
                    tuple[_Item, _Item]] |
                _abc.Iterator[
                    tuple[_Item, _Item, _Item]]):
        """Yield (annotated) edges."""
        if data:
            items = other_label.items()
            for other, label in items:
                yield (node, other, label)
        else:
            for other in other_label:
                yield (node, other)


class MonotonicDict(
        _cl.UserDict):
    """Dictionary with no key-value removal.

    *Does* allow re-adding existing
    key-value pairs.
    """

    def __setitem__(
            self,
            key,
            value
            ) -> _ty.Any:
        add = (
            key not in self or
            self[key] == value)
        if add:
            return super().__setitem__(
                key, value)
        key_str = _pp.pformat(key)
        raise ValueError(
            '\n'
            f'key = {key_str}\n'
            f'{self[key] = }\n'
            f'{value = }\n')


def is_monotonic(
        sequence:
            _abc.Sequence,
        reverse:
            bool=False
        ) -> bool:
    r"""Return `True` if nondecreasing.

    ```tla
    sequence_is_nondecreasing ==
        \A index \in 1..Len(sequence):
            sequence[index - 1] <=
            sequence[index]
    ```
    """
    if reverse:
        sequence = reversed(list(sequence))
    pairs = _itr.pairwise(sequence)
    leq = _itr.starmap(_op.le, pairs)
    return all(leq)


def _namedtuple_to_json(
        namet:
            _ty.NamedTuple
            ) -> str:
    """Serialize namedtuple as JSON."""
    return json.dumps(namet._asdict())


def assert_not_in(
        value:
            _ty.Any,
        items:
            _abc.Container
        ) -> None:
    """Assert `value not in items`."""
    if value not in items:
        return
    raise AssertionError(
        value, items)


def dict_value_len(
        mapping:
            dict
        ) -> dict:
    """Map `len` over `dict` values.

    Return a `dict` with the keys of `d`,
    and values the lengths of the values
    of `d`.
    """
    return {
        k: len(v)
        for k, v in mapping.items()}


def value_len(
        kv:
            _abc.Mapping
        ) -> int:
    return sum(
        len(v)
        for v in kv.values())


def least_fixpoint(
        operator:
            _abc.Callable
        ) -> set:
    """Return fixpoint of monotonic `operator`.

    Enumerative computation.
    """
    items = set()
    old_len = None
    while old_len != (old_len := len(items)):
        items.update(operator(items))
    return items


def _partition_using_tee(
        predicate:
            _abc.Callable[
                ...,
                bool],
        items:
            _abc.Iterable
        ) -> tuple[
            set,
            set]:
    """Return other, and matching items."""
    t1, t2 = _itr.tee(items)
    no = _itr.filterfalse(predicate, t1)
    yes = filter(predicate, t2)
    no, yes = map(set, [no, yes])
    return no, yes


def partition(
        predicate:
            _abc.Callable[
                ...,
                bool],
        items:
            _abc.Iterable[
                _Item]
        ) -> (
            (s := set[_Item]) and
            tuple[s, s]):
    """Return two sets: `(rest, matching)`.

    The set `matching` contains values in
    `items` for which `predicate` returns
    `True`. The set `rest` contains the
    remaining values from `items`.
    """
    bins = (set(), set())
    for item in items:
        index = int(predicate(item))
        bins[index].add(item)
    return bins


def pick(
        items:
            _abc.Iterable[
                _Item]
        ) -> _Item:
    """Return an element of `items`.

    Raise `ValueError` if `items` is empty.
    """
    try:
        return next(iter(items))
    except StopIteration as error:
        raise ValueError(
            items) from error


def filter_(
        items:
            _abc.Iterable[
                _Item]
        ) -> _abc.Iterable[
            _Item]:
    """Return truthy items."""
    return filter(None, items)


def pipe(
        start_value:
            _ty.Any,
        *callables:
            _abc.Callable
        ) -> _ty.Any:
    """Apply callables to `start_value`."""
    result = start_value
    for callable in callables:
        result = callable(result)
    return result


def set_union(
        dictionary:
            dict[
                _Key,
                _Value],
        items:
            set[
                _Key]
        ) -> set[
            _Value]:
    """Return union of `dictionary` values.

    The values are those that correspond to
    the elements of `items`.
    """
    return set().union(*(
        dictionary[item]
        for item in items))


def ilen(
        iterable:
            _abc.Iterable
        ) -> int:
    """Return length of iterable."""
    return sum(1 for _ in iterable)


def imap(
        function:
            _abc.Callable,
        *arg,
        **kw
        ) -> _abc.Callable:
    """Partially apply `map` to `function`."""
    return _ft.partial(map, function)
