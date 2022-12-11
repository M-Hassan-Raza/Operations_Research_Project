from pulp import *
import sys

prob = LpProblem("Question_5", LpMaximize)

x1 = LpVariable("x1",120)
x2 = LpVariable("x2",120)
x3 = LpVariable("x3",120)

prob += 6.50*x1 + 9.00*x2 + 10.00*x3

prob += 3*x1 + 4*x2 + 6*x3 <= 2700
prob += 55*x1 + 75*x2 + 95*x3 <= 48000
prob += 3*x1 + 5*x2 + 6*x3 <= 3000
prob += 5*x1 + 6*x2 + 8*x3 <= 12000

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