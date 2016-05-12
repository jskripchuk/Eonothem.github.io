from sympy import *
import differentiation

import random
x = symbols('x')

#Simple program for finding area/volume/etc bounded between two curves in the first quadrant
#I'm only using the first quadrant & simple polynomials because this gets complicated real fast if you don't: and that takes effort
def generateBoundingFunctions(lower, upper):
	precision = 5
	c = random.randint(1,10)
	b = random.randint(1,10)
	g = random.randint(0,5)
	functionOne = c*x+g
	functionTwo = b*x**2
	intercepts = solve(functionOne-functionTwo,x)
	boundVal = 0
	if(intercepts[0] > 0):
		boundVal = intercepts[0]
	else:
		boundVal = intercepts[1]

	boundVal = N(boundVal,precision)
	
	area = integrate(functionOne-functionTwo, (x,0,boundVal))

	volumeX = N(pi,precision)*integrate(functionOne**2-functionTwo**2, (x,0,boundVal))

	
	
	#print(intercepts[1] < 0)
	



generateBoundingFunctions(1,3)