#Aplicacion del metodo de Newton-Raphson multivariable a G(x)=0
#ejecucion python NRM.py

from sympy import * # todo de sympy

#Simbolos 
y1,y2,y3,y4,y5=symbols('y1,y2,y3,y4,y5')

#Funciones multivariables coordenadas G(f1,f2,f3,f4,f5)
f1=y1*y2-2*y1**2+(1/3)**2*y1-(1/3)**3
f2=y2*y3-2*y2**2+3*y1*y2-y1*y3-y1**2+(1/3)**2*y2-(1/3)**2*y1-(1/3)**3
f3=y3*y4-2*y3**2+3*y2*y3-y2*y4-y2**2+(1/3)**2*y3-(1/3)**2*y2-(1/3)**3
f4=y4*y5-2*y4**2+3*y3*y4-y3*y5-y3**2+(1/3)**2*y4-(1/3)**2*y3-(1/3)**3
f5=2*y5-2*y5**2+3*y4*y5-2*y4-y4**2+(1/3)**2*y5-(1/3)**2*y4-(1/3)**3

""" Ejemplo de como determinar las derivadas parciales
para cada una de la funciones
>>> diff(f1,y1)
0.111*cos(y1) - 2
>>> diff(f1,y2)
1
>>> diff(f1,y3)
0
>>> diff(f1,y4)
0
>>> diff(f1,y5)
0
"""

from numpy import cos,sin #funciones cos, sin de numpy
import numpy as np #numerical python como np

x=np.array([2,-1,1,1,2]) #vector inicial
N=100 #Numero maximo de iteraciones

#Funcion no lineal multivariable a encontrarle un cero, usamos x[0]=y1,...,x[4]=y5
def G(x): return np.array([x[0]*x[1]-2*x[0]**2+(1/3)**2*x[0]-(1/3)**3,
x[1]*x[2]-2*x[1]**2+3*x[0]*x[1]-x[0]*x[2]-x[0]**2+(1/3)**2*x[1]-(1/3)**2*x[0]-(1/3)**3,
x[2]*x[3]-2*x[2]**2+3*x[1]*x[2]-x[1]*x[3]-x[1]**2+(1/3)**2*x[2]-(1/3)**2*x[1]-(1/3)**3,
x[3]*x[4]-2*x[3]**2+3*x[2]*x[3]-x[2]*x[4]-x[2]**2+(1/3)**2*x[3]-(1/3)**2*x[2]-(1/3)**3,
2*x[4]-2*x[4]**2+3*x[3]*x[4]-2*x[3]-x[3]**2+(1/3)**2*x[4]-(1/3)**2*x[3]-(1/3)**3])

#Matriz jacobiana de G en vectores fila
def J(x): return np.array([[x[1]-4*x[0]+(1/3)**2,x[1],0,0,0],
[3*x[1]-x[2]-1-(1/3)**2,x[2]-4*x[1]+3*x[0]+(1/3)**2,x[1]-x[0],0,0],
[0,3*x[2]-x[3]-2*x[1]-(1/3)**2,x[3]-4*x[2]+3*x[1]+(1/3)**2,x[2]-x[1],0],
[0,3*x[2],13*x[1]-x[4]-2*x[2]-(1/3)**2,x[4]-4*x[3]+(1/3)**2,x[3]-x[2]],
[0,0,0,3*x[4]-2-2*x[3]-(1/3)**2,2-4*x[4]+3*x[3]+(1/3)**2]])

#Calcula el incremento para el vector 2
delta = np.linalg.solve(J(x), -G(x))

#norma entre el vector 1 y 2
norma = np.linalg.norm(x+delta - x)

i=0 #Contador de iteraciones
d=0.0001 #presicion vertical
e=0.0001 #presicion horizontal

while np.linalg.norm(G(x))>d and norma>e and i<N:
 delta=np.linalg.solve(J(x),-G(x))
 norma=np.linalg.norm(x+delta - x)
 x=x+delta
 i+=1


print(x)
print(i)
print(np.linalg.norm(G(x)))
print(norma)


"""
"Cinco iteraciones:
np.linalg.norm(x-x+delta)
2.5803514835340007e-16
>>> x
array([ 2.82441431,  2.61420918,  2.34814063,  2.00295365,  1.55697152])
"""
