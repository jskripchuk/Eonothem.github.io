import matplotlib.pyplot as plt, numpy as np
import matplotlib.axes as axes
import StringIO
from math import *

#import webbrowser

def graph(function, range = 10):
    sio = StringIO.StringIO()

    plt.plot([ eval(function) for x in np.arange(-5, 5, 1) ])
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")

    plt.savefig(sio, format="png", transparent=True)
    img_b64 = sio.getvalue().encode("base64").strip()

    plt.clf()
    sio.close()
    return "data:image/png;base64,%s" % img_b64

#with open("THING.html", "w+") as f:
#    f.write("<img src='%s'/>" % graph("x**3"))
#webbrowser.open("THING.html", new=0, autoraise=True)#