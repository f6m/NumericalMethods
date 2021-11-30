from __future__ import division
from sympy import *
import math
def f(t,x): return math.sin(x*x) + math.cos(t*t)
def F1(t,x,h): return h*(f(t,x))
def F2(t,x,h): return h*(f(t+h/2,x+F1(t,x,h)/2))
def F3(t,x,h): return h*(f(t+h/2,x+F2(t,x,h)/2))
def F4(t,x,h): return h*(f(t+h,x+F3(t,x,h)))


h=1/5
t=0
x=1

r=[t] #Guardamos el tiempo en una lista
func=[x] #Guardamos las aproximaciones en una lista

print(t,x)
xth=x+(1/6)*(F1(t,x,h)+2*F2(t,x,h)+2*F3(t,x,h)+F4(t,x,h))

while(t <= 2):
    x=xth
    t=t+h
    r.append(t) #Guardamos el tiempo en una lista
    func.append(x) #Guardamos el tiempo en una lista
    print(t,x)
    xth=x+(1/6)*(F1(t,x,h)+2*F2(t,x,h)+2*F3(t,x,h)+F4(t,x,h))

import matplotlib.pyplot as plt

plt.plot(r, func)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


