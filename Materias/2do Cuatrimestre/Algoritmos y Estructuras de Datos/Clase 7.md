---
base: "[[Algoritmos y Estructuras de Datos.base]]"
Descripcion: "• TDAs:  Pila, Lista, Cola"
Fecha: 2025-09-09T18:03:00
Archivo:
  - 2693f454-0dd6-8028-b64b-e0d60fa2f696
  - 2693f454-0dd6-80ff-a76d-e3158e599189
  - 2693f454-0dd6-80ac-974d-dd252cad4827
---
# Pilas

*Ejemplo*: los historiales de búsqueda, a medida que vamos avanzando paginas se van apilando, y cuando queremos retroceder se desapila el ultimo que habíamos entrado.

## Que es una pila

- Estructura de datos

Estamos intentando representar una estructura de datos en la que almacenamos elementos.

- **LIFO:** Last In First Out, sigue esta regla ya que el ultimo en entrar va a ser el primero en salir.
El ultimo elemento que entro en la pila se llama **TOPE**, el resto de la pila no lo podemos ver.
Por lo general en operaciones de búsqueda no nos va a servir la pila justamente por eso.

### Operaciones

Para que un TDA de tipo PILA sea considerado como tal, debe cumplir como mínimo con estas operaciones.

- Crear (create):
- Apilar (push): apilo un valor en la pila, (importante reasignar el tope)
- Tope (top): devuelve el valor que hay en el tope de la pila. No puedo acceder a los elementos por debajo del tope, si lo pudiera hacer 
- Destruir (destroy):
- Desapilar (pop): puedo quitar el elemento que actualmente esta en el tope (importante reasignar el tope).
- Vacia (is Empty): 

## Implementaciones

Podemos pensar nuestra pila de tres formas:

### Vector Estático

Implemento un array estático de 5 posiciones, una variable *tope, *y una *capacidad* para saber la cantidad que puedo almacenar.

Para insertar una elemento verifico si el tope es menor a la capacidad

Para ver si esta vacía veo si el tope es 0 `tope == 0`

Para ver si puedo desapilar (pop) veo si el tope es distinto de 0 `tope != 0`

El problema es si quiero almacenar mas elementos.

**Complejidad**

- Crear: O(1)
- Destruir: Puede ser O(1) o O(n) depende de la implementacion, si solo es la estructura es O(1), si en la pila los elementos que hay son punteros o elementos que no manejamos, y queremos destruir todos los elementos sin perder memoria va a ser O(n)
- Insertar / Pushear: O(1)
- Desapilar / Pop: O(1)

### Vector Dinámico

Nos permite usar realloc, ademas de mantener las demás cosas.

El asunto es saber **cuanto agrandamos el vector?**

Una cosa importante es tener en cuenta es que si vamos agregando memoria de a 1, por cada elemento que queramos agregar, la complejidad de esa implementacion es muy grande, ya que teniendo en cuenta el peor caso de *realloc,* vamos a estar copiando todo el vector en todos los casos.

Por eso buscamos implementar un incremento en el realloc al doble en *2, lo cual

Este incremento o decremento de la pila lo podemos hacer tomando distintas políticas o redimensiones.

Por ejemplo:

- La pila crece cuando se supera el 75% crece.

Inclusive también puedo hacer un decremento en el tamaño de la pila cuando por ejemplo:

- Cuando se llega al 50% de la capacidad.
- Cuando desapilo
- Cuando se llega al 25% de la capacidad.

**Complejidad**

- Crear: O(1)
- Destruir: O(1) / O(n), depende de la implementacion, si es solo la 
- Insertar / Pushear: O(n) (por el caso de realloc)
- Desapilar / Popear: O(n) 

Todo muy lindo pero si no puedo realocar, porque no existe memoria contigua y el realloc falla, debo hacer otro implementacion.

## TDA Nodo Enlazado

### Que idea abstrae

Básicamente es un struct, donde esta mi dato y un puntero asociado donde esta el siguiente dato.

Version 2.0, hay un puntero asociado al dato anterior* “TDA Nodo doblemente enlazado”*

