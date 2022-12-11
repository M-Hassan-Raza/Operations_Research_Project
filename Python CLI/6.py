from pulp import *
import sys
import matplotlib.pyplot as plt
import numpy as np

prob = LpProblem("Question_6", LpMinimize)

x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)

prob += 51*x1 + 9*x2 + 1*x3 + 8*x4

prob += 692*x1 + 110*x2 + 81*x3 + 150*x4 >= 1410
prob += 692*x1 + 110*x2 + 81*x3 + 150*x4 <= 1610
prob += 57*x1 + 6*x2 + 1*x3  + 8*x4 >= 85
prob += 1*x2 + 22*x3 + 12*x4 >= 25


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

