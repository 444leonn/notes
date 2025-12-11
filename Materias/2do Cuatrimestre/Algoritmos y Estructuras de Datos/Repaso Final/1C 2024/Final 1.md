# Final 1 - 1C 2024

## Ejercicio 1

Escriba en pseudocódigo (o en C si le parece mas fácil) una implementación de las operaciones de  inserción y eliminación de un heap binario.  
Explique cómo funcionan.  
Justifique en base a estas  implementaciones la complejidad de las operaciones.  

```c
typedef struct nodo {
    struct nodo *izq, *der;
    void *valor;
} nodo_t;

typedef struct heap_binario {
    struct nodo *raiz;
    size_t cantidad;
} heap_binario_t;

bool heap_binario_insertar(heap_binario_t *heap, void* valor)
{

}
```

## Ejercicio 2

Explicar (con diagramas) qué es un Árbol B, sus propiedades y los diferentes casos que se pueden dar  durante la inserción y eliminación.  
Insertar en un Árbol B con 3 claves por nodo los siguientes elementos  en secuencia: [6,8,3,2,5,9,7,12,15,10].  

Un Arbol B es un Tipo de Arbol de Busqueda que nos permite manejar grandes volumnes de datos de manera eficiente.  
En este tipo de arboles cada nivel almacena una determinada cantidad maxima de claves, y entre cada valor almacenado tenemos los nodos hijos.  
Tiene como caracteristicas que no agrega un nivel hasta que el nivel anterior este completo, ya que busca tener la mayor expansion posible.  

## Ejercicio 3

Explique para qué sirve y cómo funcionan el algoritmo de Dijkstra.  
Muestre cómo se aplica paso a paso al siguiente grafo desde C.  
![](../images/1C-2024-final-1.png)  

El Algoritmo de Dijkstra es un algoritmo que nos permite encontrar en grafos pesados, 

## Ejercicio 4

Escriba una función (en C) que reciba un vector (de tamaño arbitrario) de strings y devuelva el primer  string repetido del vector.  
La función debe poder funcionar en tiempo lineal respecto de la cantidad de strings.  
Explique la solución y justifique por qué es lineal.  



## Ejercicio 5

Explique qué es un diccionario y cuáles son sus principales características.  
Haga una comparativa entre  diccionarios implementados con tablas de hash y con árboles autobalanceados.  
Escriba dos fragmentos  de código (en C) donde se evidencie la conveniencia de una implementación por sobre la otra.  

Un Diccionario es un Tipo de Dato Abstracto que nos permite almacenar datos llamados `valores` asociados a `claves` que los identifican.  
Siendo estas claves tambien la forma de acceso a los valores almacenados.  
Entre su caracteristicas podemos encontrar, la insercion de claves y valores, eliminacion, y busqueda.  

|                      |   Insercion   |  Eliminacion  | Busqueda de Clave |
|:--------------------:|:-------------:|:-------------:|:-----------------:|
|    Tabla de Hash     |     O(1)      |     O(1)      |        O(1)       |
| Arbol Autobalanceado |   O(log(n))   |   O(log(n))   |      O(log(n))    |

```c
typedef struct par {
    char *clave;
    void *valor;
} par_t;

typedef struct nodo {
    struct nodo *siguiente;
    struct par;
} nodo_t;

typedef struct hash {
    nodo_t **tabla;
    size_t cantidad;
    float factor_carga;
} hash_t;

void *hash_buscar_elemento_recursivo(nodo_t *nodo, char *clave_buscada)
{
    if (nodo == NULL)
        return NULL;

    if (strcmp(nodo->par.clave, clave_buscada) == 0)
        return nodo->par.valor;

    return hash_buscar_recursivo(nodo->siguiente, clave_buscada);
}

void *hash_buscar_elemento(hash_t *hash, char *clave_buscada)
{
    if (hash == NULL || clave_buscada == NULL)
        return NULL;

    size_t clave_hasheada = funcion_hash(clave_buscada) % hash_cantidad(hash);

    return hash_buscar_elemento_recursivo(hash->tabla[clave_buscada], char *clave_buscada);
}
```

```c
typedef struct par {
    char *clave;
    void *valor;
} par_t;

typedef struct nodo {
    struct nodo *izq, *der;
    void *par;
} nodo_t;

typedef struct avl {
    nodo_t *raiz;
    size_t cantidad;
} avl_t;

typedef struct dic {
    avl_t *avl;
    int (*f_comparador)(void*, void*);
    size_t cantidad;
} dic_t;

void *diccionario_buscar(dic_t *diccionario, char *clave_buscada)
{
    if (diccionario == NULL || clave_buscada == NULL)
        return NULL;
    
    par_t par_buscado;
    par.clave = copiar_clave(clave_buscada);

    return avl_buscar(diccionario->avl, &par_buscado);
}
```

Las diferencias entre estas dos implementaciones de diccionario estan en que en la Tabla de Hash, aunque debemos avanzar recursivamente sobre los nodos enlazados, lo cual es una operacion de complejidad $ O(n) $, buscamos minimizar la cantidad de nodos enlazados almacenados, evitando colisiones generada por la funcion de hash, lo cual hace que tienda a $ O(1) $ en complejidad.  
Esto lo hacemos gracias al *factor de carga* total que tiene nuestro hash, lo cual nos establece el valor maximo de ocupacion que puede tener nuestra tabla considerado optimo, una vez alcanzado o superado este valor se debe redimensionar la tabla con un *"Rehash"* para poder asegurar esta complejidad reducida.  

En cambio en la implementacion con la estructura de soporte del AVL, siempre la complejidad de las operaciones sera de $ O(log(n)) $, ya que las operaciones se basan en la organizacion de los elementos que el mismo posee, permitiendo avanzar sobre una de las bifurcaciones de nodos por iteracion sobre el arbol, reduciendo las posibilidades a la mitad en cada paso.  

Otra diferencia clara es que uno posee colisiones y el otro no, por lo que no se deben aplicar tecnicas de resolucion de las mismas. Como si se deberian de hacer en la tabla de hash, como podria ser el encadenamiento de nodos, o quizas el *probing*, para las tablas de hash abiertas.  