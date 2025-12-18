---
base: "[[Organizacion del Computador.base]]"
Fecha: 2025-08-18T10:52:00
Descripción: • Introduccion a la Materia
Diapos: []
---
# Algunas Anotaciones

# Introducción a los Sistemas Digitales

## Señales Analógicas

Son variables eléctricas continuas en el tiempo, pueden ser en forma de una corriente, una tension o una carga eléctrica.

- Varia en forma continua entre un limite inferior y un limite superior

Para señales periódicas podemos definir ciertos parámetros como el periodo $T$

## Señales Digitales

Son variables eléctricas con dos niveles: *0 *o 1

Su variación en el tiempo contiene la información acorda a una codificación a utilizar.

## Teorema de Nyquist

Define la frecuencia minima de muestreo para poder reconstruir una señal anologica en base a su muestreo.

- $FM:$ Frecuencia de muestreo
- $FS:$ Frecuencia señal

El teorema estable que $FM >= 2*FS$

### Conversor A/D

### Muestreador

Ingresa una señal analógica* “A” *pasando por un circuito* “muestreador o discretizador”.*

Este toma muestras acorde a la *FM*. Una vez tomadas, genera una nueva señal* “B” *que posee ya no infinitos puntos como la analógica, sino finitos.

### Conversor o Codificador

La señal* “B” *ingresa al conversor para convertir los finitos puntos de tension o corriente (o la variable que sea), a valores binarios a traves de una tabla de conversion, obteniendo de esta manera la señal de salida.

# Introducción a Sistemas de Numeración

## Sistema de Numeracion

Es un conjunto finito de simbolos que se empleada para la asignación de valores numéricos.

Existen los posicionales y los no posicionales

### Sistemas No Posicionales

Los digitos tienen el valor del simbolo en particular designado

### Sistemas Posicionales

El valor de un dígito depende tanto del símbolo utilizado, como también, de la posición en la que se encuentra.

Vimos como el decimal es un sistema posicional, de la misma manera aplica para sistemas posicionales en otras bases, cuyos símbolos permitidos están en la siguiente tabla.

![](../../../images/sistema-numeracion.png)

### Ejemplo de números Decimales

- 12698 (Base 10) = 10000 + 2000 + 600 + 90 + 8
$1 * 10^4 + 2 * 10^3 + 9*10^1 + 8*10^0$
= Sumatoria (( numero * (base ^ posición))

## Cambios de Base

### De base 10 a Cualquier Base

Se divide el numero decimal por la base destino.

### De cualquier base a base 10

Se aplica el concepto de pesos de la posición

> [!tip] 💡
> Notese que los binarios que terminan en “1” son numeros impares

# Convenciones Signadas

## Valor Absoluto y Bit de Signo (VA y BS)

Una representación en formato de VA y Signo nos permite codificar un entero con *x cantidad de bits* (ej. 8 bits) , tomando 7 bits de valor modulo y el bit mas significativo como signo (7 + 1)

### Ejemplo: 

- 1 bit para el signo y 7 bits para la magnitud, son 8 bits totales que podemos representar tanto para la parte positiva y negativa. $2^8 = 256$ números (del 0 a 255 en binario natural). En VA y BS van a estar repartidos entre 128 numeros positivos (bit de signo 0) y 128 numeros negativos (bit de signo en 1).
    - 00000000: 1 en binario, es al mismo tiempo 1 en VAyBS

Si quisiera representar el -1, pondria el $MSB = 1$, lo que implica el signo negativo, y el resto seria modulo: $10000001$

Siendo asi el $MSB = 0$, implican numeros positivo, el $MSB=1$ implica numeros negativos.

Con 8 bits en binario represento un rango de 0-255, en VAyBS represento (-127; +127) teniendo doble representacion del cero (00000000; 10000000).

## Complemento a 2 o a la base (CA2)

Es similar a la anterior, solo que para hallar el modulo de un numero negativo se invierten 0 x 1 y viceversa, sumando 1 al resultado

Tomando el ejemplo anterior, 11111110 sabemos que el numero es negativo

# Operaciones Signadas y Flags

Supongamos la representacion de los numeros 43 y 8 (ambos en base 10) en binario.

Recuerden que no dividimos x 2, usamos los pesos de las posiciones.

8 (base 10) = 00001000.

43 (base 10) = 00101011

Si recordamos las tablas de las convenciones signadas, sabemos que un binario de 8 bits tiene un Rango de (0, 255), mientras que si usamos las convenciones de ese rango ya pasa a tomar numeros negativos pues ahora utiliza el MSB como signo. De esta manera en CA2, 8 bits tendran un rango de (-128; 127) y CA1 (-127; 127)
