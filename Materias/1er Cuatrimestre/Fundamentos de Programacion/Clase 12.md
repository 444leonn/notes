---
base: "[[Fundamentos de Programacion.base]]"
Descripcion: Recursividad
Fecha: 2025-06-18T16:55:00
Archivo: []
---
# Memoria

Hasta ahora trabajamos con un modelo muy simplificado del manejo de memoria en lenguaje C, pero nos alcanzo para comenzar a programar en este lenguaje.

![[image 16.png]]

![[image 17.png]]

## Punteros: Repaso de Variables

Desde el punto de vista del programador, las variables en el lenguaje C tienen 4 elementos que demeos tener presenta:

¿Como puedo conocer la posicion de memoria?

¿Como puedo acceder a la variable conociendo su posicion de memoria?

# Pila de Ejecucion (Call Stack)

![[image 18.png]]

Es una estructura dinamica de datos LIFO (acronimo incles de Last In, First Out), donde se guarda la informacion sobre las funciones que se estan ejecutando en cada momento.

Como vamos a ver mas adelante en el *debugger* (depurador), en C se administra automaticamente y -en realidad- la estamos utilizando desde comenzamos a modularizar.

<!-- Column 1 -->
- Cada vez que se invoca a una funcion, en *“la pila” *se almacena:
    - Variables locales de la funcion
    - Direccion de Retorno
    - Parametros de Invocacion
Por ejemplo:

<!-- Column 2 -->
![[Captura_desde_2025-06-18_17-13-43.png]]


## Desbordamiento de Pila

El desbordamiento de pila (en ingles Stack overflow) es un error que ocurre cuando la pila de llamadas del programa no puede almacenar más datos, lo que provoca la terminación del programa.

# Recursividad

La recursividad (en algunos textos llamada recursion, dado que en ingles se denonima *recursion) *es una tecnica de programacion en el cual una funcion se invoca a si misma.

Es una alternativa diferente para implementar soluciones iterativas (estructuras de repeticion o ciclos)

## Funcion Recursiva

Las funciones recursivas se componen de:

## Caso Base

Una solucion simple para un caso particular (puede haber mas de un caso base)

## Caso Recursivo

Una solucion que involucra volver a utilizar la funcion original, pero con parametros que se acercan mas al caso base.

## Ejemplo Factorial

Escribir un programa que calcule el factorial (!) de un entero no negativo. He aquí algunos ejemplos de factoriales:

0! = 1

1! = 1

2! = 2    → 2 * 1

3! = 6    → 3  *2*  1

4! = 24   → 4  *3*  2 * 1

5! = 120  → 5  *4*  3  *2*  1

La imagen muestra una fórmula matemática que define el factorial (N!) de la siguiente manera:

