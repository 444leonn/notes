---
base: "[[Algoritmos y Estructuras de Datos.base]]"
Grabacion: https://youtu.be/rM90uE2sKL8?si=w8TO35RNZ6Xeg_Ik
Descripcion: Punteros y  Memoria Dinamica
Fecha: 2025-08-21T18:31:00
Archivo:
  - 2543f454-0dd6-8055-b41b-f403bfac7947
---
# Cosas Importantes

## Clang (formateador código C)

1. Descargar el compilador clang (`sudo apt-get install clang-format` )
2. Descargar el archivo .clang-format de este link: [https://github.com/torvalds/linux/blob/master/.clang-format](https://github.com/torvalds/linux/blob/master/.clang-format)  y guardarlo en tu carpeta Home con el nombre `.clang-format` (exactamente con ese nombre).
3. En el directorio (carpeta) donde está tu archivo .c, ejecutar la línea `clang-format -i -style=file <archivos a formatear>` .

## Secuencias de Escape ANSI (Colores)

Las secuencias de escape ANSI son una serie de codificaciones que nos permiten manejar el formato del texto de la terminal a nuestro gusto. Existe una gran variedad de estos códigos y distintas maneras de implementarlo.

Para hacer lo hacemos definiendo una constante y poniendo un string con el código de escape que queremos usar.

Ejemplo:

[https://www.youtube.com/watch?v=BvubeR2OjfE&list=PLCURutbAAn2M9IcGCKQ0gUFv-X1O0kkIs&index=2](https://www.youtube.com/watch?v=BvubeR2OjfE&list=PLCURutbAAn2M9IcGCKQ0gUFv-X1O0kkIs&index=2)

## Como parametrizar un programa

Para poder pasarle  parámetros a  nuestro programa de C lo hacemos a través del main, pasandole la cantidad de argumentos y un *char pointer* o un array de char que son los argumentos en si.

Siempre se cuenta al nombre del programa ejecutable como primer argumento (indice 0)

```c#
int main(int argc, char *argv[]) {
	return 0;
}
```

[https://youtu.be/t87bc5EsHEQ?si=re7wMdDIMIvBPxJ6](https://youtu.be/t87bc5EsHEQ?si=re7wMdDIMIvBPxJ6)

## Makefile

Los makefile son archivos que nos ayudan a compilar y hacer distintas cosas con nuestros programas.

Los corremos con `make`  desde la consola, y los ejecuta linea por linea.

```makefile
compilar: archivo.c
	gcc archivo.c -o tp1
```

Si no quiero que se repita la compilación, cambio el nombre de la regla *compilar *por el nombre del archivo ejecutable.

Quedaria tal que asi:

```makefile
CFLAGS=-g -O0

tp1: archivo.c
	gcc archivo.c $(CFLAGS) -o tp1
```

Y si ademas quiero agregar mas dependencias, como por ejemplo probar la perdida de memoria con valgrind lo hago de la siguiente manera.

Accedo a ellas a traves de `makefile <nombre_dependencia>`

```makefile
probar: tp1
	valgrind ./tp1
```

[https://youtu.be/oy-qkZltDiU?si=qL4mdCmRiveoimcM](https://youtu.be/oy-qkZltDiU?si=qL4mdCmRiveoimcM)

## Fgets

Lee una linea completa, y pone el caracter nulo de final de string luego de encontrar un \n.

Por lo que nos permite tener un mejor control de que es lo leyo la funcion, y que es lo que quedo pendiente de leer o en el buffer, por cualquier motivo (no habia espacio en el string).

[https://youtu.be/6e-8bfNAd1U?si=VhyslDlSrPi_sVPG](https://youtu.be/6e-8bfNAd1U?si=VhyslDlSrPi_sVPG)

# Memoria Dinamica

# Punteros

## Por que los necesitamos

Todas nuestras variables y nuestras operaciones de nuestro programa se encuentra en la memoria.
