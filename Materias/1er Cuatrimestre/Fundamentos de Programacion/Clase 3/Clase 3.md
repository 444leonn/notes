---
base: "[[Fundamentos de Programacion.base]]"
cover: "[[banner-c-program.png]]"
Descripcion: "Introduccion a C: Variables, Estructuras Condicionales e Iterativas, Creacion Entorno C."
Fecha: 2025-05-28T22:58:00
Archivo: []
---
# Lenguaje “C”

## Origen y Evolución

Nace a principio de los anos 70, de la mano de Dennis Ritchie en los laboratorios Bell.

- Toma en base otro lenguaje llamado B, creado por Ken Thompson en 1969.
- Reescribe el Sistema Operativo Unix, en 1972.
- A mediados de los 80 se crea C++, que incorpora la orientación a objetos.
- En 1978, Dennis Ritchie y Brian Kernighan, publican la primer edición del libro “El Lenguaje de Programación C”.
- En 1989 se crea el primer estancar, conocido como ANSI C, y posteriormente surgen otro como ISO, etc.

Unix fue reescrito en C, ademas de que la mayor parte del Kernel de Windows esta hecho en el lenguaje C, ademas de otros lenguajes como Python.

## Características

- Es compilado, a diferencia de Python, (utiliza un compilador que convierte el programa fuente en un programa en lenguaje de maquina, que puede ser ejecutado por esta).
- Es imperativo (pertenece al grupo de los lenguajes cuyo tipo de programacion imperativa, lo cual significa que a nuestro programa le indicamos la secuencia de pasos que tieene que hacer para obtener los resultados que queremos).
    - En lo declarativos (como SQL), en cambio, le decimos directamente lo que queremos que haga.