### Solución: lista de Nodos

- Los elementos son nodos.
- Cada uno tiene una referencia al nodo anterior.

Cuando reservo / libero memoria?

- Reservo memoria para cada nodo, cuando quiero apilar.
- Libero memoria para cada nodo, cuando quiero desapilar.

Ventaja: ahora la memoria ya **no tiene que ser contigua necesariamente.**

Cuando apilamos movemos el puntero del tope al nuevo nodo

Cuando desapilamos tenemos que tener cuidado, debemos guardarnos la referencia al nodo que vamos a desapilar, reasignamos el tope, y luego liberamos la variable auxiliar. Para no perder la referencia ni de la pila ni del nodo que desapilamos.

### Complejidad:

- Crear: O(1)
- Destruir: O(n)
- Insertar / Pushear: O(1)
- Pop: O(1)

# Colas

La fila de un supermercado es una cola justamente, porque el primero que llega es el primero que se va.

Estructura “*F.I.F.O*” *First in, First Out*, esto hace referencia a que el primer ingreso que llega a la cola va a ser el primero que sale.

- Se encola por el final.
- Se desencola por el frente.

## Primitivas

- Crear
- Destruir
- Encolar / Agregar elemento
- Desencolar / Quitar elemento
- Primero: ver el primer elemento de la cola
- Vacio: ver si esta vacía

## Implementacion

### Vector Estático

Encolar: agrego un nuevo elemento en la ultima posición.

Si llego al tope no voy a poder.

Desencolar: elimino el de la primer posicion, digamos, voy desencolando desde el principio hacia el final. 

El problema es que al desencolar me quedan las primeras posiciones del vector vacias y las estaria desperdiciando despues.

Soluciones:

- Desplazar todos los elementos hacia el inicio de la cola
- Implementar una cola circular. Uno el principio de la cola con el tope

**Complejidades:**

- Encolar: O(1)
- Desencolar:
    - Desplazando elementos: O(n)
    - Usando cola circular: O(1), ya que no hace falta desplazar ningún elemento, (jugamos con los indices)
- 

### Vector Dinámico

Tiene la ventaja de que puedo ampliarlo cuando me quedo sin espacio.

Sigo teniendo el mismo problema al desencolar

### Nodos Enlazados

Nos permite hacer una implementacion de desplazamiento circular mas sencillo.

Entonces en nuestra estructura almacenamos un nodo al principio de la cola y uno al final.

Complejidades:

- Encolar: O(1)
- Desencolar: O(1)

# Listas

Es uno de los TDAs mas usados, ademas de los objetos, y suele ser usada para todos.

## Que es un Lista?

Nos permite agrupar elementos.

Cada elemento de la lista tiene un:

- Predecesor: (salvo el primer elemento) 
- Sucesor: (salvo el ultimo elemento)

## Operaciones

## Implementaciones

### Nodos Enalazados

Pueden ser:

- Simplemente enlazadas (la que vamos a usar)
- Doblemente enlazadas
- Circulares

**Simplemente Enlazada**

- Implementacion con nodos
- Cada uno con referencia al **nodo siguiente**
- Lista mantiene referencia al primer nodo.

Cuando reservo / libero memoria?

Cuando la creo el nodo al primer elemento apunta a NULO

Cuando inserto el primer elemento elemento el puntero al nodo pasa a ser al elemento, y también tengo una referencia dentro de mi nodo al siguiente elemento.

Si quiero insertar un elemento al final debo recorrer hasta llegar al nodo cuya referencia sea NULO y cambiar su referencia al nuevo nodo que quiero insertar.

Si quiero insertar un nuevo nodo entre medio, osea en cualquier lado distinto del final. Tengo que, asignar al nodo que quiero insertar la referencia al nodo que va a ser su siguiente y luego al nodo anterior le asigno la referencia al nuevo nodo. (O usar un nodo auxiliar)

Si quiero eliminar un nodo de entre medio, ahí obligatoriamente debo utilizar un nodo auxiliar para no perder la referencia.
