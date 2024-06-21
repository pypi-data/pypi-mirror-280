"""Regular languages.

- matching regular expressions
- regular expression to automaton (NFA) conversion
- automaton to regular grammar conversion
- grammar to automaton conversion
- grammar to regular expression conversion
- automaton difference and intersection
"""
import collections as _cl
import collections.abc as _abc
import functools as _ft
import os
import pprint as _pp
import shlex as _sh
import subprocess as _sbp
import textwrap as _tw
import typing as _ty

import parstools._grammars as _grm
import parstools._introspection as _intro
import parstools._lr.lr_merging_opt as _lrm
import parstools._lr.parser as _p


Node = _ty.TypeVar('Node')


class Tree(
        _ty.NamedTuple):
    """Syntax tree."""

    symbol: str
    value: str | tuple


class NFA:
    """Nondeterministic automaton."""

    def __init__(
            self,
            initial_node:
                Node,
            accepting_nodes:
                set,
            edges:
                dict
            ) -> None:
        """Initialization.

        Nodes can be `int` or
        (nested) `tuple[int]` for
        product automata.
        """
        self.edges: dict[
            Node,
            dict[str, set[Node]]
            ] = edges
        self.initial_node: Node = initial_node
        self.accepting_nodes: set[Node
            ] = accepting_nodes

    def __str__(
            self
            ) -> str:
        """Return textual description."""
        indent = 4 * '\x20'
        edges = list()
        items = self.edges.items()
        for node, symbol_edges in items:
            kv = symbol_edges.items()
            for symbol, next_nodes in kv:
                for next_node in next_nodes:
                    edge = (
                        f'{node} '
                        f'--({symbol})--> '
                        f'{next_node}')
                    edges.append(edge)
        edges = '\n'.join(edges)
        edges = _tw.indent(
            edges,
            prefix=4 * indent)
        return _tw.dedent(f'''
            initial_node =
                {self.initial_node}
            accepting_nodes =
                {self.accepting_nodes}
            edges =\n{edges}
            ''')

    def to_dot(
            self
            ) -> str:
        """Return DOT representation."""
        # edges
        edges = list()
        for node, nd_edges in self.edges.items():
            items = nd_edges.items()
            for symbol, next_node in items:
                edge = (
                    f'{node} -> {next_node}'
                    f'[label="{symbol}"]; ')
                edges.append(edge)
        edges_text = '\n'.join(edges)
        # accepting nodes
        nodes = list()
        for node in self.accepting_nodes:
            node_text = (
                f'{node} '
                '[shape="doublecircle"];')
            nodes.append(node_text)
        # initial node
        init_text = (
            f'{self.initial_node} '
            '[shape="box"];')
        nodes.append(init_text)
        nodes_text = '\n'.join(nodes)
        return f'''
            digraph {{
                {edges_text}
                {nodes_text}
            }}
            '''


def nfa_to_dot(
        nfa,
        pdf_filename:
            str
        ) -> None:
    """Layout `nfa` as PDF using `dot`."""
    dot_text = nfa.to_dot()
    name, ext = os.path.splitext(pdf_filename)
    dot_filename = f'{name}.dot'
    with open(dot_filename, 'w') as fd:
        fd.write(dot_text)
    prog = _sh.split(f'''
        dot -Tpdf
            -o {pdf_filename}
            {dot_filename}
        ''')
    _sbp.call(prog)


def match_regex(
        pattern:
            str,
        string:
            str
        ) -> set[int]:
    """Return matches of `pattern` in `string`.

    Returns end-positions of spans that match
    `pattern`. For example:

    ```py
    regex = ' a & a* '
    text = 'aa'
    indices = match_regex(regex, text)
    assert indices == {1, 2}, indices
    ```

    because there are two matching sequences:
    `'a'` (matches at index 1) and
    `'aa'` (matches at index 2).
    """
    nfa = regex_to_nfa(pattern)
    nfa_to_grammar(nfa)
    matches = set()
    nodes = {nfa.initial_node}
    if _intersect_accepting(nodes, nfa):
        matches.add(0)
    for index, symbol in enumerate(string):
        next_nodes = set()
        for node in nodes:
            has_edges = (
                node in nfa.edges and
                symbol in nfa.edges[node])
            if not has_edges:
                continue
            succ = nfa.edges[node][symbol]
            next_nodes.update(succ)
        nodes = next_nodes
        if _intersect_accepting(nodes, nfa):
            matches.add(index + 1)
    return matches


