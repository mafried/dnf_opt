import simplifier as simp
import set_cover as sc

# expression = '(~a1 & ~b & ~c) | ~a1 & ~b & c | a1 & ~b & c | a1 & b & c | a1 & b & ~c'
# expression = '(s5 | (s1 & ~(s3) & ~(s4)) | (~(s3) & ~(s4) & s2))'
#expression = '(((s1 | s2) & ~ (s3 | s4)) | s5)'

expression = '((((cube_0 & ~ cube_1) | ((cube_2 | (cube_3 | (cube_4 | cube_5))) & ~ cube_6)) | ((cube_7 & ~ cube_8) | ((cube_9 | (cube_10 | (cube_11 | cube_12))) & ~ cube_13))) | (((cube_18 & ~ cube_19) | ((cube_20 | (cube_21 | (cube_22 | cube_23))) & ~ cube_24)) | ((cube_25 & ~ cube_26) | ((cube_27 | (cube_28 | (cube_29 | cube_30))) & ~ cube_31))))'

#' s1 & ~s3 & ~s4 | s2 & ~s3 & ~s4 | s5'

print('Espresso:' + str()+ simp.simplify(expression, 'espresso'))
print('SymPy:' + simp.simplify(expression, 'sympy_todnf'))
print('SymPy:' + simp.simplify(expression, 'sympy_symplifylogic'))

#print(sc.solve_specialized_set_cover([{2, 4}, {1, 3, 4}, {0, 3}], {0, 1, 2, 3, 4}))

print(sc.solve_specialized_set_cover_str('2 4 | 1 3 4 | 0 3', '0 1 2 3 4'))


