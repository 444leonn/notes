---
base: "[[Algoritmos y Estructuras de Datos.base]]"
Descripcion: ""
Fecha: 2025-09-23T20:22:00
Archivo:
  - 25b3f454-0dd6-809c-9d34-c69aa04baf5f
---
# Como calculo la complejidad de un algoritmo Recursivo

- Metodo de Substitiucion
- Metodo de Arbol Recursivo
- Teorema Maestro.

## Teorema Maestro

Es un teorema matematico que me da la solucion a una relacion de recurrencia

Las ecuaciones de recurrencia deben ser de la forma

$$
T(N) = A\,T\!\left(\frac{N}{B}\right) + F(N)
$$

Donde A ≥ 1, B > 1 y la Función F(N) Debe Ser Polinómica Creciente.

- A: Es La Cantidad De Sub‑Problemas O Llamadas A Función Que Hacemos.
- B: Es La Proporción En La Cual Se Reduce El Problema Respecto A La Entrada (Input).
- F(N): Es El Costo De Dividir Y Combinar Los Pasos.

**Si se cumplen las tres condiciones**

Que significa: que $A \ge 1$ es verdadero, $B > 1$ es verdadero y la función $F(N)$ es polinómica creciente.

Entonces debemos calcular: $log_B(A) = C$

- Si $N^{c} = F(N)$ entonces la complejidad es: $O(log (N) * F(N))$.
- Si $N^{c} < F(N)$ entonces la complejidad es: $O(F(N))$.
- Si $N^{c} > F(N)$ entonces la complejidad es: $O(N^{c})$.

Este teorema nos simplifica muchos calculos.

![[image 4.png]]

![[image 5.png]]

### Qué es una ecuación de recurrencia y cómo se usa para la complejidad

- Una ecuación de recurrencia (o relación de recurrencia) describe el tiempo o el costo T(n) de un algoritmo en función del mismo costo para entradas más pequeñas.
- Es típica en algoritmos recursivos, donde un problema de tamaño n se resuelve llamándose a sí mismo con subproblemas de tamaño menor y agregando el costo del trabajo “no recursivo” (comparaciones, combinaciones, etc.).
- Para obtener la complejidad asintótica:
1) Planteamos T(n) = suma de T(tamaños de subproblema) + costo_no_recursivo(n).
2) Desplegamos/expandimos la recurrencia unas cuantas veces para ver el patrón, o usamos métodos estándar: sustitución, árbol de recurrencia o Teorema Maestro.
3) Simplificamos la suma resultante y expresamos T(n) en notación O, Ω o Θ.

Ejemplo típico: si T(n) = T(n−1) + c·n, al expandir se obtiene una suma aritmética que crece como n², por lo que T(n) es Θ(n²).[[1]](https://www.notion.so/2773f4540dd6807f8734c97b7aa34fb3)

### Ejemplo

Con la ecuación de recurrencia, T(N) = T(N−1) + O(N).

Reescribimos T(N) = T(N−1) + C·N. Podemos ver que C·N es de la familia O(N).

Ahora, si sabemos la ecuación de recurrencia, podemos sustituir y averiguar cuánto vale T(N−1) y así expandimos.

T(N) = T(N−1) + C·N

T(N) = T(N−2) + C·(N−1) + C·N

T(N) = T(N−3) + C·(N−2) + C·(N−1) + C·N

GENERALIZANDO

Podemos usar una variable K para poder calcular T(N) con T(N−K).

T(N) = T(N−K) + C·[(N−K+1) + (N−K+2) + … + N]

Cuando K = N−1 llegamos a la base, que es cuando tenemos un solo elemento, por ende está ordenado. Nos queda:

T(N) = T(1) + C·(2 + 3 + … + N−1 + N)

(2 + 3 + … + N−1 + N). Si nos acordamos de Análisis 1:

∑_{k=2}^{N} k = N(N+1)/2 − 1

Aunque nosotros tenemos que restarle 1 porque arrancamos desde 2, y así probamos que es T(N) = O(N²).[[2]](https://www.notion.so/2773f4540dd6807f8734c97b7aa34fb3)
