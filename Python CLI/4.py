from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_4", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)
x5 = LpVariable("x5",0)
x6 = LpVariable("x6",0)
x7 = LpVariable("x7",0)

prob += 0.15*x1 + 0.12*x2 + 0.09*x3 + 0.11*x4 + 0.085*x5 + 0.06*x6

prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 + 1*x5 + 1*x6 == 50000, "1st constraint"
prob += 1*x6 >= 10000, "2nd constraint"
prob += 1*x1 + 1*x2 + 1*x3 - 1*x7 == 0, "3rd constraint"
prob += 1*x3 - .25*x7 >= 0, "4th constraint"
prob += 1*x4 + 1*x5 - 1*x7 >= 0, "5th constraint"
prob += 1*x3 + 1*x5 + 1*x6 <= 12500, "6th constraint"

prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))