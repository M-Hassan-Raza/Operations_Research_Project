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

result = prob.solve()

if result == 1:
    print('Problem Status: ', LpStatus[prob.status])
elif result == 0:
    print('Problem Status: ', LpStatus[prob.status])
    sys.exit()
elif result == -1:
    print('Problem Status: ', LpStatus[prob.status])
    sys.exit()
elif result == -2:
    print('Problem Status: ', LpStatus[prob.status])
    sys.exit()
elif result == -3:
    print('Problem Status: ', LpStatus[prob.status])
    sys.exit()

for v in prob.variables():
    print(v.name, "=" , v.varValue, "\tReduced Cost =", v.dj)

print("Optimal Value: ", value(prob.objective))

print ("\nSensitivity Analysis\nConstraint\t\t\t\tShadow Price\t\t\t\tSlack")
for name, c in prob.constraints.items():
    print (name, "\t\t\t\t\t", round(c.pi, 3), "\t\t\t\t\t\t", round(c.slack, 5))