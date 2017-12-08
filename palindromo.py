#!/usr/bin/python
# _*_ coding: utf-8 _*_
#UNAM-CERT

def palindromo(cadena):
	if cadena[::-1]==cadena:
		return True
	else:	
		return False


cadena = "anitalavalatina"
resultado = palindromo(cadena)
print cadena + "es palindromo: " + resultado
