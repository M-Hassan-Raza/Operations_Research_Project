from pulp import *
import sys

prob = LpProblem("Question_7", LpMaximize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)

prob += 70*x1 + 80*x2 + 130*x3 + 150*x4

prob += 1*x3 >= 100
prob += 0.4*x1 + 0.5*x2 + 0.6*x3 + 0.8*x4 <= 750
prob += 1*x1 + 1*x3 <= 700
prob += 1*x2 + 1*x4 <= 550
prob += 1*x1 + 1*x2 + 1*x3  <= 800
prob += 1*x4 <= 950
prob += 1*x1 + 1*x2 + 2*x3 + 1*x4 <= 1600
prob += 1*x1 + 1*x2 + 1*x4 <= 1000
prob += 1*x1 + 1*x3 + 1*x4 <= 1600
prob += 1*x2 + 1*x3 + 1*x4 <= 900
prob += 1*x1 + 1*x2 <= 850
prob += 1*x3 + 1*x4 <= 800
prob += 1*x2 + 1*x3 <= 1250
prob += 1*x1 + 1*x4 <= 750

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