---
base: "[[Fundamentos de Programacion.base]]"
Descripcion: Programacion Estructurada y Modular, Funciones.
Fecha: 2025-05-28T22:58:00
Archivo: []
---
# Programacion Estructurada y Modular

Significa escribir un programa que cumpla con las siguientes reglas:

1. ***Diseño Modular: ***Implicar dividir un problema en problemas mas pequeños. “Descomponer el programa en modulos independientes.
2. ***Diseño Descendente sobre los Modulos:*** “Refinamiento - Stepwise”, subdividir sucesivamente los modulos hasta que cada modulo tenga <u>solo una tarea especifica</u> a ejecutar.
3. ***Cada modulo debe ser codificado utilizando las estructuras de control basicas.***

Nos detemos cuando un modulo resuelva o de soluciones especificas a un problema en particular.

Los items **1 **y **2 **se corresponden con el **Diseño Estructurado **y la **Propiedad de Modularidad.** El item **3 **se corresponde mas con el **Teorema del Programa Estructurado.**

Esto se da con varios objetivos los cuales son:

### Diagrama Modular Completo

![[diagrama-programa.png]]

# Funciones

Ahora nosotros vamos a comenzar a programar nuestras propias funciones.

## Algunas Funciones ya Conocidas por Nosotros

Estas funciones son algunas de las cuales el lenguaje C nos provee para que utilizemos.

| Funcion | Breve Descripcion |
| --- | --- |
| scanf | Permite el ingreso de datos |
| printf | Permite imprimir elementos |
| strlen | Devuelve la longitud de una cadena |
| strcpy | Permite asignar un nuevo valor a una cadena |
| strcat | Permite concatenar valores de una cadena |
| strcmp | Permite comparar 2 cadenas |
| strstr | Busco una cadena en otra cadena |

## Declaracion de Funciones en C

4. Debemos indicar el **Tipo a Devolver.**
5. Luego indicamos el **Nombre** de la funcion.
6. Y entre parentesis vamos a indicar los **parametros formales** (cuando invocamos a la funcion se dicen “parametros actuales”)
7. El cuerpo de la funcion encerrado entre llaves.
8. Por ultimo el **return **que puede retornar o no un valor.

![[funcion-en-c.png]]

### Pasaje de Parametros

Si yo no necesito devolver el parametro modificado lo paso por valor. Porque en ese caso se entrega una copia del parametro actual

Si el parametro formal se devuelve modificado, y me interesa devolverlo modificado, requiere que se pase por referencia.

- Por **Valor: **se entrega una copia del valor del parametro actual. Los parametros Actuales y los Formales utilizan distintas posiciones de memoria.
- Por **Referencia: **Se entrega una referencia (direccion de memoria) al parametro actual. Los parametros Actuales y los Formales utilizan la misma posicion de memoria en este caso.

Hay parametros que siempre deberemos pasar por referencia.

# Algunos Conceptos de Modularizacion

## Funciones

- ***Funciones con Tipo:*** Devolver un solo valor con return.
- ***Funcion Void: ***Realizar una accion que no sea devolver un valor.

## Cohesion

Hace referencia a cuando cada modulo realiza una unica tarea trabajando sobre una sola estructura de datos.

Un alto grado de cohesion seria cuando las funciones o modulos realizan tareas unicas y mas especificas.

## Acoplamiento

Hace referencia al grado de interaccion entre los modulos.

El grado de acoplamiento seria cuando los modulos tiene poco o baja relacion entre ellos, haciendolos mas independientes.

Alto acoplamiento → Baja relacion

Bajo Acolpamiento → Alta relacion

