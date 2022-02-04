#include<stdio.h>  //preprocesador

int main(int argc, char *argv[]) //funcion main que recibe parametros desde la linea de comandos
{
	if(argc==2){ //si no se ingresan elementos imprimer formato de ejecucion
		printf("Ingresa almenos un elemento en la linea de comandos:");
		printf("\n Formato: ./Practica9 <elemento1> <elemento2> <elemento3>");
	        
	}
	//si se ingresa mas de un elemento (nombre de ejecutable) imprime el ultimo elemento ingresado
	else
		printf("%s\n",argv[argc-1]);
}
