1. Ordene el siguiente vector de menor a mayor utilizando Quick-sort.
	Muestre cada paso del algoritmo.
	Justifique la complejidad.
	Explique qué cuidado hay que tener para al aplicar el Teorema Maestro y por qué estas consideraciones no son necesarias en el caso de Merge-sort.

	Quick-Sort funciona tomando una posición del vector como "pivote", y otra como "posición pivote", y se compara cada elemento del vector con el pivote y si se debe se intercambia con el de la "posición pivote", luego la posición pivote avanza en un indice.
	Así hasta recorre todos los elementos del vector, finalmente se intercambia pivote con posición pivote y se repite el proceso con los vectores resultantes a izquierda y derecha del pivote.

	La complejidad del algoitmo podemos decir que en el caso promedio es de *O(n log(n))* ya que en cada recorrido podemos dividir el vector en la mitad.
	Pero en el caso de que el pivote y la posicion pivote no resulten en intercambios, el vector a recorre en cada iteracion sera de una unica uncidad menor del tamano general. Lo cual lleva la complejidad de *O(n^2)*
	![](1C-2025-dibujo-punto-1)
	A la hora de Aplicar el Teorema Maestro debemos tener precauciones ya que la forma a utilizar debe cumplir con ciertos requisitos o caracteristicas para que el problema de recursion sea resuelto por este metodo.
	$$
		T(n) = a T(n/b) + O(f(n))
	$$
	Debe Cumplirse:
	
	- *a >= 1*: ya que es la cantidad de invocaciones recursivas por cada llamada.
	- *b > 0*: ya que es la taza en que se decrementa el tamaño del problema
	- *f(n)*: debe ser una función polinomica creciente ya que es el costo computacional del resto de operaciones de cada llamada.
	
	Por lo tanto si alguna de estas condiciones no se cumple no podemos asegurar que el Teorema de la solución correcta o exacta a la complejidad de esa función.

 2. Explique cómo funciona un árbol B y qué características lo definen.
	En un árbol B con 3 claves por nodo, inserte los siguientes elementos en el orden dado: 'M', 'A', 'L', 'T', 'G', 'R', 'I', 'O', 'S'.
	Luego elimine 'M' y 'R'. Muestre el estado del árbol en cada paso.
	
	Un *Arbol B* es un tipo de Arbol de Busqueda el cual se caracteriza por tener la menor profundidad posible, o menor cantidad de niveles posible.
	Suele almacenar en cada nodo una determinada cantidad de claves y entre cada clave un nodo hijo, del mismo tipo que el padre. Es por este motivo que se suelen ser utiles para menejar grandes volumenes de datos, ya que por ejemplo, si se utilizaran archivos se podria acotar la busqueda de manera eficiente al no tener que revisar cada archivo del nivel, sino que sabiendo los valores que almacenan entre cada archivo se puede ir avanzando sobre los nodos hasta encontrar el archivo con el contenido/longitud adecuado.
	Ademas se establece que antes de agregar un nuevo nivel de profundidad al Arbol se debe poseer el nivel padre completo.


3. Explique qué es el algoritmo de Dijkstra y para qué sirve. Aplíquelo al siguiente grafo mostrando el resultado de cada paso y el resultado final comenzando desde A.
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
| ------- | ----------- | ---- |
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
| ------- | ----------- | ---- |
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
| ------- | ----------- | ---- |
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
| ------- | ----------- | ---- |
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
	
4.   Explique qué es un diccionario y para qué se utiliza. Explique cómo implementar un
	diccionario utilizando una tabla de hash de direccionamiento cerrado.
	Dicho diccionario debe poseer una primitiva que permita iterar las claves insertadas (en orden de inserción). 
	Muestre cómo debería ser la estructura en memoria y explique cómo funcionan las operaciones de inserción, eliminación iteración y búsqueda.
	Justifique la complejidad de cada operación.