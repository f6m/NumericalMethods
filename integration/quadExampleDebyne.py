from scipy.integrate import quad
from numpy import *
import sympy as sp

yy = lambda x: x**3/(exp(x)- 1)
#x=Symbol('x')
def y(x): return x**3/(sp.exp(x)-1)
#def g(x): return x
#r=sp.Symbol('r')
#sp.integrate(y(r),(r,0,1))

t=linspace(0,10,1000)
w=[]
for u in t:
    r=quad(y,0,u)
    w.append(r[0])
print(w)

import matplotlib.pyplot as plt

plt.plot(t, w)
plt.xlabel('x')
plt.ylabel('Integral - Modelo de Debyne*')
plt.show()
