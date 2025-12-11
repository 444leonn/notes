# Final 2 - 1C 2025

1. Escriba una función (en C99 o Python) como parte de la implementación de un árbol AVL que reciba un nodo y un tipo de rotación y la realice.
Agregue parámetros si cree que son necesarios.
Justifique la implementación, su complejidad y explique cómo funciona.

```c
enum AVL_ROTACIONES {IZQ, DER};

nodo_t *realizar_rotacion(nodo_t *nodo, enum AVL_ROTACIONES rotacion)
{
	if (nodo == NULL)
		return NULL;

	if (rotacion == IZQ) {
		nodo_t *aux = nodo;
		nodo = nodo->der;
		if (nodo->izq != NULL)
			aux->der = nodo->izq;
		nodo->izq = aux;

		return nodo;
	} else {
		nodo_t *aux = nodo;
		nodo = nodo->izq;
		if (nodo->der != NULL)
			aux->izq = nodo->der;
		nodo->der = aux;

		return nodo;
	}

	return NULL;
}
```

2. Explique el algoritmo de heap-sort. Utilizando heap-sort ordene el siguiente vector de menor a mayor.
Justifique la complejidad y muestre cada paso del algoritmo. V = [6, 8, 2, 4, 5, 1, 0, 9].

Heap-Sort es un algoritmo de ordenamiento basado en la estructura del Arbol Binario Heap, el cual se caracteriza por no establecer un orden entre los nodos adyacentes, sino que establece un orden de nodos por niveles.  
Donde cada nivel del arbol es de un peso mayor al superior, donde la raiz del arbol es el nodo menos pesado, y los nodos hojas los mas pesados. Decimos que los nodos menos pesados tienden a subir/flotar en el arbol.  
Heap-Sort funciona convirtiendo un vector a uno que referencia a un Heap, mediante un algoritmo que denominamos de "Heapify" y luego aplicamos una seria de operaciones sobre el vector, en donde vamos reduciendo la capacidad total del Heap y reevaluando si los valores restantes dentro de el estan bien posicionados "mediante sift-down".

- Heapify:
Para poder ordenar de menor a mayor voy a realizar un Heap Maximal, donde el nodo raiz sera el de mayor valor.

V = [6, 8, 2, 4, 5, 1, 0, 9]

hijo izquierdo = 2 x nodo + 1
hijo derecho = 2 x nodo + 2

Comienzo desde el ultimo nodo con hijos, lo cual esta dado por la mitad del vector - 1, y aplico sift-down sobre los valores.

En este caso es el valor en el indice 3.

indice 3:
V = [6, 8, 2, 9, 5, 1, 0, 4]

indice 2:
V = [6, 8, 2, 9, 5, 1, 0, 4]

indice 1:

V = [6, 9, 2, 8, 5, 1, 0, 4]

indice 0:
V = [9, 6, 2, 8, 5, 1, 0, 4]
repito
V = [9, 8, 2, 6, 5, 1, 0, 4]

- Intercambiamos cabecera con final del heap y luego reducimos su tamaño y aplicamos sift-down sobre la nueva cabecera:

1. V = [4, 8, 2, 6, 5, 1, 0, | 9]

	V = [8, 4, 2, 6, 5, 1, 0, | 9]
	V = [8, 6, 2, 4, 5, 1, 0, | 9]

2. V = [0, 6, 2, 4, 5, 1, | 8, 9]

	V = [6, 0, 2, 4, 5, 1, | 8, 9]
	V = [6, 5, 2, 4, 0, 1, | 8, 9]

3. V = [1, 5, 2, 4, 0, | 6, 8, 9]

	V = [5, 1, 2, 4, 0, | 6, 8, 9]
	V = [5, 4, 2, 1, 0, | 6, 8, 9]

4. V = [0, 4, 2, 1, | 5, 6, 8, 9]

	V = [4, 0, 2, 1, | 5, 6, 8, 9]
	V = [4, 1, 2, 0, | 5, 6, 8, 9]

5. V = [0, 1, 2, | 4, 5, 6, 8, 9]

	V = [2, 1, 0, | 4, 5, 6, 8, 9]

6. V = [0, 1, | 2, 4, 5, 6, 8, 9]

	V = [1, 0, | 2, 4, 5, 6, 8, 9]

7. V = [0, | 1, 2, 4, 5, 6, 8, 9]

8. V = [| 0, 1, 2, 4, 5, 6, 8, 9]

Asi obtenemos el vector ordenado.


