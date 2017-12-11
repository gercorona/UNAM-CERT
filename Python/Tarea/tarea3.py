#!/usr/bin/python
# -*- coding: utf-8 -*-
#Se necesita el archivo datos.txt para poder jalar los datos!!!!!!!!!
from random import choice
lista2=[]

def checar(lista):
	"""
	Se necesita el archivo datos.txt para poder jalar los datos!!!!!!!!!
	Agrega a la lista los elementos  que no se encuentren repetidos
	Recibe:
		lista(str) Es la palabra que se va a agregar en la lista
	Regresa:
		Rellena una lista de manera global, donde se van almacenando los elementos
	"""
	if lista not in lista2:
		lista2.append(lista)

def rellenar_numeros(lista):
	"""
	Se necesita el archivo datos.txt para poder jalar los datos!!!!!!!!!
	Agrega numeros de 0 a 99 a el string y manda a llamar la funcion checar
	Recibe:
		lista(str) Es la palabra a la que se le van a agregar digitos
	Regresa:
		Manda a llamar a la funcion checar que es la que agregara las palabras a la lista
	"""
	i=0
	while i < 99:
		checar(lista+str(i))
		i+=1
	
f1=open('datos.txt','r')
with f1 as input_file:
	for line in input_file.readlines():
		checar(line[:-1].upper())
		checar(line[:-1].replace('A','4'))
		checar(line[:-1].replace('E','3'))
		checar(line[:-1].replace('O','0'))
		checar(line[:-1].replace('A','4').replace('O','0'))
		checar(line[:-1].replace('A','4').replace('O','0').replace('E','3'))
		checar(line[:-1].replace('A','4').replace('O','0').replace('E','3').replace('I','l'))
		checar(line[:-1].replace('a','4'))
		checar(line[:-1].replace('e','3'))
		checar(line[:-1].replace('o','0'))
		checar(line[:-1].replace('i','l'))
		checar(line[:-1].replace('a','4').replace('o','0'))
		checar(line[:-1].replace('a','4').replace('o','0').replace('e','3'))
		checar(line[:-1].replace('a','4').replace('o','0').replace('e','3').replace('i','l'))
		checar(line[:-1].lower())
		rellenar_numeros(line[:-1].upper())
		rellenar_numeros(line[:-1].replace('A','4'))
		rellenar_numeros(line[:-1].replace('E','3'))
		rellenar_numeros(line[:-1].replace('O','0'))
		rellenar_numeros(line[:-1].replace('A','4').replace('O','0'))
		rellenar_numeros(line[:-1].replace('A','4').replace('O','0').replace('E','3'))
		rellenar_numeros(line[:-1].replace('A','4').replace('O','0').replace('E','3').replace('I','l'))
		rellenar_numeros(line[:-1].replace('a','4'))
		rellenar_numeros(line[:-1].replace('e','3'))
		rellenar_numeros(line[:-1].replace('o','0'))
		rellenar_numeros(line[:-1].replace('i','l'))
		rellenar_numeros(line[:-1].replace('a','4').replace('o','0'))
		rellenar_numeros(line[:-1].replace('a','4').replace('o','0').replace('e','3'))
		rellenar_numeros(line[:-1].replace('a','4').replace('o','0').replace('e','3').replace('i','l'))
		rellenar_numeros(line[:-1].lower())
f1.close()

#print lista2
#print len(lista2)

f2 = open('pass.txt','w')
for valor in lista2:
	f2.write(valor+'\n')
f2.close()
