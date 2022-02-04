//Preprocesador
#include<stdio.h> 
#define BEGIN int main(){
#define END }
#define THEN {
#define ENDIF }
#define IF if
#define PRINT printf
#define ELSE }else{
#define INTEGER int
//Codigo ofuscado
//el codigo original es: [x>=10]
//no fue posible hacer
//#define [ (
//#define ] )
BEGIN
INTEGER x=10;
IF (x>=10) 
THEN
	PRINT ("TENGO DIEZ\n");
ELSE
	PRINT("REPROBARE\n");
ENDIF
END

