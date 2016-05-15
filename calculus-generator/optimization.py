appliesTo = ("optimization",)
from sympy import *
from mpmath import mp
from random import randint, choice
def latex(func):
    func = str(func)
    func = func.replace("**", "^")
    func = func.replace("*", "")
    return func

def generate():
    t = symbols("t")
    eq = 5 * t / (t + 10) + 200 / t**2
    eq2 = 0.5 * mp.e**(0.07 * t) + 3

    payload = []
    output = dict()
    output["header"] = """<em>"Dude, you want a little pot?"</em> whispered Mr. Satalino, barely in his twenties, standing at a dark alleyway, 3 in the morning.<br>
<em>"Depends on what you got. Shoot, are the cops watching?"</em><br>
Mr. Satalino's mustache twitched involuntarily as he glanced around for signs of the law.<br>
<em>"Nah, we're safe. For now. Listen, you want it or not? You gonna get lower GI distress on me?"</em><br>
<em>"Whatever man. 20 bucks sound fair?"</em><br>
<em>"Good enough. You owe me next time, this stuff costs me 23 dollars a pop."</em> he said, handing his customer a tiny clay pot.<br>
Mr. Satalino is an astute young pot dealer with a conceptual and procedural/analytical understanding of the market he deals in."""
    output["question"] = "His personal research has determined that he loses ${0}$ dollars per sale due to tolls and shipping, where $t &ge; 2$ and $t$ represents the number of days since he started selling personal sized gardening receptacles. Calculate the day he lost the least amount of money.".format(latex(eq))
    output["solution"] = float(N(solve(diff(eq))[2]))
    payload.append(output)

    output = dict()
    output["question"] = "He also found that his clients have been willing to pay $0.5e^{0.07t}+3$ dollars where $2 &le; t &le; 25$. Find the day he earned the most money."
    output["solution"] = 25
    payload.append(output)

    output = dict()
    output["question"] = "Find the day Mr. Satalino broke even."
    output["solution"] = 12

    payload.append(output)
    return payload