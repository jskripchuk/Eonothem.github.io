#LRS = 30
#RRS = 55
#5 SUBINT
#Y = x**2

eq = 5 * x**2 + 3

from sympy import *
x = symbols("x")

def eval(eq, num):
    return int(N(eq.subs(x, num)))

def leftRiemann(eq, a, b, subint):
    dx = 1.0 * (b-a)/subint
    area = 0
    for i in range(a, b):
        area += (eval(eq, i) * dx)
    return area

def rightRiemann(eq, a, b, subint):
    dx = 1.0 * (b-a)/subint
    area = 0
    for i in range(a + 1, b + 1):
        area += (eval(eq, i) * dx)
    return area

def exact(eq, a, b):
    return N(integrate(eq, (x, a, b)))

def generate():
    