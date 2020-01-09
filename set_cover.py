import dwave_qbsolv as qbs
import numpy as np


# import sympy
# from dwave.system.samplers import DWaveSampler #pip install dwave-ocean-sdk


def visualize_matrix(ising_instance, qubo_size):
    matrix = np.zeros((qubo_size, qubo_size))
    for i in range(qubo_size):
        for j in range(i, qubo_size):
            matrix[i][j] = ising_instance[(i, j)]
    print(matrix)
    return matrix


def complete_qubo_to_upper_diagonal(qubo):
    keys = qubo.keys()
    for (i, j), value in qubo.items():
        if i > j:
            if (j, i) in keys:
                qubo[(j, i)] += qubo[(i, j)]
                # del qubo[(i,j)]
                qubo[(i, j)] = 0.0
            else:
                qubo[(j, i)] = qubo[(i, j)]
                qubo[(i, j)] = 0.0
    return qubo


def generate_set_cover_qubo(input_sets, target_set, A=2, B=1):
    N = len(input_sets)
    n = len(target_set)
    target_set = list(target_set)

    #    s = 0
    #    for x in targetSet:
    #        for i in range(N):
    #            if x in inputSets[i]:
    #                s += 1

    qubo = {(i, j): 0.0 for i in range(N + N * n) for j in range(N + N * n)}
    for i in range(N):
        qubo[(i, i)] += B
    for alpha in range(n):
        for i in range(N):
            for j in range(N):
                qubo[((alpha + 1) * N + i, (alpha + 1) * N + j)] += A * (1 + (i + 1) * (j + 1))
                if i == j:
                    qubo[((alpha + 1) * N + i, (alpha + 1) * N + j)] += -2 * A
    for alpha in range(n):
        for i in range(N):
            if target_set[alpha] in input_sets[i]:
                for m in range(N):
                    qubo[(i, (alpha + 1) * N + m)] += -2 * (m + 1) * A
    for alpha in range(n):
        for i in range(N):
            for j in range(N):
                if (target_set[alpha] in input_sets[i]) and (target_set[alpha] in input_sets[j]):
                    qubo[(i, j)] += A
    qubo = complete_qubo_to_upper_diagonal(qubo)
    return qubo


def generate_qubo_specialized_set_cover(input_sets, target_set):
    actual_considered_input_sets = []
    for s in input_sets:
        if s.issubset(target_set) or s == target_set:
            actual_considered_input_sets.append(s)
    qubo = generate_set_cover_qubo(actual_considered_input_sets, target_set)
    return qubo


def solve_specialized_set_cover(input_sets, target_set):
    qubo = generate_qubo_specialized_set_cover(input_sets, target_set)

    actual_considered_input_sets = []
    for s in input_sets:
        if s.issubset(target_set):
            actual_considered_input_sets.append(s)
    #    N = len(actualConsideredInputSets)
    #    n = len(targetSet)
    #    print(N + N*n)
    #    print(actualConsideredInputSets)
    #    visualizeMatrix(qubo, N + N*n)

    qbsolv_params = dict(num_repeats=10, verbosity=-1)
    solutions = list(qbs.QBSolv().sample_qubo(qubo, **qbsolv_params).samples())
    solution_list = []
    for sol in solutions:
        temp = []
        for i in range(max(sol.keys()) + 1):
            temp.append(sol[i])
        solution_list.append(temp)
    # print(solution_list)
    potential_solutions = []
    for sol in solution_list:
        temp = []
        for i in range(len(actual_considered_input_sets)):
            if sol[i] == 1:
                temp.append(actual_considered_input_sets[i])
        potential_solutions.append(temp)
    # print("potential_solutions", potential_solutions)
    potential_solutions.sort(key=lambda x: len(x))
    for pot_sol in potential_solutions:
        total_set = set([])
        for s in pot_sol:
            total_set = total_set.union(s)
        if target_set == total_set:
            return pot_sol
    # print("We could not find a Solution")
    return -1


def sets_from_str(string):

    sets = []
    for s in string.split('|'):
        new_s = set()
        for element in s.split():
            new_s.add(int(element))
        sets.append(new_s)

    return sets


def sets_to_str(sets):
    string = ''
    for s in sets:
        for element in s:
            string += str(element)
            string += ' '
        string += '|'

    return string[:-1]


def solve_specialized_set_cover_str(input_sets_str, target_sets_str):
    input_sets = sets_from_str(input_sets_str)
    target_set = sets_from_str(target_sets_str)[0]

    print("---------------")

    print(target_set)
    print(input_sets)

    print("---------------")

    res = -1
    while res is -1:
        print("Try to solve...")
        res = solve_specialized_set_cover(input_sets, target_set)
    print("Success!")

    return sets_to_str(res)
    #if res is not -1:
    #    return sets_to_str(res)
    #else:
    #    return ''


# x = sympy.symbols("x0:6")
# print(x)
# formula_1 = 2*((1- x[2] -x[3])**2 + ( 1 - x[4] - x[5])**2)
# formula_2 = 2*((x[2]+2*x[3] - x[0] -x[1])**2 + (x[4] + 2*x[5]-x[0])**2)
# formula_3 = sympy.expand(formula_1 + formula_2 + x[0]+x[1])
# #formula_3 = sympy.expand(formula_1)
# formula_3 = formula_3.subs({y**2:y for y in x})
# print(formula_3)
