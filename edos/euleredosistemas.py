from __future__ import division
from sympy import *
import math
from numpy import cos,sin #funciones cos, sin de numpy
import numpy as np #numerical python como np

#https://dev.to/bitproject/how-to-store-data-in-python-24a5


h=1/5 #tamano de paso
t=0 #valor inicial del tiempo
z=np.array([1,2]) #vector inicial en t=0

time=[t] #Guardamos el tiempo en una lista
theta=[z[0]] #Guardamos el tiempo en una lista

# vector en R^2 derivada
def D(z): return np.array([z[1],-sin(z[0])])


print(t,z)
zth=z+h*D(z)

while(t <= 5):
    z=zth
    t=t+h
    time.append(t) #Guardamos el tiempo en una lista
    theta.append(z[0]) #Guardamos el tiempo en una lista
    print(t,z)
    zth=z+h*D(z)

import matplotlib.pyplot as plt

plt.plot(time, theta)
plt.xlabel('Tiempo')
plt.ylabel('Angulo')
plt.show()

