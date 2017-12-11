import hashlib

def hash_md5(archivo):
    hash = hashlib.new("md5", archivo)
    return hash

def hash_sha1(archivo):
    hash = hashlib.new("sha1", archivo)
    return hash

archivo = open ('nmap.xml','r')
contenido= archivo.read()
archivo.close()
md5 = hash_md5(contenido)
sha1 = hash_sha1(contenido)
print sha1.hexdigest()
print md5.hexdigest()
