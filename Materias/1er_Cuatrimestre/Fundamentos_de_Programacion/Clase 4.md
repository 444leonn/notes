---
base: "[[Fundamentos de Programacion.base]]"
Descripcion: Organización física de un computadora, Mapa de memoria, Punteros, Bibliografía complementaria, Preguntas
Fecha: 2025-05-28T22:58:00
Archivo: []
---
# Punteros

Un puntero en es una variable que almacena como valor una dirección de memoria. 

El tamaño de este tipo de variables es de 8 bytes (en arquitecturas de 64 bits y 4 bytes en arquitecturas de 32 bits).

Será de utilidad almacenar la dirección de alguna variable como valor del puntero, para poder manipular el valor de la variable original.

Los punteros pueden ser inicializados con el valor NULL o 0, cuando no se quiere almacenar una dirección en ellos.

*Ejemplo:*

Podemos obtener la dirección de una variables anteponiendo el carácter & (ampersand). Incluso podemos conocer la dirección donde está alojado el propio puntero.

Para acceder o modificar el valor de lo apuntado por el puntero, debemos desreferenciar al mismo con la siguiente notación.