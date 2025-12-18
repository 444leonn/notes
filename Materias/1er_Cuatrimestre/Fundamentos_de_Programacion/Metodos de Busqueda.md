---
base: "[[Fundamentos de Programacion.base]]"
Descripcion: Busqueda
Fecha: 2025-06-30T15:38:00
Archivo: []
---
# Búsqueda Secuencial (Linear Search)

## Concepto Básico

La búsqueda secuencial es un algoritmo simple para encontrar un elemento en un arreglo o lista. Consiste en recorrer el arreglo elemento por elemento, comparando cada uno con el valor buscado hasta encontrarlo o llegar al final de la estructura.

## Características Principales

- **No requiere arreglo ordenado**: Puede utilizarse en cualquier lista, ordenada o no.
- **Complejidad temporal**:
    - Mejor caso: $O(1)$ (si el elemento está en la primera posición)
    - Peor y caso promedio: $O(n)$ (donde $n$ es la cantidad de elementos)
- **In-place**: No requiere espacio adicional significativo.
- **Simplicidad**: Muy sencilla de implementar.

## Implementación en C

```c
int busqueda_secuencial(tvector valores, int tamanio, int buscado) {
  int i = 0, posicion = NO_ENCONTRADO;
  bool encontrado = false; 
  
  // mientras no se encontro y restan elementos por comparar
  while (!encontrado && i<tamanio) {
    if (valores[i] == buscado) {
        encontrado = true;
        posicion = i;
    }
    i++; 
  }

  return posicion;
}
```

## Ventajas y Desventajas

**Ventajas**:

- Funciona en cualquier tipo de lista o arreglo, ordenado o no
- Muy fácil de implementar
- Útil para listas pequeñas o cuando no se requiere mucha eficiencia

**Desventajas**:

- Muy ineficiente para listas grandes
- Requiere recorrer toda la lista en el peor caso

# Búsqueda Binaria (Binary Search)

## Concepto Básico

La búsqueda binaria es un algoritmo eficiente para encontrar un elemento en un arreglo **ordenado**. Funciona dividiendo repetidamente el rango de búsqueda a la mitad, comparando el elemento buscado con el elemento central, y descartando la mitad en la que el elemento no puede estar.

## Características Principales

- **Requiere arreglo ordenado**: Solo funciona correctamente si los datos están ordenados.
- **Complejidad temporal**:
    - Mejor caso: O(1) (si el elemento es central en la primera comparación)
    - Peor y caso promedio: $O(log_2(n))$
- **In-place**: Puede implementarse sin requerir espacio adicional significativo.
- **No es estable**: No es relevante ya que no reordena elementos, solo los busca.

## Implementación en C

```c
int busqueda_binaria(tvector valores, int tamanio, int buscado) {
  int inf, sup, mit;
  bool terminado; 
  int posicion;
  
  // inicializaciones
  inf = 0;
  sup = tamanio-1;
  terminado = false;

  while (!terminado) {
      if ((buscado < valores[inf]) || (buscado > valores[sup])) {
          terminado = true; // NO ESTA => FIN DE LA BUSQUEDA
          posicion = NO_ENCONTRADO;
      } else {
          mit = inf + ((sup-inf)/2); // evitamos overflow de la suma directa

          if (valores[mit] == buscado) {
            terminado = true; // ENCONTRADO => FIN DE LA BUSQUEDA
            posicion = mit;
	          } else if(buscado > valores[mit]) {
            inf = mit + 1;
          } else {
            sup = mit - 1;
          }
      }        
  }

  return posicion;
}
```

## Ventajas y Desventajas

**Ventajas**:

- Mucho más rápida que la búsqueda lineal para arreglos grandes
- Fácil de implementar
- Eficiente en términos de comparaciones

**Desventajas**:

- Solo funciona sobre estructuras de datos ordenadas
- No es adecuada para listas enlazadas o estructuras sin acceso aleatorio rápido
- Requiere que el arreglo permanezca ordenado

# Comparación entre Busquedas

| Característica | Búsqueda Binaria | Búsqueda Lineal |
| --- | --- | --- |
| Requiere orden | Sí | No |
| Complejidad | O(log n) | O(n) |
| Ideal para | Datos ordenados | Datos pequeños o no ordenados |
| Acceso aleatorio | Necesario | No necesario |