def _intersect_accepting(
        nodes:
            set,
        nfa:
            NFA
        ) -> bool:
    """Return `True` if any node is accepting."""
    for node in nodes:
        if node in nfa.accepting_nodes:
            return True
    return False


def parse_regex(
        regex:
            str
        ) -> Tree:
    """Return syntax tree for `regex`."""
    cached_parser = hasattr(parse_regex, '_parser')
    if not cached_parser:
        grammar = RegexGrammar()
        parse_regex._parser = _intro.make_parser(
            grammar)
    tokens = lex_regex(regex)
    result = parse_regex._parser.parse(tokens)
    if result is None:
        raise ValueError(result)
    tree = result.value
    return tree


def parse_regex_to_result(
        regex:
            str
        ) -> _p.Result:
    """Return derivation tree for `regex`."""
    grammar = regex_grammar()
    parser = _lrm.make_parser(grammar)
    tokens = list(lex_regex(regex))
    # for token in tokens:
    #     print(token)
    tree = parser.parse(tokens)
    if tree is None:
        raise ValueError(tree)
    return tree


def regex_grammar(
        ) -> _grm.Grammar:
    """Return description of regular expression syntax."""
    Prod = _grm.Production
    root_symbol = 'regex'
    equations = [
        Prod('regex', ['union']),
        Prod('union', ['union', 'PIPE', 'cat']),
        Prod('union', ['cat']),
        Prod('cat', ['cat', 'ET', 'rep']),
        Prod('cat', ['rep']),
        Prod('rep', ['rep', 'CARET_ASTERISK']),
        Prod('rep', ['rep', 'ASTERISK']),
        Prod('rep', ['paren']),
        Prod('paren', ['LPAREN', 'regex', 'RPAREN']),
        Prod('paren', ['NAME']),
        ]
    return _grm.Grammar(
        root_symbol, equations)


class RegexGrammar:
    """Describes regular expressions."""

    def __init__(
            self
            ) -> None:
        """Constructor."""
        self.root_symbol = 'regex'

    def p_regex(
            self, p):
        """regex : union"""
        p[0] = p[1]

    def p_union_loop(
            self, p):
        """union : union PIPE cat"""
        operands = (p[1], p[3])
        p[0] = Tree(
            symbol='|',
            value=operands)

    def p_union_start(
            self, p):
        """union : cat"""
        p[0] = p[1]

    def p_cat_loop(
            self, p):
        """cat : cat ET rep"""
        operands = (p[1], p[3])
        p[0] = Tree(
            symbol='&',
            value=operands)

    def p_cat_start(
            self, p):
        """cat : rep"""
        p[0] = p[1]

    def p_rep_loop(
            self, p):
        """rep : rep CARET_ASTERISK
               | rep ASTERISK
        """
        p[0] = Tree(
            symbol='^*',
            value=(p[1],))

    def p_rep_start(
            self, p):
        """rep : paren"""
        p[0] = p[1]

    def p_parentheses(
            self, p):
        """paren : LPAREN regex RPAREN"""
        p[0] = p[2]

    def p_name(
            self, p):
        """paren : NAME"""
        p[0] = Tree(
            symbol='NAME',
            value=p[1])


