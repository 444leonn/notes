# Final 1 - 1C 2025

## Ejercicio 1

Ordene el siguiente vector de menor a mayor utilizando Quick-sort.  
Muestre cada paso del algoritmo.  
Justifique la complejidad.  
Explique qué cuidado hay que tener para al aplicar el Teorema Maestro y por qué estas consideraciones no son necesarias en el caso de Merge-sort.

Quick-Sort funciona tomando una posición del vector como "pivote", y otra como "posición pivote", y se compara cada elemento del vector con el pivote y si se debe se intercambia con el de la "posición pivote", luego la posición pivote avanza en un indice.  
Así hasta recorrer todos los elementos del vector, finalmente se intercambia pivote con posición pivote y se repite el proceso con los vectores resultantes a izquierda y derecha del pivote.

La complejidad del algoitmo podemos decir que en el caso promedio es de $O(n log(n))$ ya que en cada recorrido podemos dividir el vector en la mitad.  
Pero en el caso de que el pivote y la posicion pivote no resulten en intercambios, el vector a recorre en cada iteracion sera de una unica uncidad menor del tamano general. Lo cual lleva la complejidad de $O(n^2)$  
![](1C-2025-dibujo-punto-1)  
A la hora de Aplicar el Teorema Maestro debemos tener precauciones ya que la forma a utilizar debe cumplir con ciertos requisitos o caracteristicas para que el problema de recursion sea resuelto por este metodo.  
$$
	T(n) = a T(n/b) + O(f(n))
$$
Debe Cumplirse:

- $ a >= 1 $: ya que es la cantidad de invocaciones recursivas por cada llamada.
- $ b > 0 $: ya que es la taza en que se decrementa el tamaño del problema.
- $ f(n) $: debe ser una función polinomica creciente ya que es el costo computacional del resto de operaciones de cada llamada.

Por lo tanto si alguna de estas condiciones no se cumple no podemos asegurar que el Teorema de la solución correcta o exacta a la complejidad de esa función.

## Ejercicio 2

Explique cómo funciona un árbol B y qué características lo definen.  
En un árbol B con 3 claves por nodo, inserte los siguientes elementos en el orden dado: 'M', 'A', 'L', 'T', 'G', 'R', 'I', 'O', 'S'.  
Luego elimine 'M' y 'R'.  
Muestre el estado del árbol en cada paso.

Un *Arbol B* es un tipo de Arbol de Busqueda el cual se caracteriza por tener la menor profundidad posible, o menor cantidad de niveles posible.  
Suele almacenar en cada nodo una determinada cantidad de claves y entre cada clave un nodo hijo, del mismo tipo que el padre. Es por este motivo que se suelen ser utiles para menejar grandes volumenes de datos, ya que por ejemplo, si se utilizaran archivos se podria acotar la busqueda de manera eficiente al no tener que revisar cada archivo del nivel, sino que sabiendo los valores que almacenan entre cada archivo se puede ir avanzando sobre los nodos hasta encontrar el archivo con el contenido/longitud adecuado.  
Ademas se establece que antes de agregar un nuevo nivel de profundidad al Arbol se debe poseer el nivel padre completo.

## Ejercicio 3

Explique qué es el algoritmo de Dijkstra y para qué sirve. Aplíquelo al siguiente grafo mostrando el resultado de cada paso y el resultado final comenzando desde A.  
![](../images/1C-2025-final-1.png)
		
El *Algoritmo de Dijkstra* es un algoritmo que podemos aplicar a Grafos Pesados el cual nos permite encontrar todos los caminos mínimos desde un vértice de origen, al resto de los vertices que componen el grafo.  
Para aplicar el algoritmo  colocamos en un tabla de 3 columnas los siguiente:
	
1. Vertices del Grafo
2. Vertice Anterior
3. Peso de la arista.

Y utilizamos 2 listas una de vertices ya visitados y otra de vertices no visitados

Y completamos con los pesos de las aristas conocidas, y las que no marcamos como infinito.  
Luego visitamos el vertice adyacente cuya arista sea la de menor peso, y lo marcamos como visitado.  
Volvemos a verificar los pesos de aristas de ese vertice sumandole el peso acumulado anterior, y visitamos el de menor peso.


I) Completo la tabla con lo conocido
Visitados = [A]
No visitados = [B, C, D, E , F, G, H, I]

| VERTICE | V. Anterior | Peso |
|---------|-------------|------|
| A       | -           | -    |
| B       | A           | 5    |
| C       | A           | 3    |
| D       | A           | 7    |
| E       | -           | inf  |
| F       | -           | inf  |
| G       | -           | inf  |
| H       | -           | inf  |
| I       | -           | inf  |

II) visito el vertice conocido de menor peso (C)
Visitados = [A, C]
No Visitados = [B, D, E, F, G, H, I]

No actualizo ningun peso

