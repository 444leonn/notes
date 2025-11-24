---
base: "[[Algoritmos y Estructuras de Datos.base]]"
Grabacion: https://youtu.be/8kZEBjyYIsg?si=SJjlgOW4e041RUMM
Descripcion: • Recursividad • Backtracking
Fecha: 2025-09-16T18:04:00
Archivo:
  - 2723f454-0dd6-80cf-95da-db2765de0631
---
# Lista

# Recursividad

## Recursividad de Cola

Si la llamada recursiva a si misma es la ultima operacion dentro de dicha funcion.

No hace falta operar con el resultado que recibe de la siguiente llamada recursiva

Nos permite optimizar las llamadas recursivas, para poder reducir el espacio ocupado en el *stack frame.*

# Dualidad

Cualquier cosa escrita de manera Iterativa puede ser escrita Recusivamente y biceversa.

Incluso existen lenguajes que no tienen estructuras iterativas, y son forzados a implementar la recursion.

## Backtracking

La idea es que yo tengo un problema y lo puedo expresar en forma/funcion de las distintas soluciones posibles que tengo.

*“Es una tecnica de reso*

### *Problema Generico*

Tengo un punto inicial y puede elegir entre dos opciones y asi sucesivamente.

![[image 2.png]]

Trato de representar todos los estados posibles de mi problema.

Y si tengo una forma de hacerlo, puedo decir que la solucion a mi problema va a estar en uno de esos estados / casos.

Lo que hago es entonces es recorrer cada uno de esos estados. Esto lo hago con invocaciones recursivas.

Empiezo a recorrer por ejemplo con A → A → A, si no encuentro la solucion, hago un paso hacia atras y puedo ir a B, quedaria A→ A→B.

![[image 3.png]]

Fijandome si puedo tomar otro camino, y si puedo exploro ese camino.

Mas adelante vamos a ver que se conoce como* ****DFS “Distributes FIle System”.*** Busco en profundidad y no a lo ancho.
