from __future__ import division
import math
from numpy import cos,sin #funciones cos, sin de numpy
import numpy as np #numerical python como np
import matplotlib.pyplot as plt

#Numero maximo de iteraciones n
#Error en la aproximacion permitido: e(horizontal) y d (vertical)
n=100
e=0.0001
d=0.0001

#funcion a encontrar el punto fijo f(x)=x
def func(x): return 0.00003985+16628/(40+(147200/(x*x)))
  #return 4+0.0333*sin(2*x)

#punto inicial
x0=100.5 #inicial 1
#x2=0.8 #inicial 2

#vector para guardar la sucecion de puntos obtenidos en una lista
x=[x0]

#nuevo punto conforme al metodo del punto fijo 
x1=func(x0)

#guardamos el punto
x.append(x1)

T=[0,1]
#print(T,x)
t=2
while t <= n and np.abs(x1-x0) >= e and np.abs(func(x1)-func(x0)) >= d:
    T.append(t)
    t=t+1
    x0=x1
    x1=func(x0)
    print(t,x1)
    x.append(x1)

#T.append(t+1)
print(T,x)

plt.plot(T,x, marker="o")
plt.xlabel('Iteraciones')
plt.ylabel('Metodo del punto fijo')
plt.show()