3. Explique qué es el algoritmo de Dijkstra y para qué sirve.
Aplíquelo al siguiente grafo mostrando el resultado de cada paso y el resultado final comenzando desde H.  
![](../images/1C-2025-final-2.png)

El Algoritmos de Dijkstra nos permite obtener, en grafos pesados y partir de un vertice inicial, todos los caminos minimos al resto de vertices de ese grafo.  
El algoritmo funciona estableciendo los **nodos visitados** y los **nodos NO visitados**, y una tabla con los 3 columnas, vertices, distancia minima, y vertice anterior por el cual se llego a ese vertice.

- Se comienza colocando el vertice de inicio, se lo pasa a la lista de visitados, y completando las distancias conocidas, que son inicialmente los pesos aristas y vertices adyacentes al vertice de origen. (resto de vertice marcados como distancia = infinito)
- Se visita el menor vertice conocido, y se calcula las distancias a sus adyacentes como la suma de su distancia mas las de sus aristas.
- Si la distancia es menor a la conocida se actualiza la tabla.
- Se marca el vertice como visitado y se repite el proceso con el siguiente menor conocido.

| Vertice | Distancia Minima | Vertice Anterior |
|:-------:|:----------------:|:----------------:|
|   H .   |        -         |        0         |
|    A    |       inf        |        -         |
|    B    |       inf        |        -         |
|    C    |       inf        |        -         |
|    D    |       inf        |        -         |
|    E    |        2         |        H         |
|    F    |        1         |        H         |
|    G    |       inf        |        -         |
|    I    |       inf        |        -         |

Visitados = [H]  
No Visitados = [A, B, C, D, E, F, G, I]

| Vertice | Distancia Minima | Vertice Anterior |
|:-------:|:----------------:|:----------------:|
|    H    |        -         |        0         |
|    A    |       inf        |        -         |
|    B    |        4         |        F         |
|    C    |       inf        |        -         |
|    D    |       inf        |        -         |
|    E    |        2         |        H         |
|   F .   |        1         |        H         |
|    G    |        4         |        F         |
|    I    |       inf        |        -         |

Visitados = [H, F]  
No Visitados = [A, B, C, D, E, G, I]

| Vertice | Distancia Minima | Vertice Anterior |
|:-------:|:----------------:|:----------------:|
|    H    |        -         |        0         |
|    A    |       inf        |        -         |
|    B    |        4         |        F         |
|    C    |       inf        |        -         |
|    D    |       inf        |        -         |
|   E .   |        2         |        H         |
|    F    |        1         |        H         |
|    G    |        4         |        F         |
|    I    |       inf        |        -         |

Visitados = [E, F, H]  
No Visitados = [A, B, C, D, G, I]

| Vertice | Distancia Minima | Vertice Anterior |
|:-------:|:----------------:|:----------------:|
|    H    |        -         |        0         |
|    A    |       inf        |        -         |
|    B    |        4         |        F         |
|    C    |       inf        |        -         |
|    D    |       inf        |        -         |
|    E    |        2         |        H         |
|    F    |        1         |        H         |
|   G .   |        4         |        F         |
|    I    |        6         |        G         |

Visitados = [E, F, G, H]  
No Visitados = [A, B, C, D, I]

| Vertice | Distancia Minima | Vertice Anterior |
|:-------:|:----------------:|:----------------:|
|    H    |        -         |        0         |
|    A    |       inf        |        -         |
|   B .   |        4         |        F         |
|    C    |        6         |        B         |
|    D    |        7         |        B         |
|    E    |        2         |        H         |
|    F    |        1         |        H         |
|    G    |        4         |        F         |
|    I    |        6         |        G         |

Visitados = [B, E, F, G, H]  
No Visitados = [A, C, D, I]

| Vertice | Distancia Minima | Vertice Anterior |
|:-------:|:----------------:|:----------------:|
|    H    |        -         |        0         |
|    A    |       inf        |        -         |
|    B    |        4         |        F         |
|    C    |        6         |        B         |
|    D    |        7         |        B         |
|    E    |        2         |        H         |
|    F    |        1         |        H         |
|    G    |        4         |        F         |
|   I .   |        6         |        G         |

Visitados = [B, E, F, G, H, I]  
No Visitados = [A, C, D]

| Vertice | Distancia Minima | Vertice Anterior |
|:-------:|:----------------:|:----------------:|
|    H    |        -         |        0         |
|    A    |        9         |        C         |
|    B    |        4         |        F         |
|   C .   |        6         |        B         |
|    D    |        7         |        B         |
|    E    |        2         |        H         |
|    F    |        1         |        H         |
|    G    |        4         |        F         |
|    I    |        6         |        G         |

