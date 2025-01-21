from sympy import *
a=0
b=1

#coeficientes para la combinación lineal
x,y,a0,a1,a2,a3=symbols('x,y,a0,a1,a2,a3')
coef=[a0,a1,a2]

#funcional lagrangiano (zx)^2+(zy)^2
def F(zx,zy): return (zx)**2+(zy)**2

#Funciones coordenadas (lin. ind. generadoras), estas forma 
#fue siguiendo las sugerencias y cambia con las utilizadas en 
#metodo de Euler de diferencias finitas
def pk(k): 
  if(k==0): return x**2+y**2 
  else: return (x**k)*y*(1-x-y)

#Construimos la funcion yn como combinacion lineal de pk
i=0
n=3
zn=0
while(i<n):
  zn=zn+coef[i]*pk(i)
  i=i+1
print(zn)

#Integramos con respecto a y siguiendo el funcional
i1=integrate(F(diff(zn,x,1),diff(zn,y,1)),(y,0,1-x))
print("1ra integral cra y:",i1)
#La aproximacion al funcional con las 4 constantes
jz=integrate(i1,(x,0,1))
print("El funcional J[z3(x,y)], 2da integral cra y:",jz)

#Derivamos para encontrar el valor de los coeficientes
#pero de la condicion z(x,1-x)=x^2+y^2 tenemos que a0=1
#pues el resto de sumandos se anula en y=1-x

Jz=2*1**2/3 - 1*a1/15 - 1*a2/45 + a1**2/90 + a1*a2/126 + a2**2/504

#print("jz con a0=1:",Jz)

#eq1=diff(jz,a0,1)
#print(eq1)
eq1=diff(Jz,a1,1)
print(eq1)
eq2=diff(Jz,a2,1)
print(eq2)

b1=solve([eq1,eq2],dict=True)
print(b1)

#Obtenemos a1: 7/2, a2: -7/5
#z3(x,y)=(x**2 + y**2) + (7/5)*x*y*(-x - y + 1) - (7/5)*x**2*y*(-x - y + 1)
#z3(x,y)=(x**2 + y**2) + x*y*(-x - y + 1)[(7/5)-(7/5)x]
