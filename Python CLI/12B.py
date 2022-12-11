from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_12B", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)

prob += 2.50*x1 + 3.25*x2 + 3.90*x3

prob += 10*x1 + 15*x2 + 20*x3 <= 5760
prob += 1*x2 >= 150
prob += -2*x1 - 2*x2 + 1*x3 <= 0
prob += 1*x1 + 1*x2 + 1*x3 - 1*x4 == 0
prob += 1*x1 - 0.3*x4 <= 0

prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))


