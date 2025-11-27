---
base: "[[Algoritmos y Estructuras de Datos.base]]"
Grabacion: https://youtu.be/7jajBwFtLHU?t=1410
Descripcion: |-
  • Mas Grafos
  • Floyd • Prim • Kruskal 
Fecha: 2025-11-11T18:01:00
Archivo:
  - 2a23f454-0dd6-80c8-80b3-ed31ed0695a6
---
# Algoritmos de Grafos

## Algoritmo de Dijkstra

El algoritmo de Dijkstra es un algoritmo para la determinación del camino más corto, dado un vértice origen, hacia el resto de los vértices en un grafo que tiene pesos en cada arista.

La idea subyacente en este algoritmo consiste en ir explorando todos los caminos más cortos que parten del vértice origen y que llevan a todos los demás vértices.

Cuando se obtiene el camino más corto desde el vértice origen hasta el resto de los vértices que componen el grafo, el algoritmo se detiene.

No funciona en grafos con aristas de peso negativo.

1. Se elige el vértice V sobre el cual se quiera aplicar el algoritmo
2. Se crean dos listas de nodos, una lista de nodos Visitados y otra listas de nodos NO Visitados, que contiene todos los nodos del grafo.
3. Se crea una tabla con 3 columnas, Vértice, Distancia mínima V y el
nodo anterior por el cual se llegó.
4. Se toma el vértice V como vértice inicial y se calcula su distancia a sí
mismo, que es 0.
5. Se actualiza la tabla, en la cual todas las distancias de los demás
vértices a V se marcan como inﬁnito.

### Búsqueda de Caminos mínimos

Significa que si tengo un grafo que representa caminos con distancia, y supongamos que quiero encontrar el camino mas corto entre dos vertices.

- Importante: se concentra en buscar caminos a partir de un vértice de salida o inicial.

## Orden Topologico

La idea del orden topológico es la de procesar los vértices de un grafo acíclico de forma tal que si el grafo contiene la arista dirigida uv entonces el nodo u aparece antes del nodo v.

## Prim

## Kruskal

Similar al de Prim, con la diferencia de que en lugar de ir agregando las aristas al arbol que ya estas construyendo, vamos a agregar las aristas de menor peso.
