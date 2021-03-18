/* Metodo de la falsa posicion */
#include<stdio.h>
#include<math.h>
#include<stdlib.h>

float f(float x)
{

//return x*x*x*x*x - sinf(x) + 3;
return cos(x) - x*x*x;

}

int main()
{

 float a=0,b=1,e=0.0001,d=0.0001,xn;
 int N=100;
 int j=0;

if (!(f(a)*f(b) < 0))
{
 printf("Error:No hay raiz en el intervalo!!!\n");
 exit(0);
}

while(fabs(a-b) > e && fabs(f(a)-f(b)) > d && j < N)
{
   xn=a-f(a)/((f(b)-f(a))/(b-a));
   printf("It. %i, intervalo [%f,%f], aprox. %f, f(%f)= %f\n",j+1,a,b,xn,xn,f(xn)); 
   if (f(xn)*f(a) < 0)
    b = xn;
    else a = xn;
    j++;
}

printf("Solucion aproximada %f valor de la funcion %f \n",xn,f(xn));

}
