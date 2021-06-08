/* Metodo de Euler para x'=[cos(t^2)+In(x+t)]/x, x(0)=1*/
/* con h=0.2, 0<=t<=2*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* x'=f(t,x) */
double f(double x ,double t)
{
return cosf(t*t)+logf(x*x);
}

int main()
{
double t=0 , h = 0.2;
double x=1.0, xth;

fprintf(stdout,"x \t\t Euler mejorado\n");
fprintf(stdout,"%f\t\t %f\n",t,x);

while (t<=1.8)
{
xth = x+(h/2)*f(x+h*f(x,t),t)+(h/2)*f(x,t);
x = xth;
t+=h;
fprintf(stdout,"%f\t\t%f\n",t,x);
}
exit(EXIT_SUCCESS);
}
