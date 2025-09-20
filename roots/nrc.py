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

#funcion a encontrar el punto fijo de Newton-Raphson x-(f(x)/f'(x))=x
def f(z): 
  return z**5+7/z
def df(z):
  return 5*z**4-7/z**2
def nr(z): 
  return z-(f(z)/df(z))

#punto inicial
z0=complex(0,1) #inicial 1
#x2=0.8 #inicial 2

#vector para guardar la susecion de números complejos obtenidos en una lista
z=[z0]

#nuevo punto conforme al metodo del punto fijo 
z1=nr(z0)

#guardamos el punto
z.append(z1)

#tiempo
T=[0,1]
t=2
while t <= n and np.abs(z1-z0) >= e and np.abs(nr(z1)-nr(z0)) >= d:
    T.append(t)
    t=t+1
    z0=z1
    z1=nr(z0)
    print(t,z1)
    z.append(z1)

#T.append(t+1)
print(T,z)


plt.plot(T,z, marker="o")
plt.xlabel('Iteraciones')
plt.ylabel('Metodo de Newton-Raphson complejo')
plt.show()
