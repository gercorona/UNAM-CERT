#!/usr/bin/python
# -*- coding: utf-8 -*-
#CORONA GERARDO, REYES JAIRO
#se encesita el archivo nmap.xml para poder correrlo!!!!!!!!!!!!!!!!
from datetime import datetime
import hashlib
import re 

#es el archivo donde vamos a guardar todo
f2=open('prendidos.csv','w')
f2.write('Ip\n')
f3=open('apagados.csv','w')
f3.write('Ip\n')
f4=open('puerto22.csv','w')
f4.write('Ip\n')
f5=open('honeypots.csv','w')
f5.write('Ip\n')
f6=open('dominio.csv','w')
f6.write('Ip\n')
#f1 es el documento donde se va a leer todo
f1=open('nmap.xml','r')

f1.close()
#volvemos a abrir el archivo ya que el read, nos manda hasta el final
f1=open('nmap.xml','r')

#variables globales, que contendran los resultados finales
host_prendidos=0
host_apagados=0
host_puerto22=0
host_dominio=0
serv_http=0
dionaea=0
ip=0
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
dom=0
puerto22=0
honey=0
with f1 as input_file:
	"""
	Por cada linea que va leyendo va identificando las etiquetas correspondientes
	Al leer una linea, necesitabamos mas de un elemento, por lo cual utilizamos unas variables
	locales para identificar a que puerto correspondian.
	El valor lo separamos con split para identificar mas facilmente los elementos con los que	contaba
	"""
	for line in input_file.readlines():
		puerto22_abierto=0
		puerto80_abierto=0
		nombre_http=0
		for valor in line.split():
			if "<host>" in line or "<host " in line:
				honey=1
				puerto22=1
				dom=1
				if valor=='state=\"up\"':
					ip=1
					host_prendidos+=1
					break
				if valor=='state=\"down\"':
					ip=2
					host_apagados+=1
					break	
			if ip==1 and "<address " in line:
				if re.match('addr=\".*',valor):
					for valor2 in valor.split('\"'):
						if "addr=" not in valor2:
							if cont1==0:
								f2.write(valor2)
								cont1=1
							else:
								f2.write(',\n'+valor2)
							break
					break
			if ip==1 and "</host>" in line:
				honey=0
				puerto22=0
				dom=0
				ip=0
				break	
			if ip==2 and "<address " in line:
				if re.match('addr=\".*',valor):
					for valor2 in valor.split('\"'):
						if "addr=" not in valor2:
							if cont2==0:
								f3.write(valor2)
								cont2=1
							else:
								f3.write(',\n'+valor2)
							break
					break
			if ip==2 and "</host>" in line:
				ip=0
				break
			if "<port " in line or "<ports><port" in line:
					if valor=='portid=\"22\"><state':
						puerto22_abierto=1
					elif valor=='portid=\"80\"><state':
						puerto80_abierto=1
					if puerto22_abierto==1 and puerto22==1:
						if valor=='state=\"open\"':
							if cont3==0:
								f4.write(valor2)
							else:
								f4.write(',\n'+valor2)
							cont3=1
							break
					elif puerto80_abierto==1:
						if valor=='state=\"open\"':
							nombre_http=1
					if nombre_http==1 and honey==1:
						if re.match('product=\"Dio.*',valor):
							print valor2
							if cont4==0:
								f5.write(valor2)
							else:
								f5.write(',\n'+valor2)
							cont4=1
							break
			#
			if "<hostname " in line and dom==1:
				if re.match('name=\".*',valor):
					if cont5==0:
						f6.write(valor2)
						cont5=1
					else:
						f6.write(',\n'+valor2)



f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
