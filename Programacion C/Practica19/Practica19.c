//Preprocesador
#include<stdio.h>
#include<fcntl.h>
//funcion principal
int main(int argc, char *argv[]){ //obtiene parametros desde linea de comandos
	if(argc==2){ //valida que se ejecute con el nombre del exe y una ruta de directorio
	printf("Archivo:%s\n",argv[argc-1]); //imprime el archivo leido
	int fsize,fd = open(argv[argc-1], O_RDONLY); //declaracion de fsize y el asignacion del file descriptor 
	fsize = lseek(fd,0,SEEK_END); //Asignacion de tamano de un archivo
	printf("Tamano\n%d bits\n%d bytes\n%d KB\n",fsize*8,fsize,fsize/1024); //impresion de tamano en diferente formato
	close(fd); //se cierra el file descriptor
	}
	else{ //Si se ingresa mas de una ruta o ninguna, imprime el formato correcto de correr el programa.
		printf("FORMATO: ./Practica19 <Ruta_Archivo>\n");
	}
}