def lex_regex(
        text:
            str
        ) -> list[
            Tree]:
    """Return tokens for `text`.

    `text` is a regular expression.
    """
    # NAME
    #     [a-zA-Z_0-9]+
    token_to_lexeme = dict(
        PIPE=
            '|',
        ET=
            '&',
            # in Python regexes
            # catenation is implicit
        ASTERISK=
            '*',
        # CARET_ASTERISK=
        #     '^*',
        # at this level of parsing,
        # one-char symbols
        LPAREN=
            '(',
        RPAREN=
            ')')
    lexeme_to_token = {
        v: k
        for k, v in
            token_to_lexeme.items()}
    tokens = list()
    for char in text:
        # implements `re.VERBOSE`
        if char in {'\x20', '\n'}:
            continue
        if char in lexeme_to_token:
            symbol = lexeme_to_token[char]
            token = Tree(
                symbol=symbol,
                value=char)
            tokens.append(token)
            continue
        assert char not in lexeme_to_token, char
        token = Tree(
            symbol='NAME',
            value=char)
        tokens.append(token)
    return tokens


def regex_to_nfa(
        regex:
            str
        ) -> NFA:
    """Return acceptor for `regex`."""
    tree = parse_regex(regex)
    # print(tree)
    return regex_tree_to_nfa(tree)


def regex_tree_to_nfa(
        tree:
            Tree
        ) -> NFA:
    """Return acceptor for syntax `tree`."""
    nodes = set()
    succ = _cl.defaultdict(
        lambda: _cl.defaultdict(set))
    pred = _cl.defaultdict(
        lambda: _cl.defaultdict(set))
    (start, accepting_nodes
        ) = _regex_tree_recurse(
            tree, nodes, succ, pred)
    # _pp.pp(succ)
    # reachability
    nodes = reachable_nodes(
        {start}, succ)
    nodes &= reachable_nodes(
        accepting_nodes, pred)
    # project accepting onto reachable nodes
    accepting_nodes = accepting_nodes & nodes
    # project edges onto reachable nodes
    edges = _cl.defaultdict(
        lambda: _cl.defaultdict(set))
    for node, edge in succ.items():
        if node not in nodes:
            continue
        for symbol, next_nodes in edge.items():
            for next_node in next_nodes:
                if next_node not in nodes:
                    continue
                edges[node][symbol].add(
                    next_node)
    # _pp.pp(edges)
    edges_ = dict()
    for k, v in edges.items():
        edges_[k] = dict(v)
    return NFA(
        initial_node=start,
        accepting_nodes=accepting_nodes,
        edges=edges_)


def _regex_tree_recurse(
        tree:
            Tree,
        nodes:
            set,
        succ:
            dict,
        pred:
            dict
        ) -> tuple[
            int,
            set[int]]:
    """Recursively convert to acceptor.

    Return `(initial_node, accepting_nodes)`.
    """
    rec = _ft.partial(
        _regex_tree_recurse,
        nodes=nodes,
        succ=succ,
        pred=pred)
    match tree.symbol:
        case '|':
            (nd_u, a1), (nd_a, a2) = map(
                rec, tree.value)
            # make node `nd_a` initial
            # in place of `nd_u`
            items = succ[nd_u].items()
            for symbol, succ_nodes in items:
                for p in succ_nodes:
                    # cycle on initial node ?
                    if p == nd_u:
                        p = nd_a
                    _add_edge(
                        nd_a, symbol, p,
                        succ, pred)
            # initial node is accepting ?
            if nd_u in a1:
                a1.remove(nd_u)
                a1.add(nd_a)
            return (nd_a, a1 | a2)
        case '&':
            (nd_u, a1), (nd_a, a2) = map(
                rec, tree.value)
            # transition to `nd_a` in parallel
            # to transitioning to `a1`
            for nd_v in a1:
                items = pred[nd_v].items()
                for symbol, pred_nodes in items:
                    for p in pred_nodes:
                        _add_edge(
                            p, symbol, nd_a,
                            succ, pred)
            # initial node is accepting ?
            if nd_u in a1:
                # replace node `nd_u` with `nd_a`
                items = pred[nd_u].items()
                for symbol, pred_nodes in items:
                    for p in pred_nodes:
                        # cycle on initial node ?
                        if p == nd_u:
                            p = nd_a
                        _add_edge(
                            p, symbol, nd_a,
                            succ, pred)
                items = succ[nd_u].items()
                for symbol, succ_nodes in items:
                    for p in succ_nodes:
                        # cycle on initial node ?
                        if p == nd_u:
                            p = nd_a
                        _add_edge(
                            nd_a, symbol, p,
                            succ, pred)
                nd_u = nd_a
            return (nd_u, a2)
        case '^*':  # *
            (nd_u, a1), = map(
                rec, tree.value)
            # make node `nd_u` accepting
            for nd_v in a1:
                items = pred[nd_v].items()
                for symbol, pred_nodes in items:
                    for p in pred_nodes:
                        _add_edge(
                            p, symbol, nd_u,
                            succ, pred)
            return (nd_u, {nd_u})
        case 'NAME':
            node = len(nodes)
            nodes.add(node)
            next_node = len(nodes)
            nodes.add(next_node)
            symbol = tree.value
            _add_edge(
                node, symbol, next_node,
                succ, pred)
            return (
                node,
                {next_node})
        case _:
            raise ValueError(tree)


