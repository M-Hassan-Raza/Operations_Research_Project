from pulp import *
import sys

prob = LpProblem("Question_10", LpMinimize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)
x5 = LpVariable("x5",0)

prob += 12*x1 + 9*x2 + 9*x3 + 15*x4

prob += 30*x1 + 30*x2 + 20*x3 + 20*x4 >= 50
prob += 25*x1 + 2*x2 + 100*x3 + 25*x4 >= 50
prob += 25*x1 + 25*x2 + 25*x3 + 25*x4 >= 50
prob += 25*x1 + 25*x2 + 100*x3 + 25*x4 >= 50
prob += 45*x1 + 45*x2 + 100*x3 + 25*x4 >= 50
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 - 1*x5 == 0
prob += 1*x1 - 0.1*x5 >= 0
prob += 1*x2 - 0.1*x5 >= 0
prob += 1*x3 - 0.1*x5 >= 0
prob += 1*x4 - 0.1*x5 >= 0

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
    print(v.name, "=" , round(v.varValue, 3), "\tReduced Cost =", round(v.dj, 3))

print("Optimal Value: ", value(prob.objective))
print ("\nSensitivity Analysis\nConstraint\t\t\t\tShadow Price\t\t\t\tSlack")
for name, c in prob.constraints.items():
    print (name, "\t\t\t\t\t", round(c.pi, 3), "\t\t\t\t\t\t", round(c.slack, 5))

