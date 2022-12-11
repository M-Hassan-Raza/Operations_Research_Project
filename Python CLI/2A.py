from pulp import *
import sys

prob = LpProblem("Question_2A", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)
x5 = LpVariable("x5",0)

prob += 110*x1 + 90*x2 + 75*x3 + 80*x4 + 130*x5

prob += 5.5*x1 + 5.2*x2 + 5.0*x3 + 5.1*x4 + 7.5*x5 <= 4800
prob += 4.5*x1 <= 1200
prob += 4.5*x2 +4.0*x3 + 3.0*x4 <= 2400
prob += 9.0*x5 <= 1200
prob += 4.0*x1 + 3.0*x2 + 2.5*x3 + 2.0*x4 + 4.0*x5 <= 3000

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