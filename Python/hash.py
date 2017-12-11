import hashlib

def hash_md5(archivo):
    hash = hashlib.new("md5", archivo)
    return hash

def hash_sha1(archivo):
    hash = hashlib.new("sha1", archivo)

archivo = open ('nmap.xml','r')
contenido= archivo.read()
archivo.close()
hash_md5(contenido)
hash_sha1(contenido)
