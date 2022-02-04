#include <stdio.h>//Biblioteca standard


int main(){//funcion principal
	int i;
	for (i=0;i<=30;i++){ //ciclo de numeros 1-30
		if(i%3==0){ //multiplos de 3
			if(i%5==0){ //multiplos de 3 y 5
				printf("FizzBuzz\n"); //impresion de FizzBuzz
			}
			else{	
				printf("Fizz\n"); //impresion de Fizz
			}

		}
		else if(i%5==0){ //multiplos de 5
			printf("Buzz\n"); //impresion de Buzz
		}
		else { //cualquier otro numero
			printf("%d\n",i); //impresion del numero
		}
	}
}
		
