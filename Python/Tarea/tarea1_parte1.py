#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Gerardo Corona Lopez

def palindromo_mas_largo(cadena):
    """
La funcion encuentra de una cadena definida en el código
un palindromo, si existen varios palindromos dentro de 
la cadena se elige el palindromo con mayor longitud
RECIBE: cadena (String), la cadena a analizar
REGRESA: cadena (String), La cadena con el palindromo mas extenso para su impresion a pantalla
"""
    longitud = len(cadena)
    palabras = []
    palabra = []
    #Crea una lista con las posibles combinaciones subcadenas de la cadena ingresada
    for i in range (0,longitud+1,1):
        j=0
        for j in range(0,longitud+1,1):
            if cadena [i:j] != "":
                palabras.append(cadena [i:j])
    #Verifica los palindromos de la lista de combinaciones
    for i in palabras:
        if i == i[::-1]:
            palabra.append(i)
    longitud = 0
    #Verifica de la lista de palindromos el palindromo mas largo
    for i in palabra:
        if len(i) > longitud:
            cadena = i
            longitud = len(cadena)
    return cadena

cadena = "aaabbcanitalavalatinaorooso"
palindromo = palindromo_mas_largo(cadena)
print palindromo