- Es de Alto Nivel o Nivel Intemedio ( Es cercano al lenguaje humano, lejano al lenguaje de maquina) Se lo considera de niver intermedio, por la posibilidad de manejar recursos como la memeorio que otros lenguajes de alto nivel no tienen.
- Es fuertemente o debilmente tipado? ( una variable con un valor de un tipo determinado, no se puede usar como si fuera de otro tipo, a menos que se haga una conversion).
- ES estructurado (permite escribir programas siguiendo las reglas del paradigma de la programacion estruturada.

## Diferencias entre Compilador vs Interprete

![[compilador-vs-interprete.png]]

## Mi Primer Programa

Todo programa debe incluir la primer linea de `#include`` <stdio.h>` la cual significa “Standar Input Output” la cual es una libreria necesaria de incluir en todos nuestro programas de C, ya que nos pone a disposicion una serie de funciones basicas necesarias.

Todo programa en C debe tener la funcion `main()` y el `***void***` declara el tipo de dato que se le esta pasando a la funcion. El cual significa que no retorna nada

Las llaves indican que dentro de ellas se encuentra el bloque de programas.

`printf`  es para mostrar por pantalla

Es importante saber que las instrucciones siempre terminan con un punto y coma `instruccion;`

```c
# include <stdio.h>

void main()
{
	printf("Hola Mundo cruel \n");
	return;
}
```

Otro ejemplo:

En este caso vemos que la funcion `main()` se le pasa el valor de un `***int***`*** .***

Pero por lo general a la funcion `main()` se le pasa un `***void***`*** ***para que no devuelva nada.

# Introduccion a C

## Variables

Para declarar las variables, se debe indicar el tipo de la variable que vamos a declarar.

`[Tipo de Dato] [Nombre de la variables]`

o

`[Tipo de Dato] [Nombre de la variable] = [Valor]`

*Ejemplo:*

`int ``x`  o `int ``x = 100` 

En el primer caso, se reserva la variable “x” pero no va a tener ningun valor inicial, (en el caso de entero puede ser que se le asigne el valor 0)

Vamos a encontrarnos con que hay muchos mas tipos de datos que en Python.

### Como mostrar el valor de la variable

Si yo quiero mostrar el valor de una variable usando `printf` debo elegir donde lo quiero mostrar.

*Ejemplo:*

### Formateadores

| Tipo | **Descripción** |
| --- | --- |
| %d ó %i | entero en base 10 con signo (int) |
| %u | entero en base 10 sin signo (int) |
| %o | entero en base 8 sin signo (int) |
| %x | entero en base 16, letras en minúscula (int) |
| %X | entero en base 16, letras en mayúscula (int) |
| %f | Coma flotante decimal de precisión simple (float) |
| %lf | Coma flotante decimal de precisión doble (double) |
| %e | La notación científica (mantisa/exponente), minúsculas |
| %E | La notación científica (mantisa/exponente), mayúsculas |
| %c | caracter (char) |
| %s | cadena de caracteres (string) |
| %07i | largo mínimo de 7 dígitos, justificado a la derecha, rellena con ceros |
| %.7i | justificado a la derecha, 7 dígitos de largo, sin relleno |
| %8.2f | tamaño total de 8 dígitos, con dos decimales |
| %.*f | tamaño predeterminado, x números decimales |
| %*.*f | tamaño igual a x, y números decimales |
| %s | cadena terminada en null |
| %5s | primeros cinco caracteres o delimitador |
| %.5s | primeros cinco caracteres, sin tener en cuenta el delimitador |
| %20.5s | primeros cinco caracteres, justificados a la derecha, con 20 caracteres de largo |
| %-20.5s | primeros cinco caracteres, justificados a la izquierda, con 20 caracteres de largo |
| %ld | Sirve para los numeros long. |
| %hu | Formato para unsigned short. |
| %lf | Formato para double. |

## Constantes

Una constante es una variable inmutable, lo que quiere decir que, una vez declara la misma su valor va a permanecer estatico y no se podra modificar durante todo el programa.

Para declarar constantes lo que lo hacemos de la siguiente manera:

## Ingresos de Usuario (inputs)

Para poder pedirle al usuario que ingrese un dato y el programa lo lea podemos usar varias opciones, una de ellas es `scanf()` 

Tiene la siguiente estrutura: `scanf(tipo, &variable)` 

*Ejemplo:*

**IMPORTANTE! **Se debe tener en cuenta que para el ingreso de usuario, previamente debemos definir la variable y dejarla sin ningun valor, ya que cualquier valor que le pasemos va a ser sobreescrito al darse el ingreso de usuario.

<!-- Column 1 -->
### Aritmeticos

---

Suma: +

Resta: - 

Multiplicación: * 

División: /

Resto de la División: %

Incremento en n: variable += n

Incremento en 1: variable ++

Decremento en n: variable -= n

<!-- Column 2 -->
### Comparacion

---

Mayor >

Menor <

Igual ==

Distinto: !=

Mayor Igual: >=

Menor Igual: <=

***Para las comparaciones con caracteres se usa comilla simple ‘’***

<!-- Column 3 -->
### Logicos

---

Conjunción - Y: &&

Disjunción - O: ||

Not lógico: !


*Algunos ejemplos* de codigo haciendo operaciones con los distintos tipos de operadores:

En el caso de la division, si queremos que nos devuelva un resultado REAL o con coma, debemos pasarle el Formato de float %f y ademas convertir una de las variables a float.

## Delimitando Bloques y Respetando su Estilo

- Un bloque de código va encerrado entre llaves { }
- Las instrucciones terminan con punto y coma ;
- Para comentarios de varias líneas, iniciar con /* y finalizar con */
- Para comentarios de una línea o a continuación de código, anteponer //
- Indentar el código para mejor legibilidad, usando una tabulación de 4 espacios
- Usar minúsculas para las instrucciones
- Usar nombres descriptivos en minúsculas para variables y funciones; cuando estén compuestos por más de una palabra, unirlos con guion bajo (_). Por ejemplo: id_cliente
- Escribir las constantes en mayúsculas

## Estructuras Condicionales

Existen tres tipos de estructuras condicionales if, las cuales son simples, compuestas o anidadas.

### If Simple

El condicional *if simple *se compone de unicamente una sola estructura condicional, con sus respectivos parametros.

*Ejemplo:*

### If Compuesto

El condicional *if compuesto* se compone de ademas de la instruccion de if, una instruccion *else*

*Ejemplo:*

### If Anidado

El condicional *if anidado *nos permite evaluar multiples condiciones, mas alla de las dos que permite el if compuesto o la unica que evalua el if simple.

*Ejemplo: *

### Switch

Puede suceder que tengamos multiples opciones que analizar y resulte mas conveniente utilizar un switch, en lugar de anidar if.

*Ejemplo:*

```c
# include <stdio.h>

int main(){
	unsigned short mes;
	printf("Ingrese el nro. del mes: ");
	scanf("%i",&mes);
	printf("\nEl mes ingresado por Ud. es: ");
	
	switch (mes) {
		case 1 :
			printf("Enero");
			break;
		case 2 :
			printf("Febrero");
			break;
		case 3 :
			printf("Marzo");
			break;
		case 4 :
			printf("Abril");
			break;
		case 5 :
			printf("Mayo");
			break;
		case 6 :
			printf("Junio");
			break;
		case 7 :
			printf("Julio");
			break;
		case 8 :
			printf("Agosto");
			break;
		case 9 :
			printf("Setiembre");
			break;
		case 10 :
			printf("Octubre");
			break;
		case 11 :
			printf("Noviembre");
			break;
		case 12 :
			printf("Diciembre");
		default :
			printf("Inexistente");
		}
	return(0);
}
```

## Estructuras Iterativas

### For

La estructura iterativa *for* necesita ciertas intrucciones las cuales son:

Siempre se deben declarar estas tres condiciones, donde la primera es la declaracion del valor la variable, la segunda es la condicion que debe cumplir, y por ultimo la modificacion que se le hace a la variable en cada iteracion.

Ademas de declarar las variables antes de entrar en el ciclo for.

*Ejemplo:*

*Otro ejemplo:*

### While

El *while* nos permite repetir una serie de acciones cuando desconocemos cuando se producira el evento que nos permita salir del ciclo.

Las acciones dentro del ciclo, se llevaran a cabo, siempre que la condicion del ciclo while sea **verdadera**, de lo contrario, no se ingresa al ciclo, y se sigue con la siguiente instrucción.

```c
# include <stdio.h>
# define MINIMO 10
# define MAXIMO 250

int main(){
	int valor;
	printf("Ingrese valor: ");
	scanf("%i", &valor);
	while (valor < MINIMO || valor > MAXIMO)
		{
		printf("\nValor Invalido, Reingrese valor: ");
		scanf("%i", &valor);
		}

	printf("\nExito! Ud. ingreso un valor valido: %i",valor);
	
	return(0);
}
```

### do while

[[Do while pdf]]

El *do … while *nos permite forzar que se ejecute minimamente una vez el codigo que se desea analizar con el while, donde si se cumple la condicion del while, vuelva a iterar, y si no, salga del bucle.

*Ejemplo:*

## Booleanos en C

Permiten almacenar valore TRUE o FALSE.

Debemos importar el <stdbool.h>

### Operadores Logicos de Expresion Booleanas

![[operadores-logicos.png]]

### Uso de Booleanos con If

Se permite el uso de variables para eso se debe importar la libreria de ***stdbool.h***

*Ejemplo:*

*Ejemplo:*

Podemos usar `getchar()` la cual nos permite limpiar el buffer de datos.

# Usando C en Linux con VS Code
