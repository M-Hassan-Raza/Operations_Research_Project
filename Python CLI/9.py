from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_9", LpMinimize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)
x5 = LpVariable("x5",0)
x6 = LpVariable("x6",0)
x7 = LpVariable("x7",0)
x8 = LpVariable("x8",0)

prob += 15*x1 + 12*x2 + 20*x3 + 18*x4 + 35*x5 + 30*x6 + 50*x7 + 40*x8

prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 + 1*x5 + 1*x6 + 1*x7 + 1*x8 == 2000, "1st constraint"
prob += 1*x1 + 1*x2 + 1*x5 + 1*x6 >= 1000, "2nd constraint"
prob += 1*x5 + 1*x6 + 1*x7 + 1*x8 >= 500, "3rd constraint"
prob += -0.5*x1 + 0.5*x5 >= 0, "4th constraint"
prob += 1*x2 + 1*x4 + 1*x6 + 1*x8 <= 800, "5th constraint"
prob += -0.25*x2 - 0.25*x4 + 0.75*x6 + 0.75*x8 <= 0, "6th constraint"
prob += 1*x1 + 1*x5 >= 200, "7th constraint"
prob += 1*x2 + 1*x6 >= 200 , "8th constraint"
prob += 1*x3 + 1*x7 >= 200 , "9th constraint"
prob += 1*x4 + 1*x8 >= 200 , "10th constraint"
prob += 1*x1 + 1*x5 <= 1000 , "11th constraint"
prob += 1*x2 + 1*x6 <= 1000, "12th constraint"
prob += 1*x3 + 1*x7 <= 1000, "13th constraint"
prob += 1*x4 + 1*x8 <= 1000 , "14th constraint"

prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))