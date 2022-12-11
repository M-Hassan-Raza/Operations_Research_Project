from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Simple_Lp_Problem", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)
x5 = LpVariable("x5",0)
x6 = LpVariable("x6",0)
x7 = LpVariable("x7",0)

prob += 0.0775*x1 + 0.1125*x2 + 0.1425*x3 + 0.9875*x4 + 0.0445*x5

prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 + 1*x5 == 68000000
prob += 1*x5 >= 5000000
prob += 1*x1 + 1*x2 + 1*x3 + -1*x6 == 0
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 - 1*x7 == 0
prob += 1*x6 - 0.8*x7 >= 0
prob += 1*x1 -0.6*x6 >= 0
prob += 4*x1 + 6*x2 + 9*x3 + 3*x4 <= 340000000

prob.solve()
for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))

