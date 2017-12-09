#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']


#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION
#filter(lambda variable: filtro in variable,parametro que se asignara a variable)
#map(lambda variable: variable.funcion(), parametro que se asignara a variable)

print (lambda cadena: ','.join(cadena))(map(lambda nombre: nombre.upper(),(filter(lambda nombre: 'i' in nombre,(lambda x,y,z,w:x+y+z+w)(sistemas,op_interna,incidentes,auditorias)))))