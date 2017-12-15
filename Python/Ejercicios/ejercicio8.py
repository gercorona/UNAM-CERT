from re import *
#Verificacion de direcciones IPv4
direccion_ip = r"([0-9]\.|[1-9][0-9]\.|1[0-9][0-9]\.|2[0-4][0-9]\.|25[0-5]\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
dir_IPv4 = "132.248.1.7"
if match(direccion_ip,dir_IPv4):
    print dir_IPv4 + " es una IPv4 Valida"
else: 
    print dir_IPv4 + " es una IPv4 no valida"

#Verificar formato de correo valido
email = r"^[a-zA-Z]([a-zA-Z]|[0-9]|_|\.|-)*@[a-zA-Z](\.|-|[a-zA-Z])*[a-zA-Z]$"
direccion_correo = "gerardo.corona@bec.seguridad.unam.mx"
if match(email,direccion_correo):
    print direccion_correo + " Tiene formato correcto"
else:
    print direccion_correo + " Tiene formato incorrecto"