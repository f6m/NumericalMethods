#include<stdio.h>
#include<math.h>

float f(float x)
{
//return 4+((0.3333)*sinf(2*x));
//return x*(x-0.5)-x;
return powf(x,3)-x+3;
}

float df(float x)
{
return 2*x - 1.5;
}

int main()
{

 float x0=-0.5,x1=-2.0,x2,e=0.0001,d=0.0001;
 int N=100;
 int j=0;


while(j<N)
{
x2=x0-f(x0)/((f(x1)-f(x0))/(x1-x0));
 printf("[%i] Ptos. iniciales (%f,%f), aproximacion actual %f con f(%f)=%f \n",j+1,x0,x1,x2,x2,f(x2));
 if(fabsf(x2-x1)<e || fabsf(f(x2)-f(x1))<d)
	break;
x0=x1;
x1=x2;
j++;
};
}
