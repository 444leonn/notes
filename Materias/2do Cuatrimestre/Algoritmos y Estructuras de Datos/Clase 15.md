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

![](../../../images/grafos-1.png)

## Características

Según la forma o la dirección que tenga podemos decir distintas cosas

- **Dirección:** Decimos que un Grafo G es Dirigido (o Digrafo) si sus aristas tienen sentido.
	Si no tiene dirección o sentido es No Dirigido y puedo ir en ambos sentidos
	
	Ejemplo: El ABB es un Digrafo o grafo dirigido ya que siempre el nodo apunta a los hijos.
	Una lista doblemente enlazada seria un grafo no dirigido ya que puedo ir en ambas direcciones.

![](../../../../grafos-dirigido.png)

- **Peso:** Significa que las aristas en el grafo tienen un peso asignado.
El peso de la arista pue    de representarse
- **Orden:** Es la cantidad de vértices o IVI (nodos)
- **Tamaño:** Es la cantidad de aristas o IEI (conexiones o arcos)
- **Arista Bucle:** Una arista es un bucle cuando conecta al vértice consigo mismo.
- **Grafo Simple:**
- **Grafo NO Simple:**

![](../../../../grafos-simples.png)

### Tipos

- Grafo Vacío: es un grafo sin aristas. (no tiene conexiones)
- Grafo Nulo: es un grafo sin vértices ni aristas.

### Completitud

Un grafo es completo cuando contiene todas las aristas posibles.

En donde cualquier par de vértices o nodos que yo elija va estar conectado entre si.

![](../../../../grafos-completos.png)

Sin embargo hay algo que no tuvimos en cuenta. Cuanto menor sea la cantidad de aristas en mi grafo vemos el grado de dispersión del grafo, y a medida que se van agregando aristas el grafo se vuelve mas denso.

### Caminos

Es una secuencia de vertices (unidos por aristas). En un camino no pueden haber vertices repetidos.

![](../../../../grafos-caminos.png)

- **Ciclos: **Es cuando un camino empieza y termina en el mismo vértice.
    - **Grafos ACICLICOS ⇒ **NO posee ciclos.
![[grafos-ciclos.png]]
- **Grafo Conexo: **un grafo (no dirigido) es conexo, si para cualquier par de vértices existe al menos un camino entre ellos.
![[grafos-conexo.png]]
    - **Fuertemente Conexo: **existe camino de A hacia B y de B hacia A.
    - **Débilmente Conexo: **Si para lograr estos caminos debemos reemplazar una o mas aristas por aristas sin sentido.
Si todos los pares son *Fuertemente Conexo, *entonces el Digrafo es fuertemente conexo.

![]](*../images/ff853a01-5b53-412d-9e4b-eaf1b40887ac.png)

### Árbol
Un grafo es un árbol si es *conexo y acíclico.*

![[grafos-arbol.png]]

## Formas de Representar Grafos

Siempre va a depender del problema que queramos responder

### Matriz de Adyacencias

**Complejidad:** $n^2$

1. Me paro en un vértice
2. Me fijo desde ese cuantas aristas de longitud 1 conectan con otro vértice.
3. Repito hasta completas la matriz.

En un grafo dirigido la matriz de adyacencia solo registra el vértice, si y solo si la arista parte del vértice i y llega hasta le vértice j.

Si el grafo tiene pesos, la matriz se completa con los pesos.

### Lista de Adyacencias

Cada arista posee una lista simplemente enlazada de a que vertices esta unida.

### Matriz de Incidencias


Al ver que la representación como matriz tiene gran complejidad y es difícil de utilizar con memoria dinámica, tenemos esta otra forma de representación para los grafos.

# Recorridos de los Grafos

[https://youtu.be/T1dZho6fD0A?t=1983](https://youtu.be/T1dZho6fD0A?t=1983)

Debemos volver a utilizar la pila y la cola.

## En Profundidad (DFS “Depth First Search”)

Es un recorrido en profundidad del grafo.

Consiste en ir recorriendo el grafo empezando desde un vértice cualquiera, y a cada paso se visita un vértice adyacente al ultimo visitado.
Utiliza una *pila*.

Ejemplo usando la pila:
1. Apilar un vértice.
2. Quitar un vértice de la pila. (visitarlo)
3. Apilar los vertices adyacentes al actual.
4. Repetir desde (2) hasta quedarse sin vertices.

## A lo Ancho (BFS “Breadth First Search”)

Es un recorrido en anchura del grafo.
Utiliza una *cola*.

Consiste en ir recorriendo el grafo empezando desde un vértice cualquiera, y luego se van visitando los vertices adyacentes mas cercanos .

Ejemplo usando la cola:
1. Encolar un vertices.
2. Quitar un vértice de la cola (visitarlo).
3. Encolar los vertices adyacentes al actual.
4. Repetir desde (2) hasta quedarse sin vertices.
