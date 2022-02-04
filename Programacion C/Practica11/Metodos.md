Metodos para encontrar el password de ./help_me
===============================================
_______________________________________________

+ # Se obtuvo la contraseña instalando dos librerias. Ademas de una aplicación indicado en la guia de ayuda. 

+ # La aplicación ltrace se instaló como se ve a continuación:

![comando](https://bytebucket.org/gercorona/programacion-en-c/raw/b6d793b2fffb1c54a01d0db147a656c52335905b/Practica11/Imagenes/comando.png?token=8309c8f79612da7b084c0be0b4453dcb7a05905d)

+ # Las dos librerias se instalaron como se ve a continuación:

![libreria1](https://bytebucket.org/gercorona/programacion-en-c/raw/b6d793b2fffb1c54a01d0db147a656c52335905b/Practica11/Imagenes/libreria1.png?token=1f300a94bc2f893434deb9a895abe508595b2f96)

![libreria2](https://bytebucket.org/gercorona/programacion-en-c/raw/b6d793b2fffb1c54a01d0db147a656c52335905b/Practica11/Imagenes/libreria2.png?token=bfe68714c894175f1777d174874cb6d2dc0a50ee)

+ # Se obtuvo la contraseña ejecutando la aplicación como se indica en la guia. Obsrvamos que en pantalla nos muestra una cadena ("hola :)") después de un indicador "strcmp" sabiando que se esta comparando un argumento con esa cadena, por lo tanto podemos asumir que esa es la contraseña que pide el programa help_me. 

![comparacion](https://bytebucket.org/gercorona/programacion-en-c/raw/b6d793b2fffb1c54a01d0db147a656c52335905b/Practica11/Imagenes/comparacion.png?token=17f865aaba477549f9921c613a51d18aee85741e)

+ # El siguiente metodo es, con el comando strings, obtener información o las cadenas visibles del binario, en donde podemos encontrar de nuevo la cadena "hola :)".

![metodo2](https://bytebucket.org/gercorona/programacion-en-c/raw/9726ba74c175a2b41b320ad699bb28544fcb92cb/Practica11/Imagenes/Metodo2.png?token=21908adf0a46716fbea6eb235405f2a118ef9625)

+ # Se puede comprobar que "hola :)" es la contraseña correcta:

![comprobacion](https://bytebucket.org/gercorona/programacion-en-c/raw/9726ba74c175a2b41b320ad699bb28544fcb92cb/Practica11/Imagenes/comprobacion.png?token=c960668838e25adf5de497afc5880cd78143d72b)






