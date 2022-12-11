from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_5", LpMaximize)

x1 = LpVariable("x1",120)
x2 = LpVariable("x2",120)
x3 = LpVariable("x3",120)

prob += 6.50*x1 + 9.00*x2 + 10.00*x3

prob += 3*x1 + 4*x2 + 6*x3 <= 2700, "1st constraint"
prob += 55*x1 + 75*x2 + 95*x3 <= 48000, "2nd constraint"
prob += 3*x1 + 5*x2 + 6*x3 <= 3000, "3rd constraint"
prob += 5*x1 + 6*x2 + 8*x3 <= 12000, "4th constraint"

prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))