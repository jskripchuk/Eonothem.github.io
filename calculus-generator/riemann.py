appliesTo = ("riemann",)
from sympy import N, symbols, integrate
from random import randint
x = symbols("x")

def latex(func):
    func = str(func)
    func = func.replace("**", "^")
    func = func.replace("*", "")
    return func

def eval(eq, num):
    return int(N(eq.subs(x, num)))

def leftRiemann(eq, a, b, subint):
    dx = 1.0 * (b-a)/subint
    area = 0
    for i in range(a, b):
        area += (eval(eq, i) * dx)
    return float(area)

def rightRiemann(eq, a, b, subint):
    dx = 1.0 * (b-a)/subint
    area = 0
    for i in range(a + 1, b + 1):
        area += (eval(eq, i) * dx)
    return float(area)

def exact(eq, a, b):
    return float(N(integrate(eq, (x, a, b))))

def generate():
    eq = ((randint(2, 7)) * x**(randint(1, 4)) + (randint(0, 10)))
    a = randint(0, 5)
    b = a + randint(4, 10)
    subint = randint(4, 8)

    payload = []

    output = dict()
    output["header"] = "The function $f(x) = {0}$ is continuous between ${1} &le; x &le; {2}$.".format(latex(eq), a, b)
    output["question"] = "Calculate the <em>left</em> Riemann sum of $f(x) between ${0} &le; x &le; {1}$ with {2} subintervals.".format(a, b, subint)
    output["solution"] = leftRiemann(eq, a, b, subint)
    payload.append(output)

    output = dict()
    output["question"] = "Is this an overestimate or underestimate? Explain."
    output["solution"] = "Overestimate, a left Riemann sum on an increasing function is always an overestimate."
    output["optional"] = True
    payload.append(output)

    output = dict()
    output["question"] = "Calculate the <em>right</em> Riemann sum of $f(x) between ${0} &le; x &le; {1}$ with {2} subintervals.".format(a, b, subint)
    output["solution"] = rightRiemann(eq, a, b, subint)
    payload.append(output)

    output = dict()
    output["question"] = "Is this an overestimate or underestimate? Explain."
    output["solution"] = "Underestimate, a right Riemann sum on an increasing function is always an underestimate."
    output["optional"] = True
    payload.append(output)

    output = dict()
    output["question"] = "Calculate the exact area of $f(x) between ${0} &le; x &le; {1}$ with {2} subintervals.".format(a, b, subint)
    output["solution"] = exact(eq, a, b)
    payload.append(output)

    return payload

if __name__ == "__main__":
    import pprint
    pprint.pprint(generate())