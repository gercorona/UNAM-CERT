#include <stdio.h> //preprocesador
void fprimos(int); //prototipo de funcion
int main(){ //funcion principal
	int primos; //declaracion
	printf("Ingresa el numero de numeros primos a mostrar: ");//impresion de pantalla
	scanf("%d",&primos);//obtiene numero desde teclado
	fprimos(primos);//el numero de elementos se para como parametro
	
}
void fprimos(int primos){ //funcion que recibe un int
	int cont=0,numero=2; //declaracion y asignacion
	if(primos>=0){	//validacion de variable primos
		printf("\nNumeros Primos:\n"); //impresion de pantalla
		while(cont!=primos){ //ciclo que se ejecuta mientras sean diferentes las variables
			if(numero==2){ //condicion valida numero = 2
				printf("%d\n",numero); //imprime el numero dos
				numero+=1;//suma a uno el numero 
				cont+=1;//suma el numero a dos
			}
			else if(numero%2==0)//si el mod del numero es 2
				numero+=1;//suma uno a lo que contiene numero
			else{
				if(numero%3==0|numero%5==0|numero%7==0){ //si el modulo 3,5 y 7 es cero
					if(numero==3|numero==5|numero==7){ //si el numero es 3, 5 o 7
						printf("%d\n",numero); //imprime el 3, el 5 o el 7
						numero+=1; //suma un uno a numero
						cont+=1; //suma uno a cont
					}
					else
						numero+=1;//suma uno a numero
				}
				else{
					printf("%d\n",numero);//imprime el numero si no su modulo 3,5,7 no es 0
					numero+=1;//suma 1 a numero
					cont+=1;//suma 1 a cont
				}
			}

		}
	}
	else
		printf("\nNumero ingresado no valido\n"); //Si el numero no es valido, como negativo.
}	
