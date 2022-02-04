//Preprocesador
#include<stdio.h>
#include<stdlib.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<unistd.h>
//funcion main
int main(int argc, char *argv){
	//Declaracion descriptor, numero aleatorio, y archivo por la ubicacion /dev/random del sistema.  
	int fd,random;
	char *archivo="/dev/random";
	fd=open(archivo,O_RDONLY); //permiso de solo lectura para el archivo
	//si no se puede abrir se obtiene un -1 y manda el mensaje error, si es correcto manda el numero de descriptor
	if(fd==-1)
		fprintf(stderr,"No se pudo abrir o crear el archivo");
	printf("Descriptor de archivo: %d\n",fd);
	//lee 4 bytes del descriptor, y lo almacena en random
	//e imprime el numero aleatorio, sino se puede manda el mensaje error
	if(read(fd,&random,4)==-1)
		fprintf(stderr,"Error al leer el archivo.");
	printf("%d\n",random);
	//cierra el descriptor, sino se puede manda mensaje error
	if(close(fd)==-1)
		fprintf(stderr,"No se pudo cerrar el descriptor de archivo");
}
