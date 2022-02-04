#include<stdio.h>

int main(){
	char cadena[20];//Arreglo que contendra la cadena
	int llave,i; //llave con la que se hara XOR  
	printf("Ingresa una cadena\n"); //impresion de pantalla
	scanf("%s",&cadena);//Cadena obtenida desde teclado
	printf("Ingresa un digito\n"); //Impresion de pantalla
	scanf("%d",&llave);//Introduccion de llave desde teclado
	printf("\nLa cadena cifrada con XOR es: "); //impresion de pantalla
	for (i=0;cadena[i]!='\0';i++) //Ciclo para generar el crifrado Xor
		printf("%c",cadena[i]^llave); //Operacion e impresion de cadenaXORllave
}
