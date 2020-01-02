import espresso_simplifier as es
import sympy_simplifier as sy


def simplify(expression, simplifier):

    if simplifier == 'espresso':
        return es.EspressoSimplifier.simplify(expression)
    elif simplifier == 'sympy_todnf':
        return sy.ToDNFSimplifier.simplify(expression)
    elif simplifier == 'sympy_symplifylogic':
        return sy.ToDNFSimplifier.simplify(expression)
    else:
        return None

