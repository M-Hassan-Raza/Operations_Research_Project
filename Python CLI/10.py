from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_10", LpMinimize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)
x5 = LpVariable("x5",0)

prob += 12*x1 + 9*x2 + 9*x3 + 15*x4

prob += 30*x1 + 30*x2 + 20*x3 + 20*x4 >= 50
prob += 25*x1 + 2*x2 + 100*x3 + 25*x4 >= 50
prob += 25*x1 + 25*x2 + 25*x3 + 25*x4 >= 50
prob += 25*x1 + 25*x2 + 100*x3 + 25*x4 >= 50
prob += 45*x1 + 45*x2 + 100*x3 + 25*x4 >= 50
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 - 1*x5 == 0
prob += 1*x1 - 0.1*x5 >= 0
prob += 1*x2 - 0.1*x5 >= 0
prob += 1*x3 - 0.1*x5 >= 0
prob += 1*x4 - 0.1*x5 >= 0

prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))

