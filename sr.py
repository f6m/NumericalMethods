# Algoritmo para determinar la raiz cuadrada de un numero real
# Compilacion y ejecucion:
# python sr.py 

from __future__ import division
from numpy import *

def contar_digitos(n):
    # Caso base
    if n == 0:
        return 1

    c = 0
    # Iteraciones
    while n != 0:
        # Borra el digito mas a la derecha
        n = n /10
        # Incrementa el contador
        c += 1

    return c

def x1(x):
   j=1
   while(j*j<=x):j=j+1
   return j-1


def n1(x,r,t):
   i=0
   if t >= 0:
   	j=1
	while(j*(2*x+j)<=r-x*x):j=j+1
	return j-1
   else:
	for m in range(1,13,1):
	        j=1
                print("m",m)
	    	while((j/(10**m))*(2*x+(j/(10**m)))<=r-x*x and j<=9):
		        print("j",j)	
			j=j+1
	        i = i+(j-1)/(10**m)
		print("i",i)
		x=x+i
   	return i

def r2(r):
   k = contar_digitos(r)
   if k % 2 != 0: 
 	x = r / 10**(k-1) #primer grupo mas a la izquierda
	b = 1 #tamano del bloque
   else:
	x = r / 10**(k-2)
        b = 2 #tamano del bloque
   print(x)
   xn = x1(x)
   print(xn)
   d=k-b
   n = n1(xn,r,d) #k-b numero de digitos que quedan.
   print(n)
   if (r-xn**2)/n == 0:
	   print("La raiz es:",xn+n)
   else:
	d=d-2
 	while(d>=0):
		xn = xn+n
	        n = n1(xn,r,d) #k-b numero de digitos que quedan.
		print("La aproximacion 1 de raiz es:",xn+n)
		d=d-2
        xn = xn+n
        print("d",d)
        print("xn",xn)
        print("r",r)
	n = n1(xn,r,d) #k-b numero de digitos que quedan.
	print("n",n)
	print("La aproximacion 2 de raiz es:",xn+n)
         
print(r2(9016))


