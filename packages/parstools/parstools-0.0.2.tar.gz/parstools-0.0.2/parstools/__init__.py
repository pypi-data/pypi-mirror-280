"""Parsing algorithms."""
import typing as _ty

import parstools._grammars as _grm
import parstools._introspection as _intro
import parstools._lex as _lex
import parstools._lr.lr as _lrk
import parstools._lr.lr_merging_opt as _lrm
import parstools._lr.parser as _p
import parstools._re as _re


__version__: _ty.Final[
    str |
    None]
try:
    import parstools._version as _version
    __version__ = getattr(
        _version, 'version', None)
except ImportError:
    __version__ = None


# regular languages
match_regex = _re.match_regex
lex_regex = _re.lex_regex
parse_regex = _re.parse_regex
regex_to_nfa = _re.regex_to_nfa
grammar_to_regex = _re.grammar_to_regex
nfa_difference = _re.nfa_difference
nfa_intersection = _re.nfa_intersection
# lexing
Lexer = _lex.Lexer
StatefulLexer = _lex.StatefulLexer
lex_delimited = _lex.lex_delimited
add_row_column = _lex.add_row_column
join_tokens = _lex.join_tokens
# grammars
Production = _grm.Production
Grammar = _grm.Grammar
is_regular_grammar = _re.is_regular_grammar
# LR parsing
make_lr_parser = _lrk.make_parser
grammar_to_parser = _lrm.make_parser
methods_to_parser = _intro.make_parser
# printing
print_parser = _p.print_parser
dump_parser_pdf = _p.dump_parser_pdf
