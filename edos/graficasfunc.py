from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

#https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html


def tbanco(t):
    if(t<0 or t>4): return 0
    else: return t*(1/4)

def escalon1(t):
    if(t<1): return 0
    else: return 1

def funcion(t):
    return tbanco(t) + escalon1(t)

t = np.linspace(-1,5,10000)
plt.plot(t, [funcion(x) for x in t])
#plt.plot(t, [tbanco(x) for x in t])

#plt.plot(t, [tbanco(x) for x in np.linspace(4,7,10000)])

plt.ylim(-2.5, 2.5)

plt.show()


#from sympy import *
#x=Symbol('x')

#plt.plot(t, [integrate(x*x*x/(exp(x)-1),[x,0,r]) for r in t])