def _add_edge(
        node:
            int,
        symbol:
            str,
        next_node:
            int,
        succ:
            dict,
        pred:
            dict
        ) -> None:
    """Add edge to `succ` and `pred`."""
    succ[node][symbol].add(next_node)
    pred[next_node][symbol].add(node)


def nfa_to_grammar(
        nfa:
            NFA
        ) -> _grm.Grammar:
    """Return regular grammar, from `nfa`."""
    # index nodes
    node_to_index = dict()
    for node, edges in nfa.edges.items():
        nodes = set().union(*edges.values())
        nodes.add(node)
        for nd in nodes:
            node_to_index.setdefault(
                nd, len(node_to_index))
    # print(node_to_index)
    # convert edges to productions
    eqs = list()
    for node, edges in nfa.edges.items():
        nonleaf = _node_to_nonleaf(
            node, node_to_index)
        for symbol, next_nodes in edges.items():
            for next_node in next_nodes:
                next_nonleaf = _node_to_nonleaf(
                    next_node, node_to_index)
                next_edges = (
                    next_node in nfa.edges and
                    nfa.edges[next_node])
                is_accepting = (
                    next_node in
                        nfa.accepting_nodes)
                next_edges_or_accepting = (
                    next_edges or
                    is_accepting)
                if not next_edges_or_accepting:
                    raise ValueError(
                        node, symbol, next_node)
                if next_edges:
                    # nonleaf = symbol & next_nonleaf
                    expansion = [symbol, next_nonleaf]
                    eq = _grm.Production(
                        symbol=nonleaf,
                        expansion=expansion)
                    eqs.append(eq)
                if is_accepting:
                    # nonleaf = symbol
                    expansion = [symbol]
                    eq = _grm.Production(
                        symbol=nonleaf,
                        expansion=expansion)
                    eqs.append(eq)
    # root symbol
    root_symbol = _node_to_nonleaf(
        nfa.initial_node, node_to_index)
    if nfa.initial_node in nfa.accepting_nodes:
        expansion = list()
        eq = _grm.Production(
            symbol=root_symbol,
            expansion=expansion)
        eqs.append(eq)
    grammar = _grm.Grammar(
        root_symbol=root_symbol,
        equations=eqs)
    # print(_grm.pformat_grammar(grammar))
    return grammar


def _node_to_nonleaf(
        node,
        node_to_index:
            dict
        ) -> str:
    """Return grammar symbol of node."""
    index = node_to_index[node]
    return f'nonleaf_{index}'


