//preprocesador
#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<netdb.h>
#include<stdlib.h>
#include<arpa/inet.h>
#define PORT 1234
#define MAXDATASIZE 100
//funcion principal
int main()
{
	int fd, numbytes;
	char buf[MAXDATASIZE];
	struct sockaddr_in server;


	if((fd=socket(PF_INET, SOCK_STREAM,0))==-1)
	{
		printf("error en socket\n");
		exit(-1);
	}

	server.sin_family=AF_INET;
	server.sin_port=htons(PORT);
	server.sin_addr.s_addr=inet_addr("127.0.0.1");
	bzero(&(server.sin_zero),0);

	if (connect(fd,(struct sockaddr*)&server, sizeof(struct sockaddr))==-1)
	{
		printf("error en connectn" );
		exit(-1);
	}

	if((numbytes=recv(fd,buf,MAXDATASIZE,0))==-1)
	{
		printf("error en recvn" );
		exit(-1);
	}

	buf[numbytes]='\0';
	printf("Mensaje del servidor:%s\n",buf);
	//declaracion de cadena que almacenara el comando a enviar	
	char opcion="";
	do{
		printf("Inserte un comando (exit para salir)\n"); //pide comando
		scanf("%s",&opcion);//recibe el comando desde teclado, solo manda correctamente comandos,
					//sin opciones, ejemplo: ps,ls,uname ya que no acepta espacios.
		if(strcmp(&opcion,"exit")!=0){ //compara la cadena ingresada, si no es exit manda el comando
			send(fd,&opcion, 7, 0);
		}
		else{ //si es exit manda exit, cierra el descriptor y termina el programa
			send(fd,"exit",7,0);
			close(fd);
			exit(1);
		}
	}while(&opcion!="exit");
	close(fd);//cierra el descriptor para renovarlo
	return 0;
}

