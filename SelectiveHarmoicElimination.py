from sympy import *
import numpy as np


def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n * multiplier) / multiplier

alp1,alp2,alp3,alp4,alp5,alp6= symbols('alp1 alp2 alp3 alp4 alp5 alp6')
#########################################################################
vars=[alp1,alp2,alp3,alp4,alp5,alp6]
varsCopy = np.array([20,30,40,50,60,70])*(3.14/180)

for i in range(len(varsCopy)):
    varsCopy[i] = truncate(varsCopy[i],7)
##########################################################################

vd = 200
Vdesired = 200
f1 = (2*vd/pi)*(1-2*cos(alp1)+2*cos(alp2)-2*cos(alp3)+2*cos(alp4)-2*cos(alp5)+2*cos(alp6))-Vdesired
f2 = (2*vd/5*pi)*(1-2*cos(5*alp1)+2*cos(5*alp2)-2*cos(5*alp3)+2*cos(5*alp4)-2*cos(5*alp5)+2*cos(5*alp6))
f3 = (2*vd/7*pi)*(1-2*cos(7*alp1)+2*cos(7*alp2)-2*cos(7*alp3)+2*cos(7*alp4)-2*cos(7*alp5)+2*cos(7*alp6))
f4 = (2*vd/9*pi)*(1-2*cos(9*alp1)+2*cos(9*alp2)-2*cos(9*alp3)+2*cos(9*alp4)-2*cos(9*alp5)+2*cos(9*alp6))
f5 = (2*vd/11*pi)*(1-2*cos(11*alp1)+2*cos(11*alp2)-2*cos(11*alp3)+2*cos(11*alp4)-2*cos(11*alp5)+2*cos(11*alp6))
f6 = (2*vd/13*pi)*(1-2*cos(13*alp1)+2*cos(13*alp2)-2*cos(13*alp3)+2*cos(13*alp4)-2*cos(13*alp5)+2*cos(13*alp6))

functions = [f1,f2,f3,f4,f5,f6]
functionsCopy = [0,0,0,0,0,0]

result =np.array([[0] * len(vars) for i in range(len(functions))])
resultINV = np.array([[0] * len(vars) for i in range(len(functions))])


def jacobian(vars,functions):
    J =[[0] * len(vars) for i in range(len(functions))]
    print(J)
    for i, fi in enumerate(functions):
        for j, s in enumerate(vars):
            J[i][j] = diff(fi, s)
    return J

def subsJ():
    for i in range(len(vars)):
        for j in range(len(vars)):
            result[i][j] = float((jacobian(vars,functions)[i][j].subs([(alp1,varsCopy[0]),(alp2,varsCopy[1]),(alp3,varsCopy[2]),(alp4,varsCopy[3]),(alp5,varsCopy[4]),(alp6,varsCopy[5])])))
    #return result

def subs():
    for i in range(len(functions)):
        functionsCopy[i] = float(functions[i].subs([(alp1,varsCopy[0]),(alp2,varsCopy[1]),(alp3,varsCopy[2]),(alp4,varsCopy[3]),(alp5,varsCopy[4]),(alp6,varsCopy[5])]))
        
    #return functionsCopy

def iteration():
    subsJ()
    subs()
    resultINV = np.linalg.inv(result)
    x = varsCopy - resultINV @ functionsCopy
    return  x

for i in range(3):
    varscopy = iteration()
    
print(varscopy*(180/3.14))

             