def grammar_to_nfa(
        grammar:
            _grm.Grammar
        ) -> NFA:
    """Return machine from `grammar`."""
    # index nodes
    nonleafs = set(grammar.nonleafs)
    node_indexing = dict()
    for index, nonleaf in enumerate(nonleafs):
        node_indexing[nonleaf] = index
    initial_node = node_indexing[
        grammar.root_symbol]
    # accepting nodes
    accepting_node = len(node_indexing)
    if accepting_node in nonleafs:
        raise ValueError(
            'nonleaf grammar symbols '
            'need be strings')
    accepting_nodes = {accepting_node}
    # edges to accepting node
    edges = _cl.defaultdict(
        lambda: _cl.defaultdict(set))
    for eq in grammar.equations:
        symbol = eq.symbol
        node = node_indexing[symbol]
        match eq.expansion:
            case (leaf, nonleaf):
                next_node = node_indexing[
                    nonleaf]
                edges[node][leaf].add(
                    next_node)
            case (leaf,):
                if leaf not in grammar.leafs:
                    raise AssertionError(leaf)
                edges[node][leaf].add(
                    accepting_node)
            case _:
                raise AssertionError(eq)
    # convert to `dict`
    edges = {
        node: dict(kv)
        for node, kv in
            edges.items()}
    return NFA(
        initial_node,
        accepting_nodes,
        edges)


def nfa_difference(
        graph:
            NFA,
        other_graph:
            NFA
        ) -> NFA:
    r"""Return language `expr \ other`."""
    p_nodes, p_edges = _difference_graph(
        graph, other_graph)
    p_accepting_nodes = set()
    for p_node in p_nodes:
        node, other_node = p_node
        is_accepting = (
            node in
                graph.accepting_nodes and
            other_node not in
                other_graph.accepting_nodes)
        if is_accepting:
            p_accepting_nodes.add(p_node)
    p_init = (
        graph.initial_node,
        other_graph.initial_node)
    return NFA(
        p_init, p_accepting_nodes,
        p_edges)


def _difference_graph(
        graph:
            NFA,
        other_graph:
            NFA
        ) -> tuple[
            set,
            dict]:
    """Return labeled-graph difference."""
    assert 0 not in graph.edges
    assert 0 not in other_graph.edges
    p_nodes = set()
    edges = set()
    # assert `other_graph` nonempty
    p_init = (
        graph.initial_node,
        other_graph.initial_node)
    todo = {p_init}
    while todo:
        pair = todo.pop()
        p_nodes.add(pair)
        node, other_node = pair
        more_nodes, more_edges = (
            _diff_next_nodes(
                node, other_node,
                graph, other_graph))
        todo |= more_nodes - p_nodes
        edges |= more_edges
    p_edges = _cl.defaultdict(
        lambda: _cl.defaultdict(set))
    for node, symbol, next_node in edges:
        p_edges[node][symbol].add(
            next_node)
    return (
        p_nodes,
        dict(p_edges))


def _diff_next_nodes(
        node,
        other_node,
        graph,
        other_graph
        ) -> set:
    """Return next nodes of difference."""
    assert 0 not in other_graph.edges
    pair = (node, other_node)
    out_edges = graph.edges[node]
    nodes = set()
    edges = set()
    for symbol, next_nodes in out_edges.items():
        has_next_node = (
            other_node in
                other_graph.edges and
            symbol in
                other_graph.edges[
                    other_node])
        if has_next_node:
            other_next_nodes = other_graph.edges[
                other_node][symbol]
        else:
            other_next_nodes = {0}
        for next_node in next_nodes:
            for other in other_next_nodes:
                next_pair = (next_node, other)
                nodes.add(next_pair)
                edge = (pair, symbol, next_pair)
                edges.add(edge)
    return (nodes, edges)


def nfa_intersection(
        graph:
            NFA,
        other_graph:
            NFA
        ) -> NFA:
    r"""Return language `expr \cap other`."""
    p_nodes, p_edges = _intersection_graph(
        graph, other_graph)
    p_accepting_nodes = set()
    for p_node in p_nodes:
        node, other_node = p_node
        is_accepting = (
            node in
                graph.accepting_nodes and
            other_node in
                other_graph.accepting_nodes)
        if is_accepting:
            p_accepting_nodes.add(p_node)
    p_init = (
        graph.initial_node,
        other_graph.initial_node)
    return NFA(
        p_init, p_accepting_nodes,
        p_edges)


