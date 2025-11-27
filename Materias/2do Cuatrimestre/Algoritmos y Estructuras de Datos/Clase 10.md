---
base: "[[Algoritmos y Estructuras de Datos.base]]"
Descripcion: • Arboles • ABB
Fecha: 2025-09-23T18:12:00
Archivo:
  - 2773f454-0dd6-8088-b8be-ed3f9f846206
---
# Arbol

Es una coleccion de nodos, que a su vez, pueden estar conectados a otros multiples nodos.

## Por que?

Nacen de la necesidad de representar una jerarquia en la estructura de los dato, asi como tambien de querer optimizar la busqueda lineal de una lista.

Con el arbol se intenta hacer algo similar a la busqueda binaria, tratando de darnos acceso a los datos en un mejor

## Como

A partir de un nodo “raiz” a los cuales se le conectan subnodos, y demas.

## Tipos de Arboles

## Estructura

### Recursividad

- Condicion de Corte
- Llamada a la funcion

## Definiciones

## Arbol N-arios

Un *arbol *es una **coleccion de nodos**

- Nodos son todos los elementos del arbol.

> [!tip] 💡
> Observacion: cada nodo tiene 0 o mas elementos conectados a el.

- Raiz: Es el elemento en el 1er nivel del arbol (mas alto).

Los elementos se numeran de N1, hacia abajo, con N2, N3, ….. Nn

- Subarbol: Parandome en un nodo, puedo ver distintos arboles debajo de el.
- Nodos Padres: Desde un nodo, el superior a el es su padre. Todos los nodos tienen un padre unico (salvo la raiz N1)
- Nodos Hijos: Los nodos conectados en un nivel inferior son *hijos *del nodo en el que estoy parado.

 

> [!warning] ⚠️
> Alcanza con mirar padre e hijos, un nivel para arriba y otro para abajo, no mas alla.
Nada de nodos abuelos, tios, etc… TAMPOCO HERMANOS

- Hojas: Nodos que no tiene hijos.

## Arbol Binario

Se restringe la cantidad de hijos que puede tener cada nodo, a como maximo dos.

Podemos tener una nocion de *“Hijo Izquierdo”* e *“Hijo Derecho”*

### **Operaciones:**

- Crear

### **Recorridos: **Es la operacion mas importante (lo van a mirar en el tp)

Significa de alguna forma pasar por cada uno de los nodos.

Hay distintas maneras de realizarlo

- *Preorder*: NID, visitar el Nodo Actual, luego la Izquierda y por ultimo la Derecha
- *Inorder*: Primero visita el subarbol izquierdo, luego el nodo actual y por ultimo el subarbol derecho
- *Postorder*: Primer visita el subarbol izquierdo, luego el subarbol derecho y por ultimo el nodo actual.

![](../../../images/recorridos-abb.png)

## Arbol Binario de Busqueda

Tenemos un orden por ende tenemos una forma de comparar los elementos para poder definir este orden y cada nodo del arbol posee un valor o una clave unica.

### **Caracterisiticas:**

- Las claves mayores se insertan en los subarboles derechos.
- Las claves menores se insertan en los subarboles izquierdos
- Ambos subarboles tambien son arboles de busqueda binaria.

### **Busqueda**

La busqueda de un elemento comienza siempre en el nodo raiz y sigue estos pasos:

1. La clave buscada se compara con la clave del nodo raiz.
2. Si las claves son iguales la busqueda se detiene.
3. Si la clave buscada es mayor que la raiz, la busqueda se reanuda en el sub-arbol derecho. Si la clave buscada es menor que la clave raiz, la busqueda se reanuda en el sub-arbol izquierdo.

Esto nos permite reducir mucho los tiempos y la complejidad de la busqueda de valores, ya que nos permite suprimir o descartar gran cantidad de opciones.

### **Insertar**

4. Comparo la clave del elemento a insertar con la clave del nodo raiz. Si es mayor avanzo hacia la subarbol derecho, si es menor avanzare hacia el subarbol izquierdo.
5. Repito el paso 1 hasta encontrar un elemento con clave igual o llegar al final del sub-arbol donde debo insertar el nuevo elemento.
6. Cuando se llega al final creo un nuevo nodo, asignado null a los punteros izquierdo y derecho y coloco el nuevo nodo como hijo izquierdo o derecho.
**Complejidad: **$log(n)$

### **Borrar Nodo**

Dividimos el problema en 3 casos.

### Recorridos Aplicados a ABBs

- Preorden: Sirve para hacer una copia del árbol.
    - [20, 15, 10, 5, 13, 17, 19, 25, 30, 27, 35]
- Inorden: Nos da un recorrido ORDENADO del árbol.
    - [5, 10, 13, 15, 17, 19, 20, 25, 27, 30, 35]
- Postorden: Nos da el orden de borrado del árbol.
    - [5, 13, 10, 19, 17, 15, 27, 35, 30, 25, 20]

### Importante Balancear un Arbol

- A pesar de todo lo visto, el orden en el que se insertan los elementos en un ABB es de gran importancia.
- Dos ABB con los mismos elementos pero insertados en distinto orden no necesariamente son iguales.
- Debido a esto, los árboles pueden degenerar en listas.
- Las complejidades algorítmicas de buscar, insertar y borrar en un ABB, en el peor de los casos, es O(N).

> [!warning] ❗
> ACLARAR SIEMPRE EL CASO DEL ARBOL BALANCEADO Y EL NO BALANCEADO

### Aplicaciones

- Son utilizados para conformar índices, tanto de uno como de múltiples niveles.
- Se utilizan para mejorar numerosos algoritmos de búsqueda.
- Son útiles para mantener ordenados streams de información entrante.
- Estructuras de datos como TreeMap y TreeSet se implementan internamente con ABBs balanceados.
- Se usa en la implementación de colas de prioridad doble, por prioridad máxima o prioridad mínima.