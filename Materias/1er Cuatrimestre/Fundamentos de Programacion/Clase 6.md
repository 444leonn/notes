---
base: "[[Fundamentos de Programacion.base]]"
Descripcion: Arreglos (arrays)
Fecha: 2025-05-28T22:58:00
Archivo: []
---
# Arreglos en C

## Que es un Arreglo en C?

Un ***arreglo ***es una coleccion finita y ordenada de datos <u>**homogeneos**</u> →Son todos del mismo Tipo

Estractura Estatica (en C) —> Se define en tiempo de diseñoNo puede ser redimensionado

Acceso directo a un elemento del arreglo →  A través de su posición en el arreglo

### Clasificacion

- Unidimensionales: Vectores - Listas
- Bidimensionales: Matrices - Tablas
- Multidimensionales: Dimension N

## Unidimensionales - Vectores

![[vectores.png]]

### Acceso a los Elementos

El primer elemento ocupa la posición 0 del arreglo (vector), por lo tanto en un arreglo de N elementos, el último de los elementos estará en la posición N-1

***Arreglo V de N elementos: v[n]***

## Bidimensionales - Matrices

![[matrices.png]]

## Acceso a los elementos

El primer elemento ocupa la posición 0,0 del arreglo (matriz), por lo tanto en un arreglo bidimensional de NxMelementos, el último de los elementos estará en la posición [ N-1 , M-1 ]

***Arreglo M de NxM elementos: v[n]***

## Declaracion

Debemos indicar, tipo de los elementos, un nombre y la cantidad de/ elementos en cada dimensión

`tipo ``nombre_arreglo``[cantidad_elementos]`

<u>***Arreglos Unidimensionales***</u>


<u>***Arreglos Bidimensionales***</u>

## Restricciones

Los parámetros de tipo arreglo serán pasados siempre por referencia, sin necesidad de indicarlo con el símbolo &.

No se pueden asignar ni comparar arreglos directamente, hay que asignar o comparar sus elementos uno a uno.

vec_1 = vec_2  MAL

`for (i=0; i<100; i++) vec_1[i] = vec_2[i]` BIEN

## Declaracion de Tipos de Datos

Es conveniente declarar tipos de datos para nuestros arreglos.

La sintaxis para declarar un tipo es la siguiente:

# Maximo Fisico vs Maximo Logico

## Maximo Fisico

Se refiere al limite que tiene nuestro arreglo realmente en terminos de datos posibles a almacenar debido a los espacios de memoria reservados que se definen.

## Maximo Logico

Se refiere a los valores que tenemos en nuestro arreglo en uso, los cuales pueden ser una cantidad menor al maximo fisico del arreglo.

Los maximos logicos pueden ser internos o externos:

### Internos

El maximo interno se utiliza

### Externos

El maximo logico ***externo ***nos permite utilizar una variable externa al Arreglo, para definir el limite en que nosotros vamos a tener nuestro maximo logico.

# Estructura Basica de un Programa

```c
#include LIBRERIAS

#define CONSTANTES

typedef TIPOS

FUNCIONES

int main() {
	--- codigo ---
	
	return 0;
}
```