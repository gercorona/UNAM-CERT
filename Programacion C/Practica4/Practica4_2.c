//Gerardo Corona Lopez
//Practica 4.2
#include <stdio.h> //biblioteca

int main(){ //funcion main
	int i,valor; //declaracion de variables
	printf("Ingresa el valor del limite: ");//impresion de pantalla
	scanf("%d",&valor);//obtencion de valor desde teclado
	for(i=1;i<=valor;i++) //ciclo para impresion de valores
		printf((i&1)?"\n%d\n":"",i); //imprime los numeros nones desde el 1 hasta n

}
