//Gerardo Corona Lopez
//Practica 6
//"Hackea" este programa
#include<stdio.h> //preprocesador
#include<limits.h>
int main(){ //Funcion principal
	unsigned int var1,var2; //declaracion de variables 
	printf("Ingresa dos enteros sin signo (maximo %u): ",UINT_MAX); //indicacion de programa y limite de numero a ingresar
	scanf("%d %d",&var1,&var2); //Obtencion de valores desde teclado
	printf("El mayor es: %d\n",(var1>var2)?var1:var2); //Operador ternario que indica el valor a imprimir en pantalla
}
