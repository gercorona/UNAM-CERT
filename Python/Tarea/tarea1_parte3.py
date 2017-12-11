#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Gerardo Corona Lopez
primos = []
inicio = 1
def numero_primo(numero,primo):
    """
    numero_primo obtiene la lista de n numeros primos y la regresa para ser mostrada a pantalla
    RECIBE: numero (int), indica el numero de elementos que se desea obtener de numeros primos. 
            primo (int), indica el numero en el cual se desea iniciar la lista. 
    REGRESA: primos (list), regresa la lista de los n numeros primos a partir del valor de el argumento primo. 
    """
    if numero != len(primos):
        if primo == 1 or primo == 2:
            primos.append(primo)
            primo +=1
            numero_primo(numero,primo)    
        elif primo % 2 == 0 or primo <= 0:
            primo +=1
            numero_primo(numero,primo)
        else:
            if primo % 5 == 0 or primo % 7 == 0 or primo % 3 == 0:
                if primo == 5 or primo == 7 or primo == 3:
                    primos.append(primo)
                    primo +=1
                    numero_primo(numero,primo) 
                else: 
                    primo +=1
                    numero_primo(numero,primo) 
            else:
                primos.append(primo)
                primo +=1
                numero_primo(numero,primo)
        return primos
    else:
        return primos

#ejecucion de la funcion numero_primo
print numero_primo(30,inicio)
