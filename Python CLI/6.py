from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_6", LpMinimize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)

prob += 51*x1 + 9*x2 + 1*x3 + 8*x4

prob += 692*x1 + 110*x2 + 81*x3 + 150*x4 >= 1410, "1st constraint"
prob += 692*x1 + 110*x2 + 81*x3 + 150*x4 <= 1610, "2nd constraint"
prob += 57*x1 + 6*x2 + 1*x3  + 8*x4 >= 85, "3rd constraint"
prob += 1*x2 + 22*x3 + 12*x4 >= 25, "4th constraint"


prob.solve()

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))

