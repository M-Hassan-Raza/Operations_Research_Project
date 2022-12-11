from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_8", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)

prob += 800*x1 + 900*x2 + 600*x3

prob += 1*x1 + 1*x2 + 1*x3 <= 7
prob += 2*x1 + 1*x2 + 1*x3 <= 8
prob += 80*x1 + 160*x2 + 80*x3 <= 480

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
    print(v.name, "=" , v.varValue)

print("Optimal Value: ", value(prob.objective))
print ("\nSensitivity Analysis\nConstraint\t\t\t\tShadow Price\t\t\t\tSlack")
for name, c in prob.constraints.items():
    print (name, "\t\t\t\t\t", round(c.pi, 3), "\t\t\t\t\t\t", round(c.slack, 5))