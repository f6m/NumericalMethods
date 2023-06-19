#x'=(-4x-1)/(4t)=f(x,t) s.a.: $x(1)=1

from __future__ import division
from sympy import *
import math
from numpy import cos,sin #funciones cos, sin de numpy
import numpy as np #numerical python como np

#Funcion derivada proveniente del pvi
def f(x,t): return (-4*x-1)/(4*t)

#Partes del metodo de rk4
def F1(x,t,h): return h*f(x,t)
def F2(x,t,h): return h*f(x+F1(t,x,h)/2,t+h/2)
def F3(x,t,h): return h*f(x+F2(t,x,h)/2,t+h/2)
def F4(x,t,h): return h*f(x+F3(t,x,h),t+h)

h=0.01 #tamano de paso
t=1 #valor inicial del tiempo
z=1 #vector inicial en t=0

time=[t] #Guardamos el tiempo en una lista
theta=[z] #Guardamos el vector en una lista

# segundo termino en la formula de RK4
def R(z): return 1/6*(F1(z,t,h)+2*F2(z,t,h)+2*F3(z,t,h)
+F4(z,t,h))

# 1er termino
print(t,z)
zth=z+R(z)

# Repeticion de rk4
while(t <= 5):
    z=zth
    t=t+h
    time.append(t) #Guardamos el tiempo en una lista
    theta.append(z) #Guardamos el la aprox. actual en una lista
    print(t,z)
    zth=z+R(z)

import matplotlib.pyplot as plt

y = np.linspace(1, 5, 100)
def f(y): return (20/(16*y))-1/4

plt.plot(time, theta)
plt.scatter(y,f(y),c='red',alpha=0.3)
plt.xlabel('Tiempo')
plt.ylabel('Angulo')
plt.show()
