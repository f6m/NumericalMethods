from __future__ import division
#from sympy import *
import math
from numpy import cos,sin #funciones cos, sin de numpy
import numpy as np #numerical python como np

#Num. max. de iteraciones n y tolerancias
n=100
e=0.000001
d=0.000001

#funcion a encontrar el cero f(x)=0
def func(x): 
  #return ((40 + 1.1474/(x*x))*(x - 0.03985)) - 0.08314*200
  return x**5 - sin(x) + 3

#el intervalo de busqueda
x1=-10.5 #inicial 1
x2=0 #inicial 2

#biseccion,nuevo punto medio
x3=(x1+x2)/2

#vector para guardar la sucecion de puntos obtenidos en una lista
x=[x3]

#guardamos el punto
x.append(x3)

T=[x3]
t=0

while t <= n and np.abs(x3-x2) >= e and np.abs(func(x3)-func(x2)) >= d:
    print(t,x3)
    t=t+1
    T.append(t)
    if (func(x1)*func(x3)<0):
       x2=x3
    else :x1=x3
    x3=(x1+x2)/2
    x.append(x3)

T.append(t+1)

import matplotlib.pyplot as plt
#print(T,x)

plt.plot(T,x)
plt.xlabel('Iteraciones')
plt.ylabel('Metodo de la biseccion')
plt.show()
