import random
import operator

appliesTo = ("addition", "subtraction", "multiplication", "division", "arithmetic")

operators = {
    "+" : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.div
}

operatorsWords = {
    "addition" : "+",
    "subtraction" : "-",
    "multiplication" : "*",
    "division" : "/"
}

payload = [{
}]

def arithmetic(pType, cap):    
    if pType == "arithmetic":
        pType = random.choice(operatorsWords.keys())    
    operator = operatorsWords[pType]

    a = random.randint(1, cap)
    b = random.randint(1, cap)
    payload[0]["problem"] = "%s %s %s = " % (a, operator, b)
    payload[0]["solution"] = operators[operator](a, b)
    payload[0]["optional"] = False
    return payload