#include<stdio.h> //preprocesador
int main(){ //funcion main
	char password[10] = "o7k3654)+", contra[20],cifrado[20]; //declaracion de arreglos
	int llave=7,i,validacion; //declaracion de int
	printf("Password: ");//impresion de pantalla pidiendo password
	scanf("%s",&contra);//obtiene pass de teclado
	for(i=0;contra[i]!='\0';i++){
		cifrado[i]=contra[i]^llave; //cifra la password ingresada para compararla con la almacenada, funcionando como hash(XOR si es reversible) y no guardarla en claro
	}
	for(i=0;password[i]!='\0';i++){//compara la contrasena ingresada con la almacenada
		if(cifrado[i]!=password[i]){ //si es diferente se asigna un cero y rompe ciclo
			validacion=0;
			break;
		}
		else
			validacion=1; //asigna uno si es el mismo caracter
	}
	if (validacion==0) //compara si la validacion es 0
		printf("GTFO!\n"); //imprime GTFO si no es contra correcta
	else
		printf("OK!\n");//imprime OK si es contra correcta
}
