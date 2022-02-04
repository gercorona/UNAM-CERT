#include<stdio.h>

factorial(int numero){
	if(numero==1){
		return 1;
	}
	else{
		return numero*factorial(numero-1);
	}
}

int main(){	
	int numero;
	printf("Ingresa el numero factorial: ");
	scanf("%d",&numero);
	printf("Numero factorial de %d! es: %d\n",numero,factorial(numero));
}
