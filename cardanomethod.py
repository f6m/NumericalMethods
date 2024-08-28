from __future__ import division
from numpy import *
from cmath import *

#x^3+x^2+x+1=0, x^3+ax^2+bx+c=0
#Coeficientes
a=1
b=1
c=1

#y^3+py+q=0
#Coeficientes ecuacion reducida
p=-(a**2/3)+b
q=((2*a**3)/27)-(a*b/3)+c #
print("p=",p)
print("q=",q)

#Discriminante
print("D=",((q**2)/4)+(p**3)/27) 
D=((q**2)/4)+(p**3)/27
if D>=0:
  R=sqrt(D)
else:
  R=sqrt(-D)
print("R=",R)

print("-q/2",-q/2)
if D<0:
  x=complex(-q/2,R)
  y=complex(-q/2,-R)
else:
  x=(-q/2)+R
  y=(-q/2)-R

print("-q/2+sqrt(D)",x)
print("-q/2-sqrt(D)",y)

s1=polar(x) #Forma polar del primer numero
print("PolarS1=",s1)
print("PolarS1",(abs(x),phase(x)))
#(2409733.8553903103, 0.058459861023862324)
r3=(abs(x))**(1/3)
print("sqrt[3](r)#",r3)
t1=phase(x)/3
print("theta/3",t1)
t2=(phase(x)+(2*pi))/3
print("theta/3+2pi/3",t2)
t3=(phase(x)+(4*pi))/3
print("theta/3+4pi/3",t3)

print("Validacion de las raices cubicas s1 de",x)
u1=rect(r3,t1)
print("u1^3=",u1**3)
u2=rect(r3,t2)
print("u2^3=",u2**3)
u3=rect(r3,t3)
print("u3^3=",u3**3)

s2=polar(y)
print("PolarS2=",s2)
print("PolarS2=",(abs(y),phase(y)))
r33=(abs(y))**(1/3)
print("sqrt[3](r)S2",r33)
t11=phase(y)/3
print("theta/3",t11)
t22=(phase(y)+(2*pi))/3
print("theta/3+2pi/3",t22)
t33=(phase(y)+(4*pi))/3
print("theta/3+4pi/3",t33)

print("Validacion de las raices cubicas s2 de",y)
v1=rect(r33,t11)
print("v1^3=",v1**3)
v2=rect(r33,t22)
print("v2^3=",v2**3)
v3=rect(r33,t33)
print("v3^3=",v3**3)

#Evaluar si el producto es -p/3
print("-p/3",-p/3)
print("prod1", rect(r3,t1)*rect(r33,t22))
print("prod2", rect(r3,t2)*rect(r33,t11))
print("prod3", rect(r3,t3)*rect(r33,t33))

y1=rect(r3,t1)+rect(r33,t22)
y2=rect(r3,t2)+rect(r33,t11)
y3=rect(r3,t3)+rect(r33,t33)

print("y1=",y1)
print("y2=",y2)
print("y3=",y3)

print("validacion y1", y1**3+p*y1+q)
print("validacion y2", y2**3+p*y2+q)
print("validacion y2", y3**3+p*y3+q)

V1=y1-a/3
V2=y2-a/3
V3=y3-a/3

print("V1=",V1)
print("V2=",V2)
print("V3=",V3)

print("validacion V1", V1**3+a*V1**2+b*V1+c)
print("validacion V1", V2**3+a*V2**2+b*V2+c)
print("validacion V1", V3**3+a*V3**2+b*V3+c)
