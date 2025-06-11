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
#En esta formula solo se aproximo x(t+h) pero t+h no
xthm=x+(x1(t+h,x+h*x1(t,x))+x1(t,x))*(h/2) #Euler Mejorado

while(t <= 2):
    x=xthm
    X.append(xthm)
    t=t+h
    T.append(t)
    print(t,x)
    xthm=x+(x1(t+h,x+h*x1(t,x))+x1(t,x))*(h/2) #Euler Mejorado

import matplotlib.pyplot as plt

plt.plot(T, X)
plt.xlabel('Tiempo')
plt.ylabel('X')
plt.show()