| VERTICE | V. Anterior | Peso |
|---------|-------------|------|
| A       | -           | -    |
| B       | A           | 5    |
| C       | A           | 3    |
| D       | A           | 7    |
| E       | -           | inf  |
| F       | -           | inf  |
| G       | -           | inf  |
| H       | -           | inf  |
| I       | -           | inf  |

III) visito el vertice conocido de menor peso y de la lista de no visitados (B)
Visitados = [A, B, C]
No Visitados = [D, E, F, G, H, I]

| VERTICE | V. Anterior | Peso |
|---------|-------------|------|
| A       | -           | -    |
| B       | A           | 5    |
| C       | A           | 3    |
| D       | A           | 7    |
| E       | B           | 8    |
| F       | B           | 9    |
| G       | -           | inf  |
| H       | -           | inf  |
| I       | -           | inf  |

IV) visito el vertice conocido de menor peso y de la lista de no visitados (B)
Visitados = [A, B, C]
No Visitados = [D, E, F, G, H, I]

| VERTICE | V. Anterior | Peso |
|---------|-------------|------|
| A       | -           | -    |
| B       | A           | 5    |
| C       | A           | 3    |
| D       | A           | 7    |
| E       | B           | 8    |
| F       | B           | 9    |
| G       | -           | inf  |
| H       | -           | inf  |
| I       | -           | inf  |

4. Explique qué son los puntos de articulación de un grafo.  
Escriba (en C99 o Python) un algoritmo para obtener los puntos de articulación.  
Explique cómo funciona y aplique el algoritmo al grafo del punto 3.
	
Los puntos de articulación son aquellos vertices dentro de un grafo que si son eliminados, aumentan la cantidad de componentes conexas que posee el grafo.  
Un algoritmo posible para encontrar los puntos de articulacion es uno similar al DFS, pero haciendo verificaciones.  
Podemos decir que un Vertice V dado es un punto de articulacion si:  

- V es la raiz del arbol obtenido por DFS y tiene mas de 2 hijos
- V no es raiz, y alguno de sus hijos no tiene forma de volver hacia los vertices superiores a V en el arbol.

```python
def puntos_articulacion(grafo):
	visitados = []
	inicio = list(grafo.keys())[0]
	orden = {}
	p_art = []
	mas_bajo = {}
	def puntos_articulacion_recursivo(grafo, vertice, visitados, es_raiz, orden, mas_bajo, p_art):
		visitados.append(vertice)
		hijos = 0
		for adyacente in grafo[vertice]:
			if adyacente not in visitados:
				orden[adyacente] = orden[vertice] + 1
				hijos += 1
				puntos_articulacion_recursivo(grafo, adyacente, visitados, False, orden, mas_bajo, p_art)
				if mas_bajo[adyacente] >= orden[vertice]:
					p_art.append(vertice)
				mas_bajo[vertice] = min(mas_bajo[vertice], mas_bajo[adyacente])
			else:
				mas_bajo[vertice] = min(mas_bajo[adyacente], orden[adyacente])
		if es_raiz and hijos > 1:
			p_art.append(vertice)

	puntos_articulacion_recursivo(grafo, inicio, visitados, True, orden, mas_bajo, p_art)

	return p_art
```

## Ejercicio 5

Explique qué es un diccionario y para qué se utiliza.  
Explique cómo implementar un diccionario utilizando una tabla de hash de direccionamiento cerrado.  
Dicho diccionario debe poseer una primitiva que permita iterar las claves insertadas (en orden de inserción).  
Muestre cómo debería ser la estructura en memoria y explique cómo funcionan las operaciones de inserción, eliminación iteración y búsqueda.  
Justifique la complejidad de cada operación.  

Un diccionario es un Tipo de Dato Abstracto el cual consiste en relacionar valores de manera que tenemos `claves` que identifican los identifican, lo cual nos permite acceder a esos valores almacenados conociendo la `clave` que lo identifica.  

Una de las maneras de implementacion que existen para estos TDA son las Tablas de Hash, la cual se encarga de transformar las claves en un valor asociado que lo identifica dentro de la tabla mediante una Funcion de Hash, las cuales pueden ser Cerradas (con direccionamiento abierto) o Abiertas (con direccionamiento cerrado), la diferencia se basa en si los valores son almacenados directamente sobre la estructura de la tabla en si (cerrada), o en una estructura auxiliar (lo que la hace abierta).  

Las Tablas de Hash Abiertas con Direccionamiento Cerrado podria implementarse como un vector dinamico en el cual cada uno de sus indice referencia a la estructura auxiliar que se va a utilizar, la cual una opcion sera utilizar una Lista, o quizas un tambien un Arbol Binario de Busqueda.  

De modo que si utilizamos una Lista como estructura auxiliar, al momento de resolver una colision (cuando dos claves distintas resultan en el mismmo valor hasheado), pondremos ese par clave/valor, al final de la lista.  

Se busca evitar las colisiones mediante lo que llamamos como *factor de carga*, en donde almacenamos un valor maximo admitido de complecion de la tabla de hash, y una vez alcanzado este maximo se debe redimensionar la tabla para poder asegurar la eficiencia de la implementacion.
