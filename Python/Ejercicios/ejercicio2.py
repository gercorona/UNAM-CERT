#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Gerardo Corona Lopez

#Funcion que recibe una cadena y determina si es palindromo
def recibe_palindromo(cadena):
    if cadena[::-1]==cadena:
        return True #Si es palindromo
    else:
        return False #No es palindromo 

cadena = "anitalavalatina" #Cadena
print recibe_palindromo(cadena) #Llamada de la funcion recibe_palindromo