Visitados = [B, C, E, F, G, H, I]  
No Visitados = [A, D]

| Vertice | Distancia Minima | Vertice Anterior |
|:-------:|:----------------:|:----------------:|
|    H    |        -         |        0         |
|    A    |        9         |        C         |
|    B    |        4         |        F         |
|    C    |        6         |        B         |
|   D .   |        7         |        B         |
|    E    |        2         |        H         |
|    F    |        1         |        H         |
|    G    |        4         |        F         |
|    I    |        6         |        G         |

Visitados = [B, C, D, E, F, G, H, I]  
No Visitados = [A]

| Vertice | Distancia Minima | Vertice Anterior |
|:-------:|:----------------:|:----------------:|
|    H    |        -         |        0         |
|   A .   |        9         |        C         |
|    B    |        4         |        F         |
|    C    |        6         |        B         |
|    D    |        7         |        B         |
|    E    |        2         |        H         |
|    F    |        1         |        H         |
|    G    |        4         |        F         |
|    I    |        6         |        G         |

Visitados = [A, B, C, D, E, F, G, H, I]  
No Visitados = []

- **Tabla Final**

| Vertice | Distancia Minima | Vertice Anterior |
|:-------:|:----------------:|:----------------:|
|    H    |        -         |        0         |
|    A    |        9         |        C         |
|    B    |        4         |        F         |
|    C    |        6         |        B         |
|    D    |        7         |        B         |
|    E    |        2         |        H         |
|    F    |        1         |        H         |
|    G    |        4         |        F         |
|    I    |        6         |        G         |


4. Explique qué es un grafo bipartito.  
Determine si el grafo del punto 3 es bipartito.  
Escriba (en C99 o Python) un algoritmo para detectar si un grafo es bipartito.  
Explique cómo funciona y las estructuras de datos necesarias para su funcionamiento.

Un grafo bipartito es aquel grafo del que puede distinguirse dos conjuntos donde las aristas que relacionan los vertices nunca relacionan dos vertices del mismo conjunto, sino que, siempre las aristas van a relacionar vertices del otro conjunto.  
Para determinar si un grafo es bipartito podemos establecer un algoritmo que marque cada uno de los vertices y luego revise los adyacentes, y debe cumplirse que ninguno de sus adyacentes tenga el mismo tipo de marca. Si eso se cumple para todos los vertices del grafo podemos asegurar que sera bipartito.  

Un posible algortimo es uno similar al DFS que es un algoritmo de recorrido en profundidad, pero agregando una revision de los adyacentes luego de visitar el vertice.

```python
def determinar_bipartito(grafo):
	inicio = list(grafo.keys())[0]
	visitados = {}

	def determinar_bipartito_recursivo(grafo, vertice, visitados, color):
		if vertice not in visitados:
			visitados[vertice] = color
		
		for adyacente in grafo[vertice]:
			if adyacente not in visitados:
				if determinar_bipartito_recursivo(grafo, adyacente, visitados, 1 - color) == False:
					return False
			elif visitados[adyacente] == color:
				return False

		return True

	return determinar_bipartito_recursivo(grafo, inicio, visitados, 0)
```

5. Explique qué es un diccionario y para qué se utiliza.  
Haga una tabla comparativa con 3 implementaciones diferentes (tabla de hash es una sola) de diccionarios.  
Las tabla debe poseer las siguientes columnas (como mínimo):
- Tiempo de inserción y búsqueda
- Resolución de colisiones.
- Memoria (aproximado en bytes) utilizada en función a la cantidad de claves.  
Para cada casillero explique cómo llega a la respuesta.

Un Diccionario es un Tipo de Dato Abstracto que nos permite establecer un relacion entre pares de `claves` y `valores`, donde cada clave puede identificar de manera sencilla a cada valor asociado a la misma.

|                           | Tiempo Insercion y Busqueda | Colisiones | Memoria |
|:-------------------------:|:---------------------------:|:----------:|:-------:|
|      Vector Dinamico      | Insercion: *O(1)* quizas *O(n)* Busqueda: *O(n)* | No hay | n * (tamaño clave + tamaño valor) contiguo en memoria |
| Arbol Binario de Busqueda | Si esta balanceado: *O(log(n))* | No hay | n * (tamaño clave + tamaño valor + 2 punteros a nodo) |
|       Tabla de Hash       | *O(1)* | Si es un Hash Abierto, se utilizan metodos para reubicar el par dentro de la tabla. Si es un Hash Cerrado, se agrega a la estructura de soporte |  |
