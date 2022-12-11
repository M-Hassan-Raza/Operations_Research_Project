from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_3", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)
x5 = LpVariable("x5",0)

prob += 400*x1 + 560*x2+ 560*x3 + 700*x4

prob += 25*x1 + 46*x2 + 16*x3 + 34*x4 <= 2500
prob += 50*x1 + 30*x2 + 28*x3 + 12*x4 <= 2800
prob += 1*x1 + 1*x2 >= 20
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 - 1*x5 == 0
prob += 1*x2 + 1*x4 - 0.50*x5 >= 0
prob += 1*x1 + 1*x2 - 0.75*x5 <= 0
prob += 1*x3 + 1*x4 - 0.75*x5 <= 0


prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))