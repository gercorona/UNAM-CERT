#include<stdio.h> //preprocesador
int main() //funcion principal
{
	char *c="hola\0"; //creacion de apuntador
	for(int i=0;*(c+i)!='\0';i++) //ciclo para la impresion de apuntador
		printf("%c\n",*(c+i)); //impresion de apuntador
}
