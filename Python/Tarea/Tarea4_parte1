#!/usr/bin/python
# -*- coding: utf-8 -*-
#CORONA GERARDO, REYES JAIRO
#se encesita el archivo nmap.xml para poder correrlo!!!!!!!!!!!!!!!!
from datetime import datetime
import hashlib
import re

#f2 es el archivo donde vamos a guardar todo
f2=open('reporte.txt','w')
fecha="\nLa fecha de ejecucion del programa es: "+ str(datetime.now()) + "\n"
print fecha
f2.write(fecha)
#f1 es el documento donde se va a leer todo
f1=open('nmap.xml','r')

#leemos el contenido para sacar los hash
contenido = f1.read()
md5 = "El hash md5 es: " + hashlib.new("md5",contenido).hexdigest()
sha1 = "El hash sha1 es: " + hashlib.new("sha1",contenido).hexdigest()
print md5
f2.write(md5+"\n")
print sha1
f2.write(sha1+"\n")

f1.close()
#volvemos a abrir el archivo ya que el read, nos manda hasta el final
f1=open('nmap.xml','r')

#variables globales, que contendran los resultados finales
host_prendidos=0
host_apagados=0
host_puerto22=0
host_puerto53=0
host_puerto80=0
host_puerto443=0
host_dominio=0
serv_http=0
apache=0
dionaea=0
nginx=0
otros=0

with f1 as input_file:
	"""
	Por cada linea que va leyendo va identificando las etiquetas correspondientes
	Al leer una linea, necesitabamos mas de un elemento, por lo cual utilizamos unas variables
	locales para identificar a que puerto correspondian.
	El valor lo separamos con split para identificar mas facilmente los elementos con los que
	contaba
	"""
	for line in input_file.readlines():
		puerto22_abierto=0
		puerto53_abierto=0
		puerto80_abierto=0
		puerto443_abierto=0
		nombre_http=0
		for valor in line.split():
			if "<host>" in line or "<host " in line:
				if valor=='state=\"up\"':
					host_prendidos+=1
					break
				if valor=='state=\"down\"':
					host_apagados+=1
					break			
			if "<port " in line or "<ports><port" in line:
					if valor=='portid=\"22\"><state':
						puerto22_abierto=1
					elif valor=='portid=\"53\"><state':
						puerto53_abierto=1
					elif valor=='portid=\"80\"><state':
						puerto80_abierto=1
					elif valor=='portid=\"443\"><state':
						puerto443_abierto=1
					if puerto22_abierto==1:
						#if valor=='state=\"open\"' or valor=='state=\"filtered\"':
						if valor=='state=\"open\"':
							host_puerto22+=1
							break
					elif puerto53_abierto==1:
						if valor=='state=\"open\"':
							host_puerto53+=1
							break
					elif puerto80_abierto==1:
						if valor=='state=\"open\"':
							host_puerto80+=1
							#jala los servidores http que estan abiertos, incluyendo a los que no tienen producto, por lo que la suma no resulta
							serv_http+=1
							nombre_http=1
					elif puerto443_abierto==1:
						if valor=='state=\"open\"':
							host_puerto443+=1
							break
					if nombre_http==1:
						if re.match('product=\"ngi.*',valor):
							nginx+=1
							break
						elif re.match('product=\"Apa.*',valor):
							apache+=1
							break
						elif re.match('product=\"Dio.*',valor):
							dionaea+=1
							break
						elif re.match('product=\".*',valor):
							otros+=1
							break
			if "<hostname " in line:
				host_dominio+=1
				break


hp = "La cantidad de host prendidos es: " + str(host_prendidos)
print hp
f2.write(hp+"\n")
ha = "La cantidad de host apagados es: " + str(host_apagados)
print ha
f2.write(ha+"\n")
p22 = "La cantidad de host con el puerto 22 abierto es: " + str(host_puerto22)
print p22
f2.write(p22+"\n")
p53 = "La cantidad de host con el puerto 53 abierto es: " + str(host_puerto53)
print p53
f2.write(p53+"\n")
p80 = "La cantidad de host con el puerto 80 abierto es: " + str(host_puerto80)
print p80
f2.write(p80+"\n")
p443 = "La cantidad de host con el puerto 443 abierto es: " + str(host_puerto443)
print p443
f2.write(p443+"\n")
hd = "La cantidad de host con con nombre de dominio es: " + str(host_dominio)
print hd
f2.write(hd+"\n")
http = "La cantidad de servidores HTTP incluyendo los que no tienen product usados es: " + str(serv_http)
print http
f2.write(http+"\n")
http2 = "La cantidad de servidores HTTP que solo tienen product usados es: " + str(apache+dionaea+nginx+otros)
print http2
f2.write(http2+"\n")
a = "		Con apache: " + str(apache)
print a
f2.write(a+"\n")
d = "		Con Dionaea: " + str(dionaea)
print d
f2.write(d+"\n")
n = "		Con Nginx: " + str(nginx)
print n
f2.write(n+"\n")
o = "		otros: " + str(otros)
print o
f2.write(o+"\n")


f1.close()
