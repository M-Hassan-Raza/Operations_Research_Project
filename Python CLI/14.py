from pulp import *
import sys

prob = LpProblem("Question_14", LpMinimize)

XJR = LpVariable("cabinets produced in regular in July", 0, None, LpContinuous)
XJO = LpVariable("cabinets produced in overtime in July", 0, None, LpContinuous)
XAR = LpVariable("cabinets produced in regular time in August", 0, None, LpContinuous)
XAO = LpVariable("cabinets produced in overtime in August", 0, None, LpContinuous)
XSR = LpVariable("cabinets produced in regular time in September", 0, None, LpContinuous)
XSO = LpVariable("cabinets produced in overtime in September", 0, None, LpContinuous)
YJR = LpVariable("Mobile home cabinets produced in regular time in July", 0, None, LpContinuous)
YJO = LpVariable("Mobile home cabinets produced in overtime in July", 0, None, LpContinuous)
YAR = LpVariable("Mobile home cabinets produced in regular time in August", 0, None, LpContinuous)
YAO = LpVariable("Mobile home cabinets produced in overtime in August", 0, None, LpContinuous)
YSR = LpVariable("Mobile home cabinets produced in regular time in September", 0, None, LpContinuous)
YSO = LpVariable("Mobile home cabinets produced in overtime in September", 0, None, LpContinuous)
SJ = LpVariable("Motor home cabinets stored in July", 0, None, LpContinuous)
SA = LpVariable("Motor home cabinets stored in August", 0, None, LpContinuous)
SS = LpVariable("Motor home cabinets stored in September", 0, None, LpContinuous)
TJ = LpVariable("Mobile home cabinets stored in July", 0, None, LpContinuous)
TA = LpVariable("Mobile home cabinets stored in August", 0, None, LpContinuous)
TS = LpVariable("Mobile home cabinets stored in September", 0, None, LpContinuous)

prob += 188*XJR + 209*XJO + 194*XAR + 218*XAO + 200*XSR + 227*XSO + 280*YJR + 315*YJO + 290*YAR + 330*YAO + 300*YSR + 345*YSO + 6*SJ + 6*SA + 6*SS + 9*TJ + 9*TA + 9*TS

prob += XJR + XJO - SJ == 225
prob += XAR + XAO + SJ - SA == 250
prob += SA + XSR + XSO - SS == 150
prob += YJR + YJO - TJ == 80
prob += TJ + YAR + YAO - TA == 300
prob += TA + YSR + YSO - TS == 400
prob += SS >= 10
prob += TS >= 25
prob += SJ + TJ <= 300
prob += SA + TA <= 300
prob += SS + TS <= 300
prob += 3*XJR + 5*YJR <= 2100
prob += 3*XAR + 5*YAR <= 1500
prob += 3*XSR + 5*YSR <= 1200
prob += 3*XJO + 5*YJO <= 1050
prob += 3*XAO + 5*YAO <= 750
prob += 3*XSO + 5*YSO <= 600

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
    print(v.name, "=", v.varValue)

print("Optimal Value: ", value(prob.objective))
print ("\nSensitivity Analysis\nConstraint\t\t\t\tShadow Price\t\t\t\tSlack")
for name, c in prob.constraints.items():
    print (name, "\t\t\t\t\t", round(c.pi, 3), "\t\t\t\t\t\t", round(c.slack, 5))



