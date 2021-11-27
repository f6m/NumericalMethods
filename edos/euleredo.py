from __future__ import division
from sympy import *
import math
def x1(t,x): return math.sin(x*x) + math.cos(t*t)

h=1/5
t=0
x=1

print(t,x)
xth=x+h*x1(t,x)

while(t <= 2):
    x=xth
    t=t+h
    print(t,x)
    xth=x+h*x1(t,x)

""

