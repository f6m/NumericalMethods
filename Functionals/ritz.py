from sympy import *
h=0.2
a=-1
b=1

#Condiciones iniciales
y0=0
y5=0

#coeficientes para la combinación lineal
x,l,m,a1,a2,a3,a4=symbols('x,l,m,a1,a2,a3,a4')
coef=[a1,a2,a3,a4]

#funcional
def F(x,y,y1): return l*y1**2+(1-l*(m**2))*y

#Funciones coordenadas (lin. ind. generadoras), estas forma 
#fue siguiendo las sugerencias y cambia con las utilizadas en 
#metodo de Euler de diferencias finitas
def pk(k): return (1-x**2)*x**(2*k)

#Construimos la funcion yn como combinacion lineal de pk
i=0
n=1
yn=0
while(i<n):
  yn=yn+coef[i]*pk(1)
  i=i+1

print(yn)

#Integramos siguiendo el funcional
p=integrate(F(x,yn,diff(yn,x,1)), (x,a,b))

#Derivamos para encontrar el valor de los coeficientes
eq1=diff(p,a1,1)
b1=solve([eq1],dict=True)
a1=b1[0][a1]
print(a1)
print(yn)

#Con a1=(l*m**2 - 1)/(4*l) tenemos la familia de extremales
#dados con una iteracion del método de Ritz

def y(x): return (7*(l*m**2 - 1)/(44*l))*(x**2)*(1-x**2)

#integramos para satisfacer la condicion isoperimetrica = l 
#y tener una ecuacion para l

i=integrate(y(x),(x,a,b))
print(i)
solve([i-1],l,dict=True)

simplify((7*((7/(7*m**2 - 165))*m**2 - 1)/(44*(7/(7*m**2 - 165))))*(x**2)*(1-x**2))
#Entonce la solucion aproximada es y(x)=15x**2(1-x**2)/4
