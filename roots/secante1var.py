from __future__ import division
#from sympy import *
import math
from numpy import cos,sin #funciones cos, sin de numpy
import numpy as np #numerical python como np

#Num. max. de iteraciones n y tolerancias
n=100
e=0.001
d=0.001

#funcion a encontrar el cero f(x)=0
def func(x): 
  return ((40 + 1.1474/(x*x))*(x - 0.03985)) - 0.08314*200

#puntos iniciales
x1=0.2 #inicial 1
x2=0.8 #inicial 2

#vector para guardar la sucecion de puntos obtenidos en una lista
x=[x1, x2]

#nuevo punto conforme al metodo de la secante
x3=x1-(func(x1)*(x2-x1)/(func(x2)-func(x1)))

#guardamos el punto
x.append(x3)


T=[1,2]
t=3

while t <= n and np.abs(x3-x2) >= e and np.abs(func(x3)-func(x2)) >= d:
	print(t,x3)
    	t=t+1
	T.append(t)
	x1=x2
	x2=x3
	x3=x1-(func(x1)*(x2-x1)/(func(x2)-func(x1)))
	x.append(x3)

T.append(t+1)

import matplotlib.pyplot as plt
#print(T,x)

plt.plot(T,x)
plt.xlabel('Iteraciones')
plt.ylabel('Metodo de la secante')
plt.show()

