from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_12A", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)

prob += 2.50*x1 + 3.25*x2 + 3.90*x3

prob += 2*x1 + 3*x2 + 6*x3 <= 1920, "1st constraint"
prob += 8*x1 + 12*x2 + 14*x3 <= 3840, "2nd constraint"
prob += 1*x2 >= 150, "3rd constraint"
prob += -2*x1 - 2*x2 + 1*x3 <= 0 , "4th constraint"
prob += 1*x1 + 1*x2 + 1*x3 - 1*x4 == 0 , "5th constraint"
prob += 1*x1 - 0.3*x4 <= 0, "6th constraint"

prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))

