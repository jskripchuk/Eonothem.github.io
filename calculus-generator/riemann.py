appliesTo = ("riemann",)
from sympy import N, symbols, integrate
from random import randint
from numpy import linspace
x = symbols("x")

def latex(func):
    func = str(func)
    func = func.replace("**", "^")
    func = func.replace("*", "")
    return func

def eval(eq, num):
    ans = float(N(eq.subs(x, num * 1.0)))
    #print ans
    return ans

def leftRiemann(eq, a, b, subint):
    dx = 1.0 * (b - a)/subint
    intervals = linspace(a, b, num=subint, endpoint=False)
    area = 0.0
    for x in intervals:
        area += (eval(eq, x) * dx)
    return area


def rightRiemann(eq, a, b, subint):
    dx = 1.0 * (b - a)/subint
    intervals = linspace(a + dx, b, num=subint)
    area = 0.0
    for x in intervals:
        area += (eval(eq, x) * dx)
    return area

def exact(eq, a, b):
    return float(N(integrate(eq, (x, a, b))))

print leftRiemann(x**2, 4, 8, 7)
print rightRiemann(x**2, 4, 8, 7)

def generate():
    eq = ((randint(2, 7)) * x**(randint(1, 4)) + (randint(0, 10)))
    a = randint(0, 5)
    b = a + randint(4, 10)
    subint = randint(4, 8)

    payload = []

    output = dict()
    output["header"] = "The function $f(x) = {0}$ is continuous between ${1} &le; x &le; {2}$.".format(latex(eq), a, b)
    output["question"] = "Calculate the <em>left</em> Riemann sum of $f(x)$ between ${0} &le; x &le; {1}$ with {2} subintervals.".format(a, b, subint)
    output["solution"] = leftRiemann(eq, a, b, subint)
    payload.append(output)

    output = dict()
    output["question"] = "Is this an overestimate or underestimate? Explain."
    output["solution"] = "Underestimate, a left Riemann sum on an increasing function is always an underestimate."
    output["optional"] = True
    payload.append(output)

    output = dict()
    output["question"] = "Calculate the <em>right</em> Riemann sum of $f(x)$ between ${0} &le; x &le; {1}$ with {2} subintervals.".format(a, b, subint)
    output["solution"] = rightRiemann(eq, a, b, subint)
    payload.append(output)

    output = dict()
    output["question"] = "Is this an overestimate or underestimate? Explain."
    output["solution"] = "Overestimate, a right Riemann sum on an increasing function is always an overestimate."
    output["optional"] = True
    payload.append(output)

    output = dict()
    output["question"] = "Calculate the exact area of $f(x)$ between ${0} &le; x &le; {1}$".format(a, b)
    output["solution"] = exact(eq, a, b)
    payload.append(output)

    return payload

#if __name__ == "__main__":
#    import pprint
#    pprint.pprint(generate())