N! = {

1                si N = 0  (base)

N * (N-1)!      si N > 0  (recursión)

### Iterativo

```c
int factorial_iterativo (int numero) {
	int i, fact = 1;
	for  (i = 1; i <= numero; i++)
	     fact = i * fact;
	return fact;
}
```

### Recursivo

```c
int factorial(int numero) {
	if (numero == 0) // Caso Base
		return 1;
	else {
		return numero * factorial(numero - 1); // Caso Recursivo
	}
}
```

![[image 19.png]]

Vemos entonces que la implementacion recursiva requiere mas recursos que la iterativa

## Por que escribir programas recursivos?

- Pueden resultar mas cercanos a la descripcion matematica.
- A veces la implementacion es mas facil de analizar.
- Se adaptan mejor a las estructuras de datos recursivas.
- Muchas veces los algoritmos recursivos ofrecen soluciones estructuradas, modulares y elegantemente simples.

### Ejemplo

Un ejemplo de una implementación "más cercanos a la descripción matemática" se da en el caso de la Sucesión de Fibonacci, que se define como una sucesión infinita de números naturales que comienza con dos números naturales (dependiendo de la referencia, con 0 y 1 en ciertos casos, otras inician con 1 y 1) y a partir de estos, «cada término es la suma de los dos anteriores»

0,1,1,2,3,5,8,13,21,34,...

## Comparando Recursividad VS Iteracion

Comparando Recursividad vs Iteración

Repetición:

Terminación:

En ambos casos podemos tener ciclos infinitos

Al utilizar Recursividad existe el riesgo de tener un desbordamiento de pila (Stack overflow)

## Clasificacion de Recursividad

### Directa

- Cuando una función incluye una llamada a sí misma

### Indirecta

## Cuando es Factible usar Recursividad

- Cuando una función llama a otra función y ésta causa que la función original sea invocada

Factible de utilizar recursividad:

No factible utilizar recursividad:

- Cuando los métodos usen arreglos largos.
- Cuando el método cambia de manera impredecible de campos.
- Cuando las iteraciones sean la mejor opción.

## Consideracion a la hora de Elegir Solucion Recursiva o Iterativa

Se debe considerar que resulta más positivo para cada problema

LA RECURSIVIDAD SE DEBE USAR CUANDO SEA REALMENTE NECESARIA, ES DECIR, CUANDO NO EXISTA UNA SOLUCIÓN ITERATIVA SIMPLE.

## Ejemplo - Secuencia de Fibonacci

<!-- Column 1 -->
```c
#include <stdio.h>
int fibonacci(int numero) {
    if (numero <= 1)
        return numero;
    else
        return fibonacci(numero-1) + fibonacci(numero-2);
}
```

<!-- Column 2 -->
![[33b70259-9e28-419e-80c4-2f947535ebe1.png]]


## Ejemplo - Busqueda Binaria

<!-- Column 1 -->
```c
#include <stdio.h>

int buscar(int[] numeros, int numero, int inicio, int fin) {
    int centro = (inicio + fin) / 2;
    
    if (fin < inicio) {
        return -1;
    }
    else {
        if (numero < numeros[centro]) {
            return buscar(numeros, numero, inicio, centro - 1);
        }
        else {
            if (numero > numeros[centro]) {
                return buscar(numeros, numero, centro + 1, fin);
            }
            else {
                if (numero == numeros[centro]) {
                    return centro;
                }
                else {
                    return -1;
                }
            }
        }
    }
}
```

<!-- Column 2 -->
![[9933f444-1f94-4e11-82f3-a3ba083bc305.png]]

## Recursividad - Ejercicios

### 1- Mostrar X primeros Números Naturales

Orden Ascendente: 

```c
void mostrar_naturales_ascendente(int num) {
	if (num <= 0)
		printf("Error %d no es un numero natural.\n", &num);
	else {
		mostrar_naturales(num - 1);
		printf("%d", num);
	}
}
```

Orden Descendente:

```c
void mostrar_naturales_descendente(int num) {
	if (num <= 0)
		printf("Error %d no es un numero natural.\n", &num);
	else {
		printf("%d", num)
		mostrar_naturales(num - 1);
	}
}
```

### 2- Sumar los dígitos un número

```c
int sumar_digitos(int numero) {
    if (numero < 10)
        return numero;
    return numero % 10 + sumar_digitos(numero / 10);
}
```

### 3- Mostrar números pares entre 1 y X

```c
void mostrar_pares(int numero) {
	if (numero <= 0) {
		return;
	}
	else {
		if (numero % 2 == 0) {
			mostrar_pares(numero - 2);
			printf("%d ", &numero);
		}
		else {
			mostrar_pares(numero - 1);
		}
	}
}
```

### 4- Mostrar de a uno los dígitos de un Número

```c
void mostrar_digitos(int numero) {
	if (numero <= 0) {
		return;
	}
	else {
		mostrar_digitos(numero / 10);
		printf("%d ", numero % 10);
}
```

### 5- Una función recursiva en C que suma los elementos en las posiciones pares de un arreglo

```c
int suma_posiciones_pares(tvec arreglo, int ml) {
    if (ml == 0)
        return 0;
    else {
        if (ml % 2 == 0)
            return arreglo[ml] + suma_posiciones_pares(arreglo, ml - 2);
        else
            return suma_posiciones_pares(arreglo, ml - 1);
    }
}
```