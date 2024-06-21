"""Read grammar definition via introspection."""
import collections.abc as _abc
import functools as _ft
import inspect
import itertools as _itr
import textwrap as _tw
import typing as _ty

import parstools._grammars as _grm
import parstools._lex as _lex
import parstools._lr.lr_merging_opt as _lrm
import parstools._lr.lrm_op_prec as _lrm_prec
import parstools._lr.parser as _p
import parstools._lr.utils as _lu


def make_parser(
        grammar_methods,
        operator_precedence:
            list[
                tuple[str]] |
            None=None,
        cache_filepath:
            str |
            None=None
        ) -> _p.Parser:
    """Return parser that reduces using methods."""
    eq_to_method = map_eq_to_methods(
        grammar_methods, 'bnf')
    grammar = grammar_from_docstrings(
        grammar_methods)
    if operator_precedence is None:
        lr_parser = _lrm.make_parser(
            grammar, cache_filepath)
    else:
        lr_parser = _lrm_prec.make_parser(
            grammar, operator_precedence,
            cache_filepath)
    initial = lr_parser._initial
    actions = lr_parser._actions
    return _p.Parser(
        initial, actions,
        tree_map=eq_to_method)


def derivation_to_ast(
        tree,
        grammar_methods,
        notation:
            _ty.Literal[
                'bnf', 'tla']='bnf'
        ) -> _ty.Any:
    """Return syntax-tree, using mapping.

    `grammar_methods` is a class with methods
    labeled with BNF notation. Each method is
    a translation, mapping a node of the tree
    labeled with that grammar production
    (item in set union).

    The current interface is the same with
    `ply` methods `p_method_name(self, p)`.
    """
    eq_to_method = map_eq_to_methods(
        grammar_methods, notation)
    return _drv_to_ast(tree, eq_to_method)


def _drv_to_ast(
        tree,
        eq_to_method):
    """Recursively map tree via methods."""
    # leaf ?
    if tree.equation is None:
        return tree.value
    # nonleaf
    eq = tree.equation
    method = eq_to_method[eq]
    pf = _ft.partial(
        _drv_to_ast,
        eq_to_method=eq_to_method)
    succ = list(map(
        pf, tree.value))
    p = [None, *succ]
    method(p)
    return p[0]


def map_eq_to_methods(
        grammar_definition,
        notation:
            _ty.Literal[
                'bnf', 'tla']
        ) -> dict[
            str,
            _abc.Callable]:
    """Return mapping from equations to methods.

    Each methods maps a derivation-tree to
    a syntax-tree.
    """
    eq_to_method = dict()
    methods = _grammar_methods(
        grammar_definition)
    for method in methods:
        doc = method.__doc__
        for eq in _doc_to_eqs(doc):
            eq_to_method[eq] = method
    def unit(p):
        p[0] = p[1]
    root_symbol = _root_symbol(
        grammar_definition)
    start_eq = (
        f'{_lu._ROOT} ⊇ {root_symbol}')
    eq_to_method[start_eq] = unit
    return eq_to_method


def _doc_to_eqs(
        docstring:
            str
        ) -> _abc.Iterable[
            str]:
    """Return formatted equations."""
    if not docstring:
        raise ValueError(
            docstring)
    symbol, expansion = docstring.split(':')
    symbol = symbol.strip()
    expansions = expansion.split('|')
    def format_eq(expansion):
        expansion = expansion.split()
        expansion = '\x20'.join(expansion)
        return f'{symbol} ⊇ {expansion}'
    yield from map(format_eq, expansions)


def grammar_from_docstrings(
        grammar_definition
        ) -> _grm.Grammar:
    r"""Return grammar from method docstrings.

    The docstrings of the bound methods named
    `p_...` of `grammar_definition` are used
    to create the grammar equations.

    Grammar docstrings have syntax of the form
    `nonleaf_name : expansion_1 | expansion_2 | ...`

    ```tla
    ASSUME
        /\ hasattr(
            grammar_definition,
            "root_symbol")
        /\ \E string \in STRING:
            hasattr(
                grammar_definition,
                "p_" \o string)
    ```
    """
    productions = list()
    methods = _grammar_methods(
        grammar_definition)
    for method in methods:
        docstring = method.__doc__
        if ':' not in docstring:
            raise ValueError(
                'missing symbol `:` in grammar '
                'production within docstring: \n'
                f'{docstring = }')
        if docstring.count(':') != 1:
            raise ValueError(docstring)
        nonleaf, expansions = docstring.split(':')
        nonleaf = nonleaf.strip()
        if '\x20' in nonleaf:
            raise ValueError(nonleaf)
        branches = expansions.split('|')
        for branch in branches:
            if not bool(branch):
                raise ValueError(_tw.dedent(f'''
                    syntax error in the alternative:
                        {branch}
                    within the grammar production of
                    the:
                        {docstring = }
                    '''))
            expansion = branch.split()
            for symbol in expansion:
                if '\x20' not in symbol:
                    continue
                raise ValueError(symbol)
            production = _grm.Production(
                nonleaf, expansion)
            productions.append(production)
    root_symbol = _root_symbol(
        grammar_definition)
    return _grm.Grammar(
        root_symbol=root_symbol,
        equations=productions)


def _root_symbol(
        grammar_definition
        ) -> str:
    """Return root of derivations."""
    has_root_symbol = hasattr(
        grammar_definition, 'root_symbol')
    if has_root_symbol:
        return grammar_definition.root_symbol
    raise ValueError(
        'The given object: '
        f'{grammar_definition = } '
        'does not have an attribute '
        'named `root_symbol`.')


