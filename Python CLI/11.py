from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_11", LpMinimize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)

prob += 140*x1 + 50*x2 + 36*x3

prob += 100*x1 + 35*x2 + 27*x3 >= 2000000
prob += 1*x1 >= 5000
prob += 1*x2 >= 4000
prob += 1*x3 >= 2300
prob += 1*x1 <= 15000
prob += 1*x2 <= 15000
prob += 1*x3 <= 15000

prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))