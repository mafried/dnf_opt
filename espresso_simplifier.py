import pyeda.inter as eda


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

        symbols = []
        for variable in variables:
            if not is_digit(str(variable)):
                symbols.append(str(variable))


        for symbol in symbols:
            if symbol.find("~") is not -1:
                expr = expr.replace(symbol, "Not(" + symbol.replace("~", "") + ")")

        for symbol in symbols:
            expr = expr.replace(symbol, "#(\'" + symbol + "\')")

        expr = expr.replace("#", "Symbol")

        return expr
