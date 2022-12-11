from pulp import *
import sys

prob = LpProblem("Question_11", LpMinimize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)

prob += 140*x1 + 50*x2 + 36*x3

prob += 100*x1 + 35*x2 + 27*x3 >= 2000000
prob += 1*x1 >= 5000
prob += 1*x2 >= 4000
prob += 1*x3 >= 2300
prob += 1*x1 <= 15000
prob += 1*x2 <= 15000
prob += 1*x3 <= 15000

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

print("Optimal Value: ", round(value(prob.objective), 4))
print ("\nSensitivity Analysis\nConstraint\t\t\t\tShadow Price\t\t\t\tSlack")
for name, c in prob.constraints.items():
    print (name, "\t\t\t\t\t", round(c.pi, 3), "\t\t\t\t\t\t", round(c.slack, 5))