def _intersection_graph(
        graph:
            NFA,
        other_graph:
            NFA
        ) -> tuple[
            set,
            dict]:
    """Return labeled-graph intersection."""
    p_nodes = set()
    edges = set()
    p_init = (
        graph.initial_node,
        other_graph.initial_node)
    todo = {p_init}
    while todo:
        pair = todo.pop()
        p_nodes.add(pair)
        node, other_node = pair
        symbols = set(
            graph.edges[node])
        symbols = symbols.intersection(
            other_graph.edges[other_node])
        for symbol in symbols:
            more_nodes, more_edges = (
                _product_next_nodes(
                    symbol, node, other_node,
                    graph, other_graph))
            todo |= more_nodes - p_nodes
            edges |= more_edges
    p_edges = _cl.defaultdict(
        lambda: _cl.defaultdict(set))
    for (node, symbol, next_node) in edges:
        p_edges[node][symbol].add(
            next_node)
    return (
        p_nodes,
        dict(p_edges))


def _product_next_nodes(
        symbol:
            str,
        node,
        other_node,
        graph:
            NFA,
        other_graph:
            NFA
        ) -> tuple[
            set,
            set]:
    """Return next nodes of intersection."""
    next_nodes = graph.edges[
        node][symbol]
    other_next_nodes = other_graph.edges[
        other_node][symbol]
    pair = (node, other_node)
    nodes = set()
    edges = set()
    for next_node in next_nodes:
        for other in other_next_nodes:
            next_pair = (next_node, other)
            nodes.add(next_pair)
            edge = (pair, symbol, next_pair)
            edges.add(edge)
    return (nodes, edges)


def is_empty_nfa(
        graph:
            NFA
        ) -> bool:
    """Return `True` if empty language."""
    if not graph.accepting_nodes:
        return True
    # reachability
    nodes = reachable_nodes(
        {graph.initial_node}, graph.edges)
    if nodes & graph.accepting_nodes:
        return False
    return True


def reachable_nodes(
        initial_nodes,
        edges:
            dict
        ) -> set:
    """Return nodes reachable from initial node."""
    nodes = set()
    todo = set(initial_nodes)
    while todo:
        node = todo.pop()
        nodes.add(node)
        nd_edges = edges.get(
            node, dict())
        more = set()
        for _, next_nodes in nd_edges.items():
            more.update(next_nodes)
        todo |= more - nodes
    return nodes


def is_regular_grammar(
        grammar:
            _grm.Grammar
        ) -> bool:
    r"""Return `True` if of a regular language.

    A grammar is regular when each production
    has one of the forms:

    - `nonleaf \supseteq leaf some_nonleaf`
    - `nonleaf \supseteq leaf`
    """
    for eq in grammar.equations:
        match eq.expansion:
            case a, b:
                if b not in grammar.nonleafs:
                    return False
            case a,:
                pass
            case _:
                return False
        if a not in grammar.leafs:
            return False
    return True


