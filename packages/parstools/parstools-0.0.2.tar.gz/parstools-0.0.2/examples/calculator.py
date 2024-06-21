"""Arithmetic calculator."""
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

    def parse(
            self,
            text:
                str
            ) -> int:
        """Evaluate expression."""
        if self._parser is None:
            path, _ = os.path.split(__file__)
            filename = 'calculator_parser.json'
            cache_filepath = os.path.join(
                path, filename)
            self._parser = parstools.methods_to_parser(
                self,
                cache_filepath=cache_filepath)
        tokens = self._lexer.parse(text)
        return self._parser.parse(tokens)

    def p_expr_append(
            self, p):
        """expr: expr PLUS diff"""
        p[0] = p[1] + p[3]

    def p_expr_start(
            self, p):
        """expr: diff"""
        p[0] = p[1]

    def p_diff_append(
            self, p):
        """diff: diff MINUS product"""
        p[0] = p[1] - p[3]

    def p_diff_start(
            self, p):
        """diff: product"""
        p[0] = p[1]

    def p_product_append(
            self, p):
        """product: product ASTERISK div"""
        p[0] = p[1] * p[3]

    def p_product_start(
            self, p):
        """product: div"""
        p[0] = p[1]

    def p_div_append(
            self, p):
        """div: div DIV number"""
        p[0] = p[1] / p[3]

    def p_div_start(
            self, p):
        """div: number"""
        p[0] = p[1]

    def p_number(
            self, p):
        """number: NUMBER"""
        p[0] = int(p[1])


def _main():
    """Entry point."""
    parser = Parser()
    result = parser.parse('1 + 2 * 3')
    result = result.value
    print(f'{result = }')


if __name__ == '__main__':
    _main()
