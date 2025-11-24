---
base: "[[Algoritmos y Estructuras de Datos.base]]"
Grabacion: https://youtu.be/KSM3gR-DP1w?si=sPXBRJXg7lyMz-HK
Descripcion: • Grafos
Fecha: 2025-11-04T18:31:00
Archivo:
  - 2a23f454-0dd6-8059-9176-c46ba0056b62
  - 2a23f454-0dd6-8015-ba30-f2b38ec3b426
---
# Introducción a Grafos

## Definición

Un Grafo G es un par ordenado G=(V,E) donde:

- V es un conjunto de vértices (o nodos)
- E es un conjunto de Aristas (o Arcos)

![[image 7.png]]

## Características

Según la forma o la dirección que tenga podemos decir distintas cosas

- **Dirección: **Decimos que un Grafo G es Dirigido (o Digrafo) si sus aristas tienen sentido.
Sin no tiene dirección o sentido es No Dirigido y puedo ir en ambos sentidos
Ejemplo: El ABB es un Digrafo o grafo dirigido ya que siempre el nodo apunta a los hijos.
Una lista doblemente enlazada seria un grafo no dirigido ya que puedo ir en ambas direcciones.

![[image 8.png]]

- **Peso: **Significa que las aristas en el grafo tienen un peso asignado.
El peso de la arista puede representarse
- **Orden: **Es la cantidad de vértices o IVI (nodos)
- **Tamaño: **Es la cantidad de aristas o IEI (conexiones o arcos)
- **Arista Bucle: **Una arista es un bucle cuando conecta al vértice consigo mismo.
- **Grafo Simple:**
- **Grafo NO Simple:**
![[c80d2c72-e0b1-450b-88b5-403a39edc6ef.png]]

### Tipos

- Grafo Vacío: es un grafo sin aristas. (no tiene conexiones)
- Grafo Nulo: es un grafo sin vértices ni aristas.

### Completitud

Un grafo es completo cuando contiene todas las aristas posibles.

En donde cualquier par de vértices o nodos que yo elija va estar conectado entre si.

![[image 9.png]]

Sin embargo hay algo que no tuvimos en cuenta. Cuanto menor sea la cantidad de aristas en mi grafo vemos el grado de dispersión del grafo, y a medida que se van agregando aristas el grafo se vuelve mas denso.

### Caminos

Es una secuencia de vertices (unidos por aristas). En un camino no pueden haber vertices repetidos.

![[757740f2-3808-445a-bd9b-2541a7181e90.png]]

- **Ciclos: **Es cuando un camino empieza y termina en el mismo vértice.
    - **Grafos ACICLICOS ⇒ **NO posee ciclos.
![[f191ae40-e255-488f-b746-3c3d77c02c35.png]]
- **Grafo Conexo: **un grafo (no dirigido) es conexo, si para cualquier par de vértices existe al menos un camino entre ellos.
![[883cdf20-5e1c-41f9-a663-77c3bd96df6e.png]]
    - **Fuertemente Conexo: **existe camino de A hacia B y de B hacia A.
    - **Débilmente Conexo: **Si para lograr estos caminos debemos reemplazar una o mas aristas por aristas sin sentido.
Si todos los pares son *Fuertemente Conexo, *entonces el Digrafo es fuertemente conexo.
![[ff853a01-5b53-412d-9e4b-eaf1b40887ac.png]]
    ### Árbol
Un grafo es un árbol si es *conexo y acíclico.*

![[29c6fa94-f93e-4493-b630-46208327670e.png]]

## Formas de Representar Grafos

Siempre va a depender del problema que queramos responder

### Matriz de Adyacencias

**Complejidad:** $n^2$

### Matriz de Incidencias

### Lista de Adyacencias

Al ver que la representación como matriz tiene gran complejidad y es difícil de utilizar con memoria dinámica, tenemos esta otra forma de representación para los grafos.

# Recorridos de los Grafos

[https://youtu.be/T1dZho6fD0A?t=1983](https://youtu.be/T1dZho6fD0A?t=1983)

Debemos volver a utilizar la pila y la cola.

## En Profundidad (DFS “Depth First Search”)

Es un recorrido en profundidad del grafo.

Utiliza una *pila*.

## A lo Ancho (BFS “Breadth First Search”)

Es un recorrido en anchura del grafo.

Utiliza una *cola*.

# Algorimo de Dijkstra

El algoritmo de Dijkstra es un algoritmo para la determinación del camino más corto, dado un vértice origen, hacia el resto de los vértices en un grafo que tiene pesos en cada arista.

La idea subyacente en este algoritmo consiste en ir explorando todos los caminos más cortos que parten del vértice origen y que llevan a todos los demás vértices.

Cuando se obtiene el camino más corto desde el vértice origen hasta el resto de los vértices que componen el grafo, el algoritmo se detiene.

No funciona en grafos con aristas de peso negativo.

## Busqueda de Caminos minimos

Significa que si tengo un grafo que representa caminos con distancia, y supongamos que quiero encontrar el camino mas corto entre dos vertices.

- Importante: se concentra en buscar caminos a partir de un vertice de salida o inicial.
