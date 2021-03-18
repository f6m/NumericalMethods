#include<stdio.h>
#include<math.h>

float f(float x)
{
//return 4+((0.3333)*sinf(2*x));
return x*(x-0.5);
}

int main()
{

 float x0=-1.5,x1=f(x0),e=0.0001,d=0.0001;
 int N=100;
 int j=0;


while(j<N)
{
 printf("[%i] Punto fijo actual %f con f(%f)=%f \n",j+1,x0,x0,f(x0));
 if(fabsf(x1-x0)<e || fabsf(f(x1)-f(x0))<d)
	break;
x0=x1;
x1=f(x0);
j++;
};
printf("[%i] Punto fijo %f con f(%f)=%f\n",j+1,x0,x0,f(x0));
 
}
