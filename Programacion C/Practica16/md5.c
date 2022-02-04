#include<string.h>
#include<openssl/md5.h>
#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
int main(int argc, char *argv[])
{	
	if (argc==2){
		int fd = open(argv[argc-1],O_RDONLY);
	  	int size = lseek(fd,0,SEEK_END);
		printf("%d\n",size);
		unsigned char digest[MD5_DIGEST_LENGTH];
		char string[size];   
		read(fd,string,size);
		puts(string);
		MD5((unsigned char*)&string, strlen(string), (unsigned char*)&digest);    
		char mdString[33];
		for(int i = 0; i < 16; i++)
	        	sprintf(&mdString[i*2], "%02x", (unsigned int)digest[i]);
		printf("md5 digest: %s\n", mdString);
		return 0;
	}
	else{
		printf("Formato: ./md5 <archivo>\n");
	}
}
