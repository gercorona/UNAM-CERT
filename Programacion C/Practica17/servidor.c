//Preprocesador
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <fcntl.h>
#define PORT 1234	// puerto de conexion

int main() {
	int sockfd, new_sockfd;  // descriptores de archivo
	struct sockaddr_in host, cliente;	// Informacion de las direcciones IP
	socklen_t sin_size;
	int recv_length=1, yes=1;
	char buffer[1024];
	FILE *fd,*fd2;
	if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1)
		perror("Error al crear el socket");

	if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int)) == -1)
		perror("Error al agregar la opcion SO_REUSEADDR en setsockopt");
	
	host.sin_family = PF_INET; 
	host.sin_port = htons(PORT);
	host.sin_addr.s_addr = inet_addr("127.0.0.1"); // Asigno mi IPP
	memset(&(host.sin_zero), '\0', 8); // El resto de la estructura en 0s

	if (bind(sockfd, (struct sockaddr *)&host, sizeof(struct sockaddr)) == -1)
		perror("Error haciendo el bind");

	if (listen(sockfd, 5) == -1)
		perror("Error al escuchar en el socket");
	while(1) {    // Accept loop
		sin_size = sizeof(struct sockaddr_in);
		new_sockfd = accept(sockfd, (struct sockaddr *)&cliente, &sin_size);
		if(new_sockfd == -1)
			perror("Error al aceptar la conexion");
		printf("server: Conexion aceptada desde %s desde  %d\n",inet_ntoa(cliente.sin_addr), ntohs(cliente.sin_port));
		send(new_sockfd, "system(""clear"")\n", 13, 0);
		while(1){ //Recibe cadenas desde que manda el cliente
			recv(new_sockfd, &buffer, 1024, 0); //recibe el comando desde el cliente
			if(strcmp(buffer,"exit")!=0){
			system(buffer);//ejecuta el comando en el sistema linux
			printf("\n");
			}
			else{
				close(new_sockfd); //si recibe exit, cierra el descriptor y sale
				exit(1);
			}
		}
		close(new_sockfd);//cierra el descriptor de socket y lo renueva por el while
	}
	return 0;
}
