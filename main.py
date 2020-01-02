import simplifier as simp

# expression = '(~a1 & ~b & ~c) | ~a1 & ~b & c | a1 & ~b & c | a1 & b & c | a1 & b & ~c'
expression = '(s5 | (s1 & ~(s3) & ~(s4)) | (~(s3) & ~(s4) & s2))'
#' s1 & ~s3 & ~s4 | s2 & ~s3 & ~s4 | s5'

print(simp.simplify(expression, 'espresso'))
print(simp.simplify(expression, 'sympy_todnf'))
print(simp.simplify(expression, 'sympy_symplifylogic'))



