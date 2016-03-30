import matplotlib.pyplot as plt, numpy as np
import StringIO
from math import *

def graph(function, range = 10):
    plt.plot([ eval(function) for x in np.arange(0,5,0.001) ])
    sio = StringIO.StringIO()
    plt.savefig(sio, format="png")
    img_b64 = sio.getvalue().encode("base64").strip()
    plt.clf()
    sio.close()
    return "data:image/png;base64,%s" % img_b64