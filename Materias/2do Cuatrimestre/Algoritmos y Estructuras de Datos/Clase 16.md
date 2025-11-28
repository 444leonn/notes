---
base: "[[Algoritmos y Estructuras de Datos.base]]"
Grabacion: https://youtu.be/wafzt0PKVlE?si=siwoaYJyzJ3NSp7_
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
## Floyd-Warshall

Lo podemos utilizar para encontrar el camino mínimo, pero a diferencia de Dijkstra que sirve para solo un vértice inicio, Floyd-Warshall sirve para cualquier par de vertices.

Podemos pensarlo como hacer un "Dijkstra con cada uno de los vertices"

Armamos una matriz de distancias:

![[../../../images/grafos-matriz-distancias.png]]

Una vez armada ya con la information de la matriz podemos hacer el algoritmo

1. Tomo un vértice _V0_ y otro par de vertices _V1_ y _V2_.
2. Y chequeo si es mas rápido ir de _V1_ a _V2_ o es mas rápido ir de V1 a V2 pasando por un vértice intermedio (V0).
3. Si es menor actualizo el valor, sino no.
4. Repito pero para todos los pares vertices.
5. Vuelvo al paso 1.

Los siguientes dos Algoritmos sirven para convertir Grafos Pesados en Arboles, y no solamente transformarlo en un Árbol, sino que la suma de los pesos totales que va a quedar en el Árbol, sea la minima posible.

Esto se conoce *Árbol de Expansion Mínimo* 
## Prim

La idea es empezar por un Árbol Vacio, es ir incorporando vertice a vertice, cada uno de los vertices del grafo.

Marcando el vertice agregado como ya visitado, evitando asi volver agregar una arista, y evitando que se formen ciclos.

![](../../../images/grafos-algoritmo-prim.gif)
## Kruskal

Similar al de Prim, con la diferencia de que en lugar de crear un árbol e ir agregando los vertices, va a crear N arboles con un vértice cada uno.

1. Crea los arboles
2. Ordeno las aristas de menor a mayor.
3. Verifico si puedo combinar los arboles con sus aristas. (solo si son arboles distintos)
4. Continuo hasta que me quede un único árbol.

## Orden Topologico

La idea del orden topológico es la de procesar los vértices de un grafo acíclico de forma tal que si el grafo contiene la arista dirigida uv entonces el nodo u aparece antes del nodo v.

- Busco el vértice que no tiene aristas incidentes/entrantes (grado de incidencia 0), y lo recorro.
- Esto me habilita las vertices adyacentes, elimino sus aristas, haciéndolo de grado de incidencia 0.

Siempre voy a recorrer el que tiene grado de incidencia 0, sino no lo puedo recorrer.

### Como hacerlo?

Podríamos usar DFS, lo cual me permitiría obtener un orden topologico.

Lo aplicamos a partir de cualquier vértice de nuestro grafo.

# Grafo Bipartito

Es un grafo que yo puedo dividir a la mitad, y puedo partir los vertices en dos grupos distintos de forma tal que nunca voy a tener aristas que relacionen dos vertices del mismo grupo.

Si lo pensamos con colores, tengo que poder colorear el grafo con dos colores sin que dos vertices del mismo color se toquen.

![](../../../images/grafos-bipartito.png)

Si tengo ciclos de longitud impar, es imposible que pueda lograr tener un grafo bipartito.

# Puntos de Articulación

Llamamos puntos de articulación a aquellos vertices que, si los elimino, me aumenta la cantidad de componentes conexas que tiene mi grafo.

Ejemplo: si tengo un grafo conexo de una única componente, y elimino un vértice y se separa en dos componentes conexas, ese vértice que elimine es un punto de articulación.

## Como los detecto?

Puedo usar DFS, ya que puedo detectar con eso si un grafo es conexo o no.
Entonces saco un vértice, hago DFS y me fijo si quedo conexo o no.

Otra forma seria aplicar 1 vez DFS, y luego fijarme los *BACKEDGE* que seria cunado volví sobre el vértice con la recursividad.

Un borde posterior **"Backedge"** es un borde en un grafo que conecta un vértice con un antepasado en un DFS. Indica la presencia de un ciclo y apunta a un nodo que ya ha sido visitado y todavía está en la pila de recursividad.

Entonces
1. Me guardo el recorrido
2. Me fijo cual seria el numero mas chico al que puedo llegar, con los *Backedge*

Ejemplo:

![](../../../../images/grafos-puntos-articulacion.png)
