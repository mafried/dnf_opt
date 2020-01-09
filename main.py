import simplifier as simp
import set_cover as sc

# expression = '(~a1 & ~b & ~c) | ~a1 & ~b & c | a1 & ~b & c | a1 & b & c | a1 & b & ~c'
expression = '(s5 | (s1 & ~(s3) & ~(s4)) | (~(s3) & ~(s4) & s2))'
#' s1 & ~s3 & ~s4 | s2 & ~s3 & ~s4 | s5'

print(simp.simplify(expression, 'espresso'))
print(simp.simplify(expression, 'sympy_todnf'))
print(simp.simplify(expression, 'sympy_symplifylogic'))

#print(sc.solve_specialized_set_cover([{2, 4}, {1, 3, 4}, {0, 3}], {0, 1, 2, 3, 4}))

print(sc.solve_specialized_set_cover_str('2 4 | 1 3 4 | 0 3', '0 1 2 3 4'))


