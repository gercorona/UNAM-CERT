Practica 3.
===========
Fin del mundo.
_______________
El tiempo en la mayoria de los sistemas derivados de UNIX, se mide en segundos transcurridos desde el 1 de enero del 1970, esta dato no se ha cambiado desde entonces, la sincronizacion de los servdores que mueven al mundo se basan en este contador.

El problema es que esta variable tiene un limite, y cuando se alcance este limite algo interesante sucedera.

¿Puedes hacer un programa que diga la fecha exacta de este suceso?

+ La variable se almacena en un tipo de dato int de 32 bits.
+ time.h define el tiepo de dato time_t y la funcion ctime(), la cual regresa una cadena con formato de fecha.
