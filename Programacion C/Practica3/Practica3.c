//Preprocesador
#include<stdio.h> 
#include<time.h>
#include <limits.h>
//funcion main
int main(){
	//declaracion de variables de tipo time_t (valor actual y valor maximo)
	time_t now=time(NULL),fin_du_monde = INT_MAX;
	//impresion de pantalla de fecha actual
	printf ("Fecha de ejecucion de programa:  %s\n", ctime (&now));
	//impresion de patalla del fin del mundo (32bits)
	printf ("Fin du monde: %s\n",ctime(&fin_du_monde));
	//impresion de pantalla del la diferencia de segundos para el fin del mundo
	printf("Segundos para el fin del mundo: %d\n",fin_du_monde-now);
}
