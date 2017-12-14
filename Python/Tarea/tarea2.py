#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Gerardo Corona Lopez

from random import *
minus = "abcdefghijklmnopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digitos = "1234567890"


def genera_contra(minuscula,may,dig):
    """
    genera_contra genera contraseñas aleatorias por medio de la funcion 
    choice eligiendo un elemento de las cadenas asignadas en la primera parte del codigo
    llamadas minus, mayus y digitos e intercalandolas para crear una cadena que sera
    la contraseña final, llamandose la funcion de forma recursiva. 
    RECIBE: 
    minuscula (entero), la cantidad de mimusculas que tendra la contraseña
    may (entero), la cantidad de mayusculas que tendra la contraseña
    dig (entero), la cantidad de numero que tendra la contraseña
    REGRESA:
    La cadena final con todas las especificaciones de minusculas, mayusculas y numeros.
    """
    if minuscula > 0:
        if may > 0:
            if dig > 0:
                return choice(minus) + choice(mayus) + choice(digitos) + genera_contra(minuscula-1,may-1,dig-1)
            else:
                return choice(minus) + choice(mayus) + genera_contra(minuscula-1,may-1,0)
        else:
            if dig > 0:
                return choice(minus) + choice(digitos) + genera_contra(minuscula-1,0,dig-1)
            else:
                return choice(minus) + genera_contra(minuscula-1,0,0)
            
    else: 
        if may > 0:
            if dig > 0:
                return choice(mayus) + choice(digitos) + genera_contra(0,may-1,dig-1)
            else:
                return choice(mayus) + genera_contra(0,may-1,0)
        else:
            if dig > 0:
                return  choice(digitos) + genera_contra(0,0,dig-1)
            else:
                return ""

letra_minus = int(raw_input("Minusculas: "))
letra_mayus = int(raw_input("Mayusculas: "))
numeros = int(raw_input("Numeros: "))
passwd = genera_contra(letra_minus,letra_mayus,numeros)
print "Contraseña generada con " + str(letra_minus) + " minusculas " + str(letra_mayus) + " mayusculas y " + str(numeros) + " numeros" 
print passwd