def _grammar_methods(
        grammar_definition
        ) -> _abc.Iterable[
            _abc.Callable]:
    """Yield `p_...` methods."""
    methods = inspect.getmembers(
        grammar_definition,
        predicate=inspect.ismethod)
    if not methods:
        raise ValueError(
            'The given object: '
            f'{grammar_definition = } '
            'does not have any grammar methods. '
            'Grammar methods are bound methods '
            'whose name starts with `p_`.')
    def line_number(x):
        _, method = x
        _, start_line = inspect.getsourcelines(
            method)
        return start_line
    methods = sorted(
        methods,
        key=line_number)
    for name, method in methods:
        is_grammar_method = (
            name.startswith('p_') and
            name != 'p_error')
        if is_grammar_method:
            yield method


def group_operator_tokens(
        tokens:
            _abc.Iterable,
        grouping:
            dict[str, str]
        ) -> _abc.Iterable:
    """Map each operator token by `grouping`.

    Tokens not in `grouping` remain unchanged.
    """
    for token in tokens:
        if token.symbol not in grouping:
            yield token
            continue
        symbol = grouping[token.symbol]
        yield _lex.Token(
            symbol=symbol,
            value=token.value,
            row=token.row,
            column=token.column,
            start=token.start)


def make_operator_groups(
        precedence:
            list[
                tuple[str]],
        unchanged:
            set[str]
        ) -> tuple[
            list[tuple[str, str]],
            dict[str, str]]:
    """Group operators by precedence.

    Operators of the same group have the
    same precedence and fixity. They are
    represented by the same token.

    A function between lexer and parser
    maps between lexer-tokens and
    group-tokens, for the parser.

    `unchanged` contains token names
    for groups that remain the same.
    Implementing unary minus uses this.
    """
    prec = list()
        # operator group token, fixity
    grouping: dict[str, str] = dict()
    enum = enumerate(precedence)
    for index, (fixity, *operators) in enum:
        is_unchanged = (
            len(operators) == 1 and
            operators[0] in unchanged)
        if is_unchanged:
            op_group_token = operators[0]
        else:
            fixity_ = fixity.upper()
            op_group_token = f'OP_{index}_{fixity_}'
        token_fixity = (
            op_group_token,
            fixity)
        prec.append(token_fixity)
        if is_unchanged:
            continue
        for op_token in operators:
            if op_token in grouping:
                raise ValueError(
                    f'operator `{op_token}` '
                    'is duplicated')
            grouping[op_token] = op_group_token
    return (
        prec,
        grouping)


def make_operator_grammar(
        precedence_associativity:
            list[
                tuple[str, str]],
        apply:
            _abc.Callable,
        grammar
        ) -> None:
    """Add grammar methods to `instance`.

    These methods represent a grammar that
    describes the precedence and associativity of
    operators defined in `precedence_associativity`,
    as pairs of token-name and fixity-associativity:

    - `'prefix'` (nestable)
    - `'infix'` (not nestable)
    - `'left'` (infix left associative)
    - `'right'` (infix right associative)
    - `'postfix'` (nestable)
    - `None` for the last item

    For example:

    ```
    precedence_associativity = [
        ('OR', 'left'),
        ('AND', 'left'),
        ('rest_of_grammar', None)]
    ```

    The last item is the symbol that connects to
    the rest of the grammar, and is not mapped to
    a grammar equality.

    `apply()` is called with arguments
    `[operator, *operands]`, where `operator` is
    an infix, prefix, or postfix operator.

    `grammar` is the grammar instance to bind
    the methods to.
    """
    enum = enumerate(_itr.pairwise(
        precedence_associativity))
    for i, ((operator, fixity), (
            operand, operand_fixity)) in enum:
        if operand_fixity is not None:
            operand = f'op_{i + 1}_{operand_fixity}'
        # repetition method
        grammar_symbol = f'op_{i}_{fixity}'
        method_name = f'p_{grammar_symbol}_repeat'
        match fixity:
            case 'prefix':
                repetition_docstring = f'''
                    {grammar_symbol} :
                        {operator} {grammar_symbol}
                    '''
                def method_repeat(self, p):
                    args = [p[1], p[2]]
                    p[0] = apply(*args)
            case 'infix':
                repetition_docstring = f'''
                    {grammar_symbol} :
                        {operand} {operator} {operand}
                    '''
                def method_repeat(self, p):
                    args = [p[2], p[1], p[3]]
                    p[0] = apply(*args)
            case 'left':
                repetition_docstring = f'''
                    {grammar_symbol} :
                        {grammar_symbol} {operator}
                        {operand}
                    '''
                def method_repeat(self, p):
                    args = [p[2], p[1], p[3]]
                    p[0] = apply(*args)
            case 'right':
                repetition_docstring = f'''
                    {grammar_symbol} :
                        {operand} {operator}
                        {grammar_symbol}
                    '''
                def method_repeat(self, p):
                    args = [p[2], p[1], p[3]]
                    p[0] = apply(*args)
            case 'postfix':
                repetition_docstring = f'''
                    {grammar_symbol} :
                        {grammar_symbol} {operator}
                    '''
                def method_repeat(self, p):
                    args = [p[2], p[1]]
                    p[0] = apply(*args)
            case _:
                raise ValueError(fixity)
        _attach_method(
            method_repeat, method_name,
            repetition_docstring, grammar)
        # start method
        start_docstring = f'''
            {grammar_symbol} : {operand}
            '''
        def method_start(self, p):
            p[0] = p[1]
        method_name = f'p_{grammar_symbol}_start'
        _attach_method(
            method_start, method_name,
            start_docstring, grammar)


def _attach_method(
        method,
        name,
        docstring,
        instance):
    """Bind `method` to `instance`.

    `name` is the attribute name for the method.
    """
    method.__name__ = name
    method.__doc__ = docstring
    bound_func = method.__get__(instance)
    setattr(instance, name, bound_func)
