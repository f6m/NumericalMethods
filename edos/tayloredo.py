from __future__ import division
from sympy import *
import math
def x1(t,x): return t**2 - math.sin(x) + math.cos(t)
def x2(t,x): return 2*t - (x1(t,x))*math.cos(x) - math.sin(t)
def x3(t,x): return -math.cos(t) - x2(t,x)*x2(t,x)*math.cos(x) + x1(t,x)*x1(t,x)*math.sin(x) + 2
def x4(t,x): return math.sin(t) - x3(t,x)*math.cos(x) + 3*x1(t,x)*x2(t,x)*math.sin(x) + x1(t,x)**3*math.cos(x)

h=0.01
t=-1
T=[t] #array
x=3
X=[x] #array

print(t,x)
xth=x+h*x1(t,x)+(h*h/2)*x2(t,x)+(h**3/6)*x3(t,x)+(h**4/24)*x4(t,x)

while(t < 1):
    x=xth
    X.append(xth)
    t=t+h
    T.append(t)
    print(t,x)
    xth=x+h*x1(t,x)+(h*h/2)*x2(t,x)+(h**3/6)*x3(t,x)+(h**4/24)*x4(t,x)

import matplotlib.pyplot as plt

plt.plot(T, X)
plt.xlabel('Tiempo')
plt.ylabel('X')
plt.show()

