appliesTo = ("volume",)
from sympy import *
import differentiation

import random

#Simple program for finding area/volume/etc bounded between two curves in the first quadrant
#I'm only using the first quadrant & simple polynomials because this gets complicated real fast if you don't: and that takes effort
def generate(lower, upper):
    x = symbols('x')
    precision = 5
    c = random.randint(1,10)
    b = random.randint(1,10)
    g = random.randint(0,5)
    functionOne = c*x+g
    functionTwo = b*x**2
    intercepts = solve(functionOne-functionTwo,x)
    boundVal = 0
    if(intercepts[0] > 0):
        boundVal = intercepts[0]
    else:
        boundVal = intercepts[1]

    boundVal = N(boundVal,precision)
    
    area = integrate(functionOne-functionTwo, (x,0,boundVal))

    volumeX = N(pi,precision)*integrate(functionOne**2-functionTwo**2, (x,0,boundVal))

    volumeSquareBase = integrate((functionOne-functionTwo)**2, (x,0,boundVal))

    verticalAxis = random.randint(-4,0)
    #print(verticalAxis)
    #print(functionOne, functionTwo)
    volumeShell = 2*N(pi,precision)*integrate((x-verticalAxis)*(functionOne-functionTwo), (x,0,boundVal))
    #print(volumeShell)
    payload = []

    output = dict()
    output["header"] = "The functions "+latex(functionOne)+" and "+latex(functionTwo)+" are defined in the first quadrant."
    output["question"] = "Find the area between the two functions."
    output["solution"] = float(area)
    payload.append(output)

    output = dict()
    output["question"] = "Find the volume of the solid of revolution of the two functions when rotated about the x-axis."
    output["solution"] = float(volumeX)
    payload.append(output)

    output = dict()
    output["question"] = "Find the volume of the solid of revolution between the two functions when it is rotated about the line x = "+str(verticalAxis)
    output["solution"] = float(volumeShell)
    payload.append(output)

    output = dict()
    output["question"] = "Find the volume between the two functions when the cross-section perpendicular to the x-axis is a square."
    output["solution"] = float(volumeSquareBase)
    payload.append(output)

    return payload

def latex(func):
    func = str(func)
    func = func.replace("**", "^")
    func = func.replace("*", "")
    return func

if __name__ == "__main__":
    import pprint
    pprint.pprint(generate(1,3))