---
base: "[[Algoritmos y Estructuras de Datos.base]]"
Grabacion: https://youtu.be/6Q_EaxQgUxY?si=RB38noZXfmyWWjv4
Descripcion: Introduccion a la Materia y Manejo de Memoria
Fecha: 2025-08-19T15:20:00
Archivo:
  - 2543f454-0dd6-80a5-ad45-d3536f02eb36
  - 2543f454-0dd6-8055-b41b-f403bfac7947
---
Un programa puede encontrarse en varias etapas:

- *Edicion*
- *Compilacion*
- *Ejecucion*

En cada una de las etapas el programa tiene una estructura distinta.

En *Edición *el programa solo es un archivo de texto editado en el lenguaje seleccionado por el programador *(en este caso “C”)*, esto se denomina *Codigo Fuente.*

Una vez el código fuente del programa se encuentra listo, se utiliza un conjunto de programas para traducir el código fuente, a un lenguaje que la computador pueda ejecutar.

Este programa es el ***Compilador***

# Compilador

Tiene la tarea de ==traducir el código fuente del programa a una estructura que una computadora pueda ejecutar.==

Este no es un proceso sencillo, y se encuentra compuesto por varias etapas.

## Lexer: Análisis Lexicógrafo

En esta primera etapa el *Lexer *es el ==encargado de leer el archivo de codigo fuente y generar unidades atomicas==.

Para ello lee el programa de izquierda a derecha y agrupa en **componentes léxicos**(tokens), que son secuencias de caracteres que tienen un significado, *extrae las palabras.*

Ademas, todos los espacios en blanco, lineas en blanco, comentarios y demás información innecesaria se elimina del programa.

También se comprueba que los símbolos del lenguaje se han escrito correctamente.

## Parser: Análisis Sintáctico y Semántico

Los caracteres o componentes léxicos se agrupan jerarquicamente en frases gramaticales que el compilador utiliza para sintetizar la salida.

Se comprueba si lo obtenido en la fase anterior es sintacticamente correcto (obedece a la gramática del lenguaje).

Por lo general, las frases gramaticales del programa fuente se representan mediante un árbol de análisis sintáctico.

La fase de análisis semántico revisa el programa fuente para tratar de encontrar errores semánticos y reúne la información sobre los tipos para la fase posterior de generación de código. En ella se utiliza la estructura jerárquica determinada por la fase de análisis sintáctico para identificar los operadores y operandos de expresiones y proposiciones.

Un componente importante del análisis semántico es la verificación de tipos. Aquí, el compilador verifica si cada operador tiene operandos permitidos por la especificación del lenguaje. Por ejemplo, las definiciones de muchos lenguajes de programación requieren que el compilador indique un error cada vez que se use un número real como índice de una matriz. Sin embargo, la especificación del lenguaje puede imponer restricciones a los operandos, por ejemplo, cuando un operador aritmético binario se aplica a un número entero y a un número real. Revisa, también, que los arreglos tengan definido el tamaño correcto.

## Generador de Código Intermedio

Después de los análisis sintáctico y semántico, algunos compiladores generan una representación intermedia explícita del programa fuente. Se puede considerar esta representación intermedia como un programa para una máquina abstracta que debe tener dos propiedades importantes:

- Ser fácil de producir
- Ser fácil de traducir al programa objeto

La representación intermedia puede tener diversas formas. Existe una llamada **código de tres direcciones** que es como el lenguaje ensamblador de una máquina en la que cada posición de memoria puede actuar como un registro.

## Generador de Código Objeto

Una vez compilado el código fuente del programa, gracias a la acción del compilador y el link editor, toma forma como un archivo en formato objeto, el cual es posible ejecutar en una computadora (comando: objdump -d). Por último, este programa objeto que está guardado en un dispositivo de almacenamiento es capaz de cobrar vida, al ser ejecutadas sus instrucciones por el procesador de la computadora. En esta etapa pasa a ser una entidad con "vida" (dinámica) la cual se divide en ciertas secciones. Estas son:

### **Código (.code)**

En esta sección del programa se almacenan el código del mismo, una vez traducido por el compilador.

### **Datos (.data)**

En esta sección se almacena los datos de los valores literales y valores globales del programa. Se almacenan las constantes globales, variables externas y valores literales del programa.

### **Pila de ejecución (execution stack o .stack)**

Se almacenan todas las variables locales de las funciones que se encuentran en ejecución.

Y no existe hasta que el programa es ejecutado.

### **Montículo (.heap)**

No existe hasta que el programa es ejecutado.

Cada una de estas secciones guarda distinto tipo de información perteneciente al programa.

Está reservada a la denominada memoria dinámica, la misma es memoria que puede estar disponible para ser utilizada por el programador en tiempo de ejecución.

La memoria dinámica no es reservada por el compilador, sino que por lo contrario es manejada por el programador, en tiempo de ejecución del programa. Una de las implicaciones de esto es que no se sepa a priori la cantidad a ser reservada, sino hasta el momento en que es necesario reservarla.

## Comentarios

Normalmente estas tres secciones (.code, .data. y .stack) son controladas exclusivamente por el compilador, el programador no tiene forma de alterar estas secciones. El compilador es el que estructura la información que debe ir en esas secciones sin que el programador pueda hacer ninguna otra modificación tras haber compilado el programa.

Para que un programa compilado, que está almacenado en un disco, pueda ser ejecutado debe ser cargado directamente en la memoria RAM. De esta tarea se encarga el sistema operativo.

El mismo lee la estructura del programa compilado y teniendo en cuenta la memoria RAM, reserva espacio para las cuatro secciones (.code, .data, .stack y .heap).
