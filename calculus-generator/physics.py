appliesTo = ("physics",)

from sympy import symbols, N, diff, integrate, cos

import random
t = symbols('t')

#Simple program for finding area/volume/etc bounded between two curves in the first quadrant
#I'm only using the first quadrant & simple polynomials because this gets complicated real fast if you don't: and that takes effort
def generate():
    precision = 3
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    d = random.randint(1,10)

    velocity = a*cos(b*t+c)+d

    accelerationTime = random.randint(0,100)

    payload = []
    item = random.choice(["Mr. Satalino's mustache", "Mr. Stover's beard", "Mr. Kramer's anime addiction", "the downfall of the bourgeoisie"])
    output = dict()
    output["header"] = "The velocity of %s over time is given by the function $%s$" % (item, latex(str(velocity)))
    output["question"] = "Calculate the instantanious acceleration of %s at time $t = %s$" % (item, accelerationTime)
    output["solution"] = float(N(diff(velocity,t).subs(t,accelerationTime), precision))
    payload.append(output)

    positionTime = random.randint(0,10)
    position = integrate(velocity,t)+random.randint(0,50)
    #print(position)

    output = dict()
    output["question"] = "At the time $t = %s$, the position of %s is equal to $%s$. Find the equation for postion." % (positionTime,item,N(position.subs(t,positionTime),precision))
    output["solution"] = str(latex(position))
    payload.append(output)

    averageVelocityStart = random.randint(0,10)
    averageVelocityEnd = averageVelocityStart+random.randint(4,20)

    output = dict()
    output["question"] = "Find the average velocity of %s from $%s &le; t &le; %s$" % (item, averageVelocityStart, averageVelocityEnd)
    output["solution"] = float(N( (1.0/(averageVelocityEnd-averageVelocityStart))*integrate(velocity,(t,averageVelocityStart,averageVelocityEnd)), precision ))

    payload.append(output)

    return payload
    

def latex(func):
    func = str(func)
    func = func.replace("**", "^")
    func = func.replace("*", "")
    return func

if __name__ == "__main__":
    import pprint
    problem = generate()
    pprint.pprint(problem)