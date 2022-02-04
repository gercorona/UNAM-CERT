#include<stdio.h>//preprocesador

int main(){ //funcion main
	//declaracion de variables
	int opcion;
	float base,altura;
	//despliegue de menu
	printf("Elige el cuerpo geometrico del cual calcular area\n");
	printf("1. Triangulo\n2. Rectangulo\n3. Cuadrado\nOpcion: ");
	//obtiene opcion
	scanf("%d",&opcion);
	//analiza el contenido de opcion
	switch(opcion){
		case 1: //si es 1 pide base y altura y calcula area de triangulo
			printf("\nBase: ");
			scanf("%f",&base);
			printf("\nAltura: ");
			scanf("%f",&altura);
			printf("\nArea: %.2f u^2\n",(base*altura)/2);
			break;
		case 2: //si es 2 pide base y altura y calcula area de rectangulo
			printf("\nBase: ");
			scanf("%f",&base);
			printf("\nAltura: ");
			scanf("%f",&altura);
			printf("\nArea: %.2f u^2\n",base*altura);
			break;
		case 3://si es 3 pide lado y calcula area de cudrado
			printf("\nLado: ");
			scanf("%f",&base);
			printf("\nArea: %.2f u^2\n",base*base);
			break;
		default://cualquier otro numero muestra opcion no valida
			printf("\nOpcion no valida\n");
			break;
	}
}
