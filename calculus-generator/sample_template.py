import random

appliesTo = ("wordproblem",)

def generate():
    payload = []

    variables = dict()

    output = dict()
    variables["bags"] = random.randint(1, 10)
    variables["fruits"] = random.randint(1, 10)
    output["problem"] = "Jimmy has {bags} bags of fruit. Each contains {fruits} fruits. How many fruits does Jimmy have?".format(**variables)
    output["solution"] = variables["bags"] * variables["fruits"]
    output["optional"] = False
    output["image"] = "http://eonothem.github.io/images/fruit.png"
    payload.append(output)

    output = dict()
    variables["cost"] = random.randint(1, 5)
    output["problem"] = "Each fruit costs ${cost}. How much did Jimmy spend?".format(**variables)
    output["solution"] = variables["bags"] * variables["fruits"] * variables["cost"]
    output["optional"] = False
    output["image"] = "http://eonothem.github.io/images/fruit.png"
    payload.append(output)

    output = dict()
    variables["tax"] = random.randint(1, 20)
    output["problem"] = "There's also a {tax}% sales tax! How much did Jimmy spend with tax?".format(**variables)
    output["solution"] = variables["bags"] * variables["fruits"] * variables["cost"] * (1.0 + variables["tax"]/100.0)
    output["optional"] = False
    output["image"] = "http://eonothem.github.io/images/fruit.png"
    payload.append(output)

    output = dict()
    variables["friends"] = random.randint(2, 5)
    output["problem"] = "Jimmy will be splitting the cost with {friends} friends. How much will he end up paying?".format(**variables)
    output["solution"] = variables["bags"] * variables["fruits"] * variables["cost"] * (1.0 + variables["tax"]/100.0) / variables["friends"]
    output["optional"] = False
    output["image"] = "http://eonothem.github.io/images/fruit.png"
    payload.append(output)

    output = dict()
    output["problem"] = "Explain what a fruit is.".format(**variables)
    output["solution"] = "A sweet vegetable that you put in yogurt."
    output["optional"] = True
    output["image"] = "http://eonothem.github.io/images/fruit.png"
    payload.append(output)
    
    return payload