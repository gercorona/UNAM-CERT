#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Gerardo Corona Lopez
from random import choice

aprobado = []
reprobado = []
calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

#funcion que determina si esta aprobado o reprobado el alumno
def retorna():
    promedio=[]
    for i in becarios:
        if calificacion_alumno[i]>=8:
            aprobado.append(i)
            promedio.append(calificacion_alumno[i])
        else:
            reprobado.append(i)
            promedio.append(calificacion_alumno[i])
    alumno_aprobado = tuple(aprobado)
    alumno_reprobado = tuple(reprobado)
    prom=promedios(promedio)
    #print promedio # para ver todas las calificaciones de los becarios
    #conjunto_promedio = set(promedio) Alternativa para crear el conjunto sin llamar a la funcion
    conjunto_promedio = conjunto(promedio) 
    #Regresa la lista de los alumnos aprobados, alumnos reprobados, el promedio de todas las 
    #calificaciones y el conjunto de estas calificaciones. 
    return alumno_aprobado,alumno_reprobado,prom,conjunto_promedio
    
#Funcion que saca el promedio de las calificaciones obtenidas por los becarios
def promedios(promedio):
    total = 0
    for i in promedio:
        total += i
    return float(total) / len(promedio)
#Funcion que asigna las calificaciones a un conjunto y devuelve el conjunto
def conjunto(promedio):
    conjunto = set(promedio)
    return conjunto
    

asigna_calificaciones()
#imprime_calificaciones()
a = retorna()
print "Aprobados: " + str(a[0])
print "Reprobados: " + str(a[1])
print "Promedio de calificaciones: " + str(a[2])
print "Conjunto Promedio:" + str(a[3])
