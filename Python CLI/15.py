from pulp import*
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_15", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)

prob += 622*x1 + 690*x2 + 231*x3 + 684*x4

prob += 4*x1 + 5*x2 + 3*x3 + 10*x4 <= 1800
prob += 50*x1 + 75*x2 + 30*x3 + 60*x4 <= 25000
prob += 2*x1 + 6*x2 + 1*x3 + 4*x4 <= 1200
prob += 210*x1 >= 30000
prob += 300*x2 >= 30000
prob += 180*x3 <= 25000
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 <= 300

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