from pulp import *
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_1", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)

prob += 27*x1 +32*x2 +38*x3 +51*x4

prob += 1*x1 + 1*x3 >= 200
prob += 1*x2 + 1*x4 >= 200
prob += 12*x1 + 12*x2 + 9*x3 + 9*x4 <= 4800
prob += 6*x1 + 9*x2 + 12*x3 + 18*x4 <= 4800
prob += 2*x1 + 2*x2 <= 500
prob += 2*x3 + 2*x4 <= 800

prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))