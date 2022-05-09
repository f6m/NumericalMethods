#Integración numérica: método del trapecio compuesto

from sympy import *
import math
#x=Symbol('x')
a=0
b=math.pi/2
N=10 #debe ser par
h=(b-a)/N
sum1 = 0
sum2 = 0
x0=a
def f(x):return (1/sqrt(1+math.sin(x)*math.sin(x))) 

#suma1
j=2
while(j<=N/2):
     sum1 = sum1 + f(x0+(2*j-2)*h)
     j=j+1

#suma2
j=1
while(j<=N/2):
     sum2 = sum2 + f(x0+(2*j-1)*h)
     j=j+1

print(simplify((h/3)*(f(a)+2*sum1+4*sum2+f(b))))

from mpmath import *
mp.dps = 25; mp.pretty = True
print(ellipk(-1))
