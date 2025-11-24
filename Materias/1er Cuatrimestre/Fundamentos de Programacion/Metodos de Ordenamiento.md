---
base: "[[Fundamentos de Programacion.base]]"
Descripcion: Ordenamiento
Fecha: 2025-05-28T22:58:00
Archivo: []
---
# Ordenamiento de Burbuja (Bubble Sort)

## Concepto Básico

El ordenamiento de burbuja es un algoritmo simple para ordenar elementos en un arreglo o lista. Funciona comparando pares de elementos adyacentes y **intercambiándolos** si están en el orden incorrecto.

## Características Principales

- **Complejidad temporal**:
    - Peor caso: $O(n²)$
    - Mejor caso: $O(n)$ (cuando el arreglo ya está ordenado)
    - Caso promedio: $O(n²)$
- **Estable**: Mantiene el orden relativo de elementos iguales
- **In-place**: Solo requiere una cantidad constante de espacio adicional

## Implementación en C

```c
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        // Últimos i elementos ya están en su lugar
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Intercambiar arr[j] y arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

```

# Ordenamiento de Burbuja Optimizado

El metodo de ordenamiento por burbujeo, se puede optimizar, con el objetivo de reducir la cantidad de iteraciones, en cuanto se detecte que el arreglo que se esta queriendo ordenar ya lo esta.

## Ventajas y Desventajas

**Ventajas**:

- Simple de entender e implementar
- No requiere espacio adicional significativo
- Eficiente para conjuntos de datos pequeños o casi ordenados

**Desventajas**:

- Ineficiente para conjuntos de datos grandes
- Rendimiento pobre comparado con algoritmos más avanzados como QuickSort o MergeSort

## Implementacion en C

```c
void ordenar_por_burbujeo_optimizado (tvec vec, int ml) {
	int i, j, aux;
	
	i = 1;
	bool hubo_intercambio = true;
	
	while ((i < ml) && hubo_intercambio) { // Pasos
		hubo_intercambio = false;
		for (j = 0; j < ml - i; j++) { // Comparaciones
			if (vec[j] > vec[j+1]) {
				aux = vec[j]; // Intercambio
				vec[j] = vec[j + 1];
				vec[j+1] = aux;
				hubo_intercambio = true;
			}
		}
		i++;
	}
}
```

# Ordenamiento por Selección (Selection Sort)

## Concepto Fundamental

El ordenamiento por selección es un algoritmo de ordenamiento **in-place** que divide el arreglo en dos partes: una sublista ordenada y otra sublista desordenada. Funciona encontrando repetidamente el elemento mínimo (o máximo) de la parte desordenada y colocándolo al final de la parte ordenada.

## Características Clave

- **Complejidad temporal**: $O(n²)$ en todos los casos (peor, mejor y promedio)
- **In-place**: Solo requiere $O(1)$ espacio adicional
- **No estable**: Puede cambiar el orden relativo de elementos iguales
- **Pocos intercambios**: Realiza exactamente n-1 intercambios (ventaja cuando los intercambios son costosos)

## Ventajas y Desventajas

**Ventajas**:

- Simple de implementar
- Rendimiento predecible (siempre $O(n²)$)
- Eficiente en términos de número de intercambios (solo n-1 intercambios)

**Desventajas**:

- Ineficiente para listas grandes
- Peor rendimiento que otros algoritmos O(n²) como el insertion sort en la mayoría de casos
- No estable (no mantiene el orden original de elementos iguales)

## Implementación Básica en C

```c
void ordenar_seleccion(tvector vector, int n) {
	int i, j, minimo, aux;
	
	for (i=0; i<n-1; i++) {
		minimo = i;
		for (j=i+1; j<n; j++) {
			if (vector[j] < vector[minimo]) {
				minimo = j;
			}
		}
		aux=vector[i];
		vector[i]=vector[minimo];
		vector[minimo]=aux;
	}
}
```

# Ordenamiento por Insercion (Insertion Sort)

El metodo de ordenamiento como seleccion busca ordenar los elementos del arreglo, tomando un elemento y comparandolo contra los anteriores ya ordenados, deteniendose cuando se encuentra uno menor y entonces alli es donde se inserta, desplazando el resto de los elementos mayores.

## El Algoritmo

- Vamos a recorrer todo el vector `A` comenzando desde la posicion inicial del vector + 1, hasta la ultima posicion.
- Para cada elemento del vector `A[i]`, se trata de ubicar en el lugar correcto el elemento `A[i]` en cuestion, entre los elementos: `A[i-1]` , `A[i-2]` , …, `A[inicial]` .
- Dada la posicion actual *i*, el algoritmo se basa en que los elementos `A[inicial]` , `A[1]` , …, `A[i-1]` . ya estan ordenados

## Complejidad Temporal

- Mejor Caso: $O(n)$
- Peor Caso: $O(n^2/2)$

## Implementacion en C

```c
void ordenar_insercion (tvec vec, int ml) {
	int i, j, aux;
	for (i = 1; i <= ml; i++) {
		aux = vec[i]; // preservo valor
		j = i - 1;
		while ((j >= 0) && (vec[j] > aux)) {
			vec[j+1] = vec[j]; // desplazo elemento
			j = j - 1;
		}
		vec[j+1] = aux;
	}
}
```

# Comparación entre Algoritmos

| Característica | Selection Sort | Bubble Sort | Insertion Sort |
| --- | --- | --- | --- |
| Complejidad | O(n²) | O(n²) | O(n²) |
| Intercambios | O(n) | O(n²) | O(n²) |
| Estabilidad | No | Sí | Sí |
| Rendimiento práctico | Pobre | Pobre | Mejor para pequeños/con casi ordenados |