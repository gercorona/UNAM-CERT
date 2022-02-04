Practica 14.
============
Numeros aleatorios.
___________________
Hay dos formas de genrar numeros aleaotrios, como los egresados de alguna licenciatura o como los integrantes de PBSI.

Recuerda que todo es un archivo, lee los bytes necesarios del "device" /dev/random en tu equipo, para generar un numero aleatorio, que pueda ser alojado en un entero.

La funcion read() recibe descriptor de archivo, direccion de la variable en la que se almacenaran los bytes leidos, y los bytes a leer.
