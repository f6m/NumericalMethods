from sympy import *

#coeficientes para la combinación lineal
x,y,b,a0,a1,a2,a3,a11,a12=symbols('x,y,b,a0,a1,a2,a3,a11,a12')
coef=[a1,a2,a3]

#funcional lagrangiano (zx)^2+(zy)^2
def F(z,zx,zy): return (zx)**2 + (zy)**2 - 2*z

#Funciones coordenadas (lin. ind. generadoras), estas forma
#fue siguiendo las sugerencias y cambia con las utilizadas en
#metodo de Euler de diferencias finitas
def pk(k): return (y**2-((x**2)/3))

#Construimos la funcion yn como combinacion lineal de p1
#solo una iteracion
i=0
n=1
zn=0
while(i<n):
  zn=zn+coef[i]*pk(i)
  i=i+1
print(zn)

#Integramos con respecto a y siguiendo el funcional
#colocamos la derivada explicita cra x
i1=integrate(F(zn,(y**2-x**2/3)*a11-2*x*a1/3,2*y*a1),(y,0,x/sqrt(3)))
print("1ra integral cra y:",simplify(i1))

#Definimos el lagrangiano para calcular su ecuacion de Euler y determinar a1(x)

def FF(x,a1,a11):
  return 2*(4*sqrt(3)*x**3*(30*a1**2 + 10*a1*a11*x + 15*a1 + 2*a11**2*x**2)/405)

#FF_y - a12F_{y'y'}-a11F_{y'y}-a1F_{xy'}=0

eulereq = simplify(diff(FF(x,a1,a11),a1,1)
-a12*diff(FF(x,a1,a11),a11,2)-a11*diff(diff(FF(x,a1,a11),a1,1),a11,1)-diff(diff(FF(x,a1,a11),x,1),a11,1))
print("Ecuacion de Euler:",eulereq)

#La ecuacion eulereq se simplifica como una de Cauchy-Euler no homogenea
#su solucion es a1(x)=(c1x+c2x^{-5}-3/4), con las condiciones iniciales
#que se anula en el triangulo equilatero entonces b=6, y la aproximación
#al extremo del funcional es z1(x,y)=(3/4)(x/6-1)(y^2-x^2/3)
