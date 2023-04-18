from sympy import * # todo de sympy
from numpy import *
#Simbolos
y1,y2,y3,y4,y5=symbols('y1,y2,y3,y4,y5')

#Funciones multivariables coordenadas
def f1(y1,y2,y3,y4):  return y2-2*y1-0.06324616*(y2)**0.5
def f2(y1,y2,y3,y4):  return y3-2*y2+y1-0.06324616*(y3-y1)**0.5
def f3(y1,y2,y3,y4):  return y4-2*y3+y2-0.06324616*(y4-y2)**0.5
def f4(y1,y2,y3,y4):  return 2-2*y4+y3-0.06324616*(2-y3)**0.5

def f(x): return [f1(x),f2(x),f3(x),f4(x)]

eq1 = Eq(y2-2*y1-0.06324616*(y2)*0.5, 0)
eq2 = Eq(y3-2*y2+y1-0.06324616*(y3-y1)*0.5, 0)
eq3 = Eq(y4-2*y3+y2-0.06324616*(y4-y2)*0.5, 0)
eq4 = Eq(2-2*y4+y3-0.06324616*(2-y3)*0.5, 0)

#usamos nsolve para aproximar la solución
solv = nsolve([eq1, eq2, eq3, eq4], [y1,y2,y3,y4],[1,3,6,4],prec=20)
print(solv)

print(f1(solv[0],solv[1],solv[2],solv[3]))
print(f2(solv[0],solv[1],solv[2],solv[3]))
print(f3(solv[0],solv[1],solv[2],solv[3]))
print(f4(solv[0],solv[1],solv[2],solv[3]))
