import random

appliesTo = ("wordproblem",)

def wordProblem():
    payload = []

    variables = dict()

    output = dict()
    variables["bags"] = random.randint(1, 10)
    variables["fruits"] = random.randint(1, 10)
    output["problem"] = "Jimmy has {bags} bags of fruit. Each contains {fruits} fruits. How many fruits does Jimmy have?".format(**variables)
    output["solution"] = variables["bags"] * variables["fruits"]
    payload.append(output)

    output = dict()
    variables["cost"] = random.randint(1, 5)
    output["problem"] = "Each fruit costs ${cost}. How much did Jimmy spend?".format(**variables)
    output["solution"] = variables["bags"] * variables["fruits"] * variables["cost"]
    payload.append(output)

    output = dict()
    variables["tax"] = random.randint(1, 20)
    output["problem"] = "There's also a {tax}% sales tax! How much did Jimmy spend with tax?".format(**variables)
    output["solution"] = variables["bags"] * variables["fruits"] * variables["cost"] * (1.0 + variables["tax"]/100.0)
    payload.append(output)

    output = dict()
    variables["friends"] = random.randint(2, 5)
    output["problem"] = "Jimmy will be splitting the cost with {friends} friends. How much will he end up paying?".format(**variables)
    output["solution"] = variables["bags"] * variables["fruits"] * variables["cost"] * (1.0 + variables["tax"]/100.0) / variables["friends"]
    payload.append(output)

    return payload