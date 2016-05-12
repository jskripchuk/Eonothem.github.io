from sympy import diff, symbols
from sympy.parsing.sympy_parser import parse_expr

import random

appliesTo = ("differentiation",)

x, y = symbols('x y')

skipChance = 60 #percent chance of skipping
maxCo = 10 #max coefficient
negChance = 50 #percent chance of negative

def sign(): #generate random sign
    if random.randint(0, 100) < negChance:
        return "-"
    else:
        return "+"

def coefficient(): #generate random coefficient
    return random.randint(1, maxCo)

def polyGen(degree): #build a polynomial
    poly = ""
    for i in range(degree, -1, -1):
        if random.randint(0, 100) > skipChance or i == degree:
            poly += (sign() + str(coefficient()) + "*x**" + str(i))
    return parse_expr(poly)

def latex(func):
    func = str(func)
    func = func.replace("**", "^")
    func = func.replace("*", "")
    return func

def generate(degree):
    problem = polyGen(degree)
    return {
        "optional": False,
        "problem": latex(problem),
        "solution": latex(diff(problem, x))
    }

if __name__ == "__main__":
    import pprint
    pprint.pprint(generate(3))