from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_7", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)

prob += 70*x1 + 80*x2 + 130*x3 + 150*x4

prob += 1*x3 >= 100, "1st constraint"
prob += 0.4*x1 + 0.5*x2 + 0.6*x3 + 0.8*x4 <= 750, "2nd constraint"
prob += 1*x1 + 1*x3 <= 700, "3rd constraint"
prob += 1*x2 + 1*x4 <= 550, "4th constraint"
prob += 1*x1 + 1*x2 + 1*x3  <= 800, "5th constraint"
prob += 1*x4 <= 950, "6th constraint"
prob += 1*x1 + 1*x2 + 2*x3 + 1*x4 <= 1600, "7th constraint"
prob += 1*x1 + 1*x2 + 1*x4 <= 1000, "8th constraint"
prob += 1*x1 + 1*x3 + 1*x4 <= 1600, "9th constraint"
prob += 1*x2 + 1*x3 + 1*x4 <= 900, "10th constraint"
prob += 1*x1 + 1*x2 <= 850, "11th constraint"
prob += 1*x3 + 1*x4 <= 800, "12th constraint"
prob += 1*x2 + 1*x3 <= 1250, "13th constraint"
prob += 1*x1 + 1*x4 <= 750, "14th constraint"

prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))