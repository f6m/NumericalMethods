/* Aproximacion del area de una piramide por cubos */
#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int main()
{

 int N=40000;
 int j=0;
 long double S=0;
 long double bc;
 float hc;
 int nc;
 long int C=0;

while(j < (N-2)/2)SU
{
   nc=pow((N-2*(j+1))/2,2); /* num. de cubos por capa horizontal */
   hc=2*((double)20/N); /* altura en base al problema */
   bc=4*powl((long double)20/N,2); /* area de la base de cada cubo */

   C=C+nc;
   S=S+nc*bc*hc; 

   printf("It. %i Num. cubos %i, Altura cubo %f Suma del area de cubos %Lf\n",j,nc,hc,S); 
   j++;
}

printf("Num de cubos empleados %li\n",C); 

}