def grammar_to_regex(
        grammar:
            _grm.Grammar
        ) -> str:
    """Return regular expression for `grammar`.

    Asserts that `grammar` is regular.
    """
    if not is_regular_grammar(grammar):
        raise ValueError(
            '`grammar` need be regular')
    eq_repeated_leafs = _cl.defaultdict(set)
    eq_other = _cl.defaultdict(set)
    for eq in grammar.equations:
        symbol = eq.symbol
        match eq.expansion:
            case a, b:
                if b == symbol:
                    eq_repeated_leafs[
                        symbol].add(a)
                else:
                    eq_other[symbol].add(
                        eq.expansion)
            case a,:
                eq_other[symbol].add(
                    eq.expansion)
            case _:
                raise AssertionError(
                    'grammar need be regular')
    eq_repeated_leafs = dict(eq_repeated_leafs)
    eq_other = dict(eq_other)
    # _pp.pp(eq_repeated_leafs)
    # _pp.pp(eq_other)
    #
    # order the equations,
    # starting at the root symbol
    nonleafs = set(grammar.nonleafs)
    root_symbol = grammar.root_symbol
    nonleafs.remove(root_symbol)
    nonleafs = [root_symbol, *nonleafs]
    # print(nonleafs)
    #
    # substitute in ordered sequence
    end = len(nonleafs)
    for i, nonleaf in enumerate(nonleafs):
        others = eq_other[nonleaf]
        regex = _format_expansions_as_regex(
            others)
        repeated = eq_repeated_leafs.get(
            nonleaf, set())
        repeated_regex = _format_alternation(
            repeated)
        regex = (
            f'( ({repeated_regex})* ) & '
            f'({regex})')
        for j in range(i + 1, end):
            other = nonleafs[j]
            expansions = eq_other[other]
            eq_other[other] = _replace_nonleaf(
                nonleaf, regex, expansions)
    # _pp.pp(eq_other)
    #
    # solve and back-substitute,
    # starting from the end
    regex_solution = dict()
    end_to_start = range(
        end - 1, -1, -1)
    for i in end_to_start:
        nonleaf = nonleafs[i]
        repeated = set()
        for expansion in eq_other[nonleaf]:
            # print(expansion)
            if nonleaf in expansion:
                if nonleaf != expansion[1]:
                    raise AssertionError(
                        nonleaf, expansion)
                if nonleaf == expansion[0]:
                    raise AssertionError(
                        nonleaf, expansion)
                repeated.add(expansion[0])
        leafs = eq_repeated_leafs.get(
            nonleaf, set())
        repeated.update(leafs)
        if repeated:
            regex = _format_alternation(
                repeated)
            regex_1 = f'( ({regex})* )'
                # used `*` instead of `^*`
                # to enable lexing by the
                # basic lexer of this module
        else:
            regex_1 = ''
        eqs = eq_other[nonleaf]
        regex_2 = _format_expansions_as_regex(eqs)
        if regex_1:
            regex = f'({regex_1}) & ({regex_2})'
        else:
            regex = f'({regex_2})'
        # print(f'{nonleaf} = {regex}')
        regex_solution[nonleaf] = regex
        # back-substitute
        previous_nonleafs = range(
            i - 1, -1, -1)
        for j in previous_nonleafs:
            other = nonleafs[j]
            expansions = eq_other[other]
            eq_other[other] = _replace_nonleaf(
                nonleaf, regex, expansions)
    # _pp.pp(regex_solution)
    return regex_solution[
        root_symbol]


def _replace_nonleaf(
        nonleaf:
            str,
        regex:
            str,
        expansions:
            set
        ) -> set[
            tuple[str]]:
    """Return expansions with substitution.

    Replaces occurrences of `nonleaf` symbol
    with the regular expression `regex`.
    """
    def replace(
            symbol:
                str
            ) -> str:
        """Replace with `regex` if `nonleaf`."""
        if symbol == nonleaf:
            return regex
        return symbol
    exps = set()
    for expansion in expansions:
        expansion = tuple(map(
            replace, expansion))
        exps.add(expansion)
    return exps


def _format_expansions_as_regex(
        expansions:
            set[
                tuple[str]]
        ) -> str:
    """Return regex that is `|` of catenations."""
    catenations = list()
    for expansion in expansions:
        cat = ' & '.join(
            f'({sym})'
            for sym in expansion)
        catenations.append(cat)
    return _format_alternation(
        catenations)


def _format_alternation(
        alternatives:
            _abc.Iterable[
                str]
        ) -> str:
    """Return alternatives joined by pipe `|`."""
    return ' | '.join(
        f'({a})'
        for a in alternatives
        if a)
