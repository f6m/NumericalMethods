/* Metodo de Euler para x'=sen(x^2)+cos(t^2), x(0)=1*/
/* con h=0.2, 0<=t<=2*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double f(double x ,double t)
{
return sinf(x*x) + cosf(t*t);
}

int main()
{
double t =0 , h = 0.2;
double x = 1.0,xth;

fprintf(stdout,"x \t\t Euler\n");
fprintf(stdout,"%f\t\t %f\n",t,x);
while ( t<=2.0)
{
xth = x+h*f(x,t);
x = xth;
t+=h;
fprintf(stdout,"%f\t\t%f\n",t,x);
}
exit(EXIT_SUCCESS);
}
