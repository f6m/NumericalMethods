from __future__ import division
from numpy import *
from cmath import *

#V^3-415.7V^2+3680V-0.1465=0

a=-415.7
b=3680
c=-0.1465

p=-(a**2/3)+b #-53922.16333333333
q=((2*a**3)/27)-(a*b/3)+c #-4811234.657092592

print("p=",p)
print("q=",q)

print("D=",((q**2)/4)+(p**3)/27) #-19822522412.03125
D=((q**2)/4)+(p**3)/27
R=sqrt(-D)
print("R=",R) #140792.47995554042

print("-q/2",-q/2)
x=complex(-q/2,R)
y=complex(-q/2,-R)
print("-q/2+sqrt(D)",x)
print("-q/2-sqrt(D)",y)

#x=2405617.328546296+140792.47995554042j
print("PolarS1=",polar(x))
#(2409733.8553903103, 0.058459861023862324)
r3=(2409733.8553903103)**(1/3)
print("sqrt[3](r)#",r3)
t1=0.058459861023862324/3
print("theta/3",t1)
t2=(0.058459861023862324+(2*pi))/3
print("theta/3+2pi/3",t2)
t3=(0.058459861023862324+(4*pi))/3
print("theta/3+4pi/3",t3)

u1=rect(r3,t1)
print("u1^3=",u1**3)
u2=rect(r3,t2)
print("u2^3=",u2**3)
u3=rect(r3,t3)
print("u3^3=",u3**3)

print("PolarS2=",polar(y))
#2409733.8553903145, -0.05845986102386223
print("sqrt[3](r)#",r3)
t11=-0.05845986102386223/3
print("theta/3",t11)
t22=(-0.05845986102386223+(2*pi))/3
print("theta/3+2pi/3",t22)
t33=(-0.05845986102386223+(4*pi))/3
print("theta/3+4pi/3",t33)

#(22544791450.412132)*(1/3)
#1.5707486294297304/3-3.1416*2/3
#-1.5707486294297304/3-3.1416*2/3

print("-p/3",-p/3)
print("prod1", rect(r3,t1)*rect(r3,t11))
print("prod2", rect(r3,t2)*rect(r3,t33))
print("prod3", rect(r3,t3)*rect(r3,t22))

y1=rect(134.0673504043563,0.019486620341287408)+rect(134.0673504043563,-0.019486620341287408)
y2=rect(r3,t2)+rect(r3,t33)
y3=rect(r3,t3)+rect(r3,t22)

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
