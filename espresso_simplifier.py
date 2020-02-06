import pyeda.inter as eda
import hashlib

class EspressoSimplifier:

    @staticmethod
    def simplify(expression):

        simplified_expr, = eda.espresso_exprs(eda.expr(expression).to_dnf())


        return EspressoSimplifier.convert(simplified_expr)

    @staticmethod
    def convert(expression):


        def is_digit(n):
            try:
                int(n)
                return True
            except ValueError:
                return False

        variables = expression.encode_inputs()[0].keys()
        expr = str(expression)

        print(expr)

        symbols = []
        for variable in variables:
            if not is_digit(str(variable)):
                symbols.append(str(variable))

        symbols.sort(key=len, reverse=True)
        print(symbols)

        for symbol in symbols:
            if symbol.find("~") is not -1:
                expr = expr.replace(symbol, "Not(" + symbol.replace("~", "") + ")")

        for symbol in symbols:
            symbol_hash = hashlib.sha224(symbol.encode('utf-8')).hexdigest()
            expr = expr.replace(symbol, "#(\'" + symbol_hash + "\')")

        for symbol in symbols:
            symbol_hash = hashlib.sha224(symbol.encode('utf-8')).hexdigest()
            expr = expr.replace(symbol_hash, symbol)

        expr = expr.replace("#", "Symbol")

        return expr
