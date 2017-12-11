#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Gerardo Corona Lopez

def numero_primo(numero):
    """
numero_primo indica con True si el numero indicado es un numero primo, de lo contrario da falso
RECIBE: Recibe un numero entero
REGRESA: Un booleano True para un numero primo y False para un numero no primo
"""
    if numero == 1 or numero == 2:
        return True
    elif numero % 2 == 0 or numero <= 0:
        return False
    else:
        if numero % 5 == 0 or numero % 7 == 0 or numero % 9 == 0:
            if numero == 5 or numero == 7:
                return True
            else: 
                return False
        else:
            return True

#457 si es un numero primo
print numero_primo(457)
