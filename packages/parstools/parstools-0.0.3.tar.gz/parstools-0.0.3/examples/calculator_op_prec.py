"""Arithmetic calculator.

Operator parsing is defined by a table of
operator precedence.
"""
import os

import parstools


class Lexer(
        parstools.StatefulLexer):
    """Lexer of arithmetic."""

    t_NUMBER = r' \d+ '
    t_PLUS = r' \+ '
    t_MINUS = r' \- '
    t_ASTERISK = r' \* '
    t_DIV = r' / '
    t_omit = r' \s* '


class Parser:
    """Calculator of arithmetic operators."""

    def __init__(
            self
            ) -> None:
        self.root_symbol = 'expr'
        self._lexer = Lexer()
        self._parser = None
        self.operator_precedence = [
            ('left', 'PLUS', 'MINUS'),
            ('left', 'ASTERISK', 'DIV')]

    def parse(
            self,
            text:
                str
            ) -> int:
        """Evaluate expression."""
        if self._parser is None:
            path, _ = os.path.split(__file__)
            filename = 'calculator_parser_op_prec.json'
            cache_filepath = os.path.join(
                path, filename)
            self._parser = parstools.methods_to_parser(
                self,
                operator_precedence=self.operator_precedence,
                cache_filepath=cache_filepath)
        tokens = self._lexer.parse(text)
        return self._parser.parse(tokens)

    def p_plus(
            self, p):
        """expr: expr PLUS expr"""
        p[0] = p[1] + p[3]

    def p_diff(
            self, p):
        """expr: expr MINUS expr"""
        p[0] = p[1] - p[3]

    def p_product(
            self, p):
        """expr: expr ASTERISK expr"""
        p[0] = p[1] * p[3]

    def p_division(
            self, p):
        """expr: expr DIV expr"""
        p[0] = p[1] / p[3]

    def p_unary_minus(
            self, p):
        """expr: MINUS expr"""
        p[0] = - p[2]

    def p_number(
            self, p):
        """expr: NUMBER"""
        p[0] = int(p[1])


def _main():
    """Entry point."""
    parser = Parser()
    result = parser.parse('-1 + 2 * 3')
    result = result.value
    print(f'{result = }')


if __name__ == '__main__':
    _main()
