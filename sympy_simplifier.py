import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from sympy.printing.repr import srepr


class ToDNFSimplifier:

    @staticmethod
    def simplify(expression):
        simplified_expr = sp.to_dnf(parse_expr(expression, evaluate=False), True)
        return srepr(simplified_expr)


class SimplifyLogicSimplifier:

    @staticmethod
    def simplify(expression):
        simplified_expr = sp.simplify_logic(parse_expr(expression, evaluate=False))
        return srepr(simplified_expr)
