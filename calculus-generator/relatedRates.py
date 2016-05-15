appliesTo = ("relatedrates",)
from sympy import *
from random import randint, choice

def generate():
    a, r, t = symbols("x y t")
    a = Function('r')(t)
    r = Function('a')(t)

    payload = []
    item = choice(["Mr. Stella's bald spot", "Mr. Satalino's forehead", "Mr. Stover's beard", "the weird mole on my elbow"])
    related = choice(["DDT levels in the environment", "amount of lead in CSW water"])
    a = randint(2, 5)
    b = randint(0, 9)
    L = t**a + b

    output = dict()
    output["header"] = "{0} can be roughly approximated as a circle. Extensive research shows that the area of {0} is directly correlated with {1}.".format(item, related)
    output["question"] = "The following table of experimental data shows the {0} over time. Use a graphing calculator to find the formula $L(t)$ describing the data. You should get whole numbers.\n{1}".format(related, genTable(L, t))
    output["solution"] = latex(L)
    payload.append(output)

    output = dict()
    time = randint(1, 6)
    output["question"] = "At time $t = {0}$, find $dL/dt$.".format(time)
    output["solution"] = int(N(diff(L, t).subs(t, time)))
    payload.append(output)

    output = dict()
    output["question"] = "Further research suggests that the radius of {0} is equal to $2L$. Find the rate of change of the area of {0} at time $t = {1}$.".format(item, time)
    output["solution"] = float(N(diff(pi * (2 * L)**2).subs(t, time)))
    payload.append(output)
    return payload

def genTable(equation, t):
    table = "<table><tr><td>$t$</td>"
    for i in range(0, 6):    
        table += "<td>%s</td>" % i
    table += "</tr><td>$L(t)$</td>"
    for i in range(0, 6):
        table += "<td>%s</td>" % int(N(equation.subs(t, i)))
    return table

def latex(func):
    func = str(func)
    func = func.replace("**", "^")
    func = func.replace("*", "")
    return func

if __name__ == "__main__":
    import pprint
    pprint.pprint(generate())