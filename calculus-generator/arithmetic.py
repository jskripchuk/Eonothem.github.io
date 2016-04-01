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

def generate(pType, cap):    
    if pType == "arithmetic":
        pType = random.choice(operatorsWords.keys())    
    operator = operatorsWords[pType]

    a = random.randint(1, cap)
    b = random.randint(1, cap)

    payload[0]["choices"] = [a + b * 1.0, a - b * 1.0, a * b * 1.0, a / b * 1.0]
    random.shuffle(payload[0]["choices"])

    payload[0]["problem"] = "%s %s %s = " % (a, operator, b)
    payload[0]["solution"] = operators[operator](a * 1.0, b)
    payload[0]["optional"] = False

    payload[0]["image"] = "http://eonothem.github.io/images/arithmetic.png"
    return payload