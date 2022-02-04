//Gerardo Corona Lopez
//Practica 2
//Bibliotecas, standard input output, y limites.
#include <stdio.h> 
#include <limits.h>
//funcion principal
int main(){
	//impresion de formato de tabla
	printf("Limites de tipos de variable en C\n\n");
	printf("Tipo de variable\t\tValor_Min\t\t\tValor_Max\n");
	printf("----------------------------------------------------------------------------------------\n");
	//caracter con signo
	printf("Signed char");
	printf("\t\t\t%d",SCHAR_MIN);
	printf("\t\t\t\t%d\n\n",SCHAR_MAX);
	//caracter sin signo
	printf("Unsigned char");
	printf("\t\t\t%d",0);//minimo indicado en la cabecera limits.h
	printf("\t\t\t\t%d\n\n",UCHAR_MAX);
	//entero corto con signo
	printf("Signed short int");
	printf("\t\t%d",SHRT_MIN);
	printf("\t\t\t\t%d\n\n",SHRT_MAX);
	//entero corto sin signo
	printf("Unsigned short int");
	printf("\t\t%d",0);//minimo indicado en la cabecera limits.h
	printf("\t\t\t\t%d\n\n",USHRT_MAX);
	//entero con signo
	printf("Signed int");
	printf("\t\t\t%d",INT_MIN);
	printf("\t\t\t%d\n\n",INT_MAX);
	//entero sin signo
	printf("Unsigned int");
	printf("\t\t\t%d",0);//minimo indicado en la cabecera limits.h
	printf("\t\t\t\t%u\n\n",UINT_MAX);
	//entero largo con signo
	printf("Signed long int");
	printf("\t\t\t%ld",LONG_MIN);
	printf("\t\t%ld\n\n",LONG_MAX);
	//entero largo sin signo
	printf("Unsigned long int");
	printf("\t\t%d",0);//minimo indicado en la cabecera limits.h
	printf("\t\t\t\t%lu\n\n",ULONG_MAX);
	//entero largo largo con signo
	printf("Signed long long int");
	printf("\t\t%lld",LLONG_MIN);
	printf("\t\t%lld\n\n",LLONG_MAX);
	//entero largo largo sin signo
	printf("Unsigned long long int");
	printf("\t\t%d",0);//minimo indicado en la cabecera limits.h
	printf("\t\t\t\t%llu\n\n",ULLONG_MAX);
}
