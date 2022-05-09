#Integración numérica: método del trapecio compuesto

from sympy import *

x=Symbol('x')
a=1
b=10
N=10 #debe ser par
h=(b-a)/N
j=0
sum1 = 0
sum2 = 0
x0=a
def f(x): return 1/(sqrt(1-(sin(x)**2))) #K(k)


#suma1
while(j<=N/2):
     sum1 = sum1 + f(x0+(2j-2)*h)
     j=j+1

#suma2
j=0
while(j<=N/2):
     sum2 = sum2 + f(x0+(2j-1)*h)
     j=j+1

print(h/3*(f(a)+2*sum1+4*sum2+f(b)))

from mpmath import *
mp.dps = 25; mp.pretty = True
print(ellipk(-1))
 
