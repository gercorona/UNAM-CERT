#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Gerardo Corona Lopez

aprobados = []
lista = ['GerARdo', 'AlAN', 'GuadaLUPE', 'RaFael', 'KARIna']
becarios2 = []
def aprueba_becario(nombre_completo):
    nombre_separado = nombre_completo.split()
    for n in nombre_separado:
        if n.upper() in str(lista).upper(): #Validacion de becarios
            return False
    nombre_completo = nombre_completo.upper() #usuarios en mayuscula
    aprobados.append(nombre_completo) # insertar usuarios en mayuscula
    aprobados.sort() #Ordenar despues de la insercion
    return True

#Funcion que crea una nueva lista con el usuario eliminado
def borrar_becario(nom_a_borrar):
    for nombres in becarios:
        if nom_a_borrar in nombres:
            becarios2.append("Becario eliminado")#Indica el becario eliminado
        else:
            becarios2.append(nombres)
        
    if becarios == becarios2:
        return False
    else:
        return True


becarios = ['Becerra Alvarado Hugo Alonso',
            'Cabrera Balderas Carlos Eduardo',
            'Corona Lopez Gerardo',
            'Diez Gutierrez Gonzalez Rafael',
            'Disner Lopez Marco Antonio',
            'Garcia Romo Claudia Fernanda',
            'Gonzalez Ramirez Miguel Angel',
            'Gonzalez Vargas Andrea Itzel',
            'Orozco Avalos Aline Karina',
            'Palacio Nieto Esteban',
            'Reyes Aldeco Jairo Alan',
            'Santiago Mancera Arturo Samuel',
            'Sarmiento Campos Jose',
            'Sarmiento Campos Maria Guadalupe',
            'Valle Juarez Pedro Angel',
            'Viveros Campos Ulises']

for b in becarios:
    if aprueba_becario(b):
        print 'APROBADO: ' + b
    else:
        print 'REPROBADO: ' + b

#Agrega una funcion que permita borrar a 
print "\nPrint de la funcion borrar_becario"
eliminacion = borrar_becario("Gerardo")
#Impresion de la nueva lista con el becario eliminado (Si existia)
print becarios2 
#True si se pudo eliminar, False si es que el becario no existe
print "Se pudo eliminar el becario? " + str(eliminacion)