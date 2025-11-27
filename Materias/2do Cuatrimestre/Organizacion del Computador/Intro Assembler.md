---
base: "[[Organizacion del Computador.base]]"
Fecha: 2025-08-21T19:17:00
Descripción: • Introduccion a Assembler
Diapos:
  - 2a23f454-0dd6-8062-93c7-c3c477850b86
  - 2a23f454-0dd6-805b-8da0-d5e2c604856f
---
# Instalacion de las Herramientas

# Compilado

## Introduccion

Compilar es el proceso de transformar un programa informatica escrito en un lenguaje en un programa equivalente en otro lenguaje.

Al programa que se encarga de realizar esta transformacion se le llama compilador.

Normalmente, un compilador transforma un lenguaje de alto nivel como C o Java, el cual es legible por los humanos (codigo fuente), en un lenguaje de maquina que la CPU peude procesar y ejecutar (codigo ejecutable)

## Codigo Intermedio

Este proceso de compilado tiene varias etapas, en las cuales se generan *codigos intermedios*, los que pueden ser codigo fuente modificado; pueden estar en un lenguaje *“assembler”*; o puede ser codigo* “objeto”*.

Estos codigos intermedios se pueden ver en distintos archivos que brindan informacion sobre como fue realizado el proceso de compilacion desde el codigo fuente al codigo ejecutable.

![](../../../images/diagrama-etapas-compilado.png)

### Analisis

A veces es necesario analizar el codigo generado en las distintas etapas intermedias, algunas razones son:

- **Desempeño**: viendo la forma en que se genera el codigo ejecutable es posible encontrar formas mas eficientes de ejecutar un algoritmo, donde la eficiencia puede ser mayor velocidad de ejecucion, menor tamaño de codigo ejecutable, o menor espacio de memoria necesario para ejecutar el algoritmo.
- **Busqueda de Errores**: algunos errores muy sutiles surgen por la forma en que se realiza la transformacion del codigo fuente en codigo ejecutable (*”side effects”*).
- **Comprension de la Influencia del Hardware**: viendo las secuencias de instrucciones que van a ser procesadas por la CPU, es posible ver los condicionamientos que el hardware impone a la implementacion de un algoritmo. Estos condicionamientos relacionados con el tamaño de las unidades de informacion (tamaño de palabra) o de procesamiento (unidades SIMD), o la cantidad y tipo de accesos a las distintas memorias del sistema.

## Preprocesamiento

En esta etapa se realizan las siguientes actividades:

### **Empalmado de Lineas**

Las lineas de codigo que continuan con secuencias de escape de nueva linea son unidas para formar lineas logicas.

### **Tokenizacion**

Reemplaza los comentarios por espacios en blanco. Divide cada uno de los elementos a preprocesar para formar lineas logicas.

### **Expansion de Marcos**

Ejecuta las lineas con directivas de preprocesado particularmente las que incluyen otros archivos y las de compilacion condicional. Ademas expande las macros. Desde la version de C de 1999 tambien gesitiona los operadores #Pragma.

## Compilado

En esta etapa el codigo fuente preprocesado es convertido a un codigo intermedio en lenguaje Assembler, el cual es un lenguaje de bajo nivel que representa instrucciones basicas que puede realizar el procesador.

## Ensamblado

En la etapa de *ensamblado *el codigo en lenguaje Assembler es convertido en Codigo Objeto, el cual esta en lenguaje de maquina, generandose el archivo “ejemplo.o”

El codigo fuente se ha convertido a un lenguaje que entiende el procesador, pero solo se encuentra el codigo correspondiente al archivo fuente. Asi, por ejemplo, el codigo correspondiente a la funcion pirintf no se encuentra en este archivo, sino en un archivo “printf.o”.

Por otra parte, todas las referencias a posiciones de memoria son relativas, por lo que este archivo no puede ser ejecutado.

## Enlazado

- Se unifican todos los archivos objeto (en este caso ejemploC.o y printf.o)
- Se resuelven las referencias a posiciones de memoria, pasando a ser todas absolutas (indirecciones, saltos, etc)
- Se resuelven todos los símbolos que no hubieran sido definidos en etapas
anteriores
- Se genera un único archivo ejecutable “hello”.

# Consideraciones finales

El análisis de los archivos intermedios nos permite ver como es el proceso de
transformación desde el Código Fuente (lenguaje humano) hasta el Código Ejecutable (lenguaje del procesador).