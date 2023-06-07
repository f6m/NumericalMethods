from __future__ import division
from sympy import *
import math
def x1(t,x): return math.sin(x*x) + math.cos(t*t)

h=1/5
t=0
T=[t]
x=1
X=[x]

print(t,x)
xth=x+h*x1(t,x)

while(t <= 2):
    x=xth
    X.append(xth)
    t=t+h
    T.append(t)
    print(t,x)
    xth=x+h*x1(t,x)

import matplotlib.pyplot as plt

plt.plot(T, X)
plt.xlabel('Tiempo')
plt.ylabel('X')
plt.show()

