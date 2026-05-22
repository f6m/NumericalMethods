from sympy import * # todo de sympy
from numpy import *

t,h=symbols('t,h')
eq = Eq(h*((0.05*h+1.5)**2+1.5*(0.05*h+1.5)+1.5**2), 6*t/pi)

solv = solve(eq,h)
print(solv)
print((35**3-27000)/764)
