from __future__ import division
from sympy import *
import math
from numpy import cos,sin #funciones cos, sin de numpy
import numpy as np #numerical python como np

#https://dev.to/bitproject/how-to-store-data-in-python-24a5
#v''=-cos(v),v(0)=0,v'(0)=1
#u=v'->f(t,u,v)=u
#u'=-cos(v)->g(t,u,v)=-cos(v)

def f(t,x1,x2): return -cos(x2)
def g(t,x1,x2): return  x1


def F1(t,x1,x2,h): return h*f(t,x1,x2)
def F2(t,x1,x2,h): return h*f(t+h/2,x1+F1(t,x1,x2,h)/2,x2+FF1(t,x1,x2,h)/2)
def F3(t,x1,x2,h): return h*f(t+h/2,x1+F2(t,x1,x2,h)/2,x2+FF2(t,x1,x2,h)/2)
def F4(t,x1,x2,h): return h*f(t+h,x1+F3(t,x1,x2,h),x2+FF3(t,x1,x2,h))


def FF1(t,x1,x2,h): return h*g(t,x1,x2)
def FF2(t,x1,x2,h): return h*g(t+h/2,x1+F1(t,x1,x2,h)/2,x2+FF1(t,x1,x2,h)/2)
def FF3(t,x1,x2,h): return h*g(t+h/2,x1+F2(t,x1,x2,h)/2,x2+FF2(t,x1,x2,h)/2)
def FF4(t,x1,x2,h): return h*g(t+h,x1+F3(t,x1,x2,h),x2+FF3(t,x1,x2,h))


h=1/5 #tamano de paso
t=0 #valor inicial del tiempo
z=np.array([0,1]) #vector inicial en t=0

time=[t] #Guardamos el tiempo en una lista
theta=[z] #Guardamos el vector en una lista

# segundo termino en la formula de RK4
def R(z): return np.array([1/6*(F1(t,z[0],z[1],h)+2*F2(t,z[0],z[1],h)+2*F3(t,z[0],z[1],h)
+F4(t,z[0],z[1],h)),1/6*(FF1(t,z[0],z[1],h)+2*FF2(t,z[0],z[1],h)+2*FF3(t,z[0],z[1],h)
+FF4(t,z[0],z[1],h))])


print(t,z)
zth=z+R(z)

while(t <= 5):
    z=zth
    t=t+h
    time.append(t) #Guardamos el tiempo en una lista
    theta.append(z) #Guardamos el la aprox. actual en una lista
    print(t,z)
    zth=z+R(z)

import matplotlib.pyplot as plt

plt.plot(time, theta)
plt.xlabel('Tiempo')
plt.ylabel('Angulo')
plt.show()