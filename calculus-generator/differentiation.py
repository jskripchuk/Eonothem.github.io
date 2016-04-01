from sympy import diff, symbols
from sympy.parsing.sympy_parser import parse_expr

import random

x, y = symbols('x y')
exp = parse_expr("5 * x ** 2 + 4")

print diff(exp)