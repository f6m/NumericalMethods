from sympy import *
h=0.2
a=0
b=1

#Condiciones iniciales
y0=0
y5=0

#puntos equiespaciados 0,0.2,0.4,0.6,0.8,1
y1,y2,y3,y4=symbols('y1,y2,y3,y4')

sol = [y0,y1,y2,y3,y4,y5]
print(sol)
#Lagrangian J[y]=int_0^1 y1**2+y**2+2xy dx
def F(x,y,y1): return y1**2+y**2+2*x*y
def derivativeap(dx,yk1,yk2): return (yk2-yk1)/dx
d=h
i=0
I=0
#I=F(d,sol[i],derivativeap(h,sol[i],sol[i+1]))
print(I)
while(d<=b):
  I=I+F(d,sol[i],derivativeap(h,sol[i],sol[i+1]))
  print(I)
  d=d+h
  i=i+1
I=I*h
eq1=diff(I,y1)
eq2=diff(I,y2)
eq3=diff(I,y3)
eq4=diff(I,y4)

#Comparamos con la solucion analitica y(x)=(sinh(x)/sinh(1))-x
def y(x): return (sinh(x)/1.17520119364)-x
print(y(0.2),y(0.4),y(0.6),y(0.8))

solve([eq1,eq2,eq3,eq4],dict=True)
