#include<stdio.h>
#include<math.h>
#include<stdlib.h>

float f(float x)
{

return x*x*x*x*x - sinf(x) + 3;

}

int main()
{

 float a=-10.5,b=0.0,e=0.0001,d=0.0001,xn;
 int N=100;
 int j=0;

if (!(f(a)*f(b) < 0))
{
 printf("Error:No hay raiz en el intervalo!!!\n");
 exit(0);
}

while(fabs(a-b) > e && fabs(f(a)-f(b)) > d && j < N)
{
   xn = (a+b)/2;
   printf("Iteracion %i, intervalo [%f,%f], valor medio %f, f(%f)= %f\n",j+1,a,b,xn,xn,f(xn)); 
   if (f(xn)*f(a) < 0)
    b = xn;
    else a = xn;
    j++;
}

printf("Solucion aproximada %f valor de la funcion %f \n",xn,f(xn));

}
