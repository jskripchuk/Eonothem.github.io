import random
import operator

arithmeticList = ("addition", "subtraction", "multiplication", "division", "arithmetic")

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
    "type": None,
    "problem": None,
    "solution": None
}]

def arithmetic(pType, ranges = 100):    
    if pType == "arithmetic":
        pType = random.choice(operatorsWords.keys())    
    operator = operatorsWords[pType]

    a = int(random.randint(1, ranges))
    b = int(random.randint(1, ranges))
    payload[0]["type"] = pType
    payload[0]["problem"] = "%s %s %s = " % (a, operator, b)
    payload[0]["solution"] = operators[operator](a, b)
    return payload