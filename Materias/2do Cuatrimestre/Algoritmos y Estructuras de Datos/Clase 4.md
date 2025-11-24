---
base: "[[Algoritmos y Estructuras de Datos.base]]"
Grabacion: https://youtu.be/LhD4Qp18tFM?si=1ZZw2NwMGr4Ww0Ta
Descripcion: |-
  • Más práctica de punteros
  • Consultas de Análisis de Algoritmos
  • Teorema Maestro
Fecha: 2025-08-28T17:48:00
Archivo: []
---
# Parcialito

# Cosas

## Flags de C

- `-std=c99` : restringe el estandar al c99, si hay funciones en el programa fuera del estandar no compila
- `-Wall` : da warnings sobre cosas que son sencillas de arreglar
- `-Wconversion` : da warnings sobre conversiones da tipos en operaciones que pueden cambiar el valor
- `-Wtype-limits` : da warnings en comparaciones que pueden llegar a dar siempre true o siempre false
- `-pedantic` : advierte sobre cosas que estan fueras del estandar
- `-Werror` : convierte todas las advertencias de compilacion en errores
- `-O2` : optimiza el codigo para mejor rendimiento
- `-g` : incluye informacion de depuracion (sirve para que valgrind pueda dar mejor descripciones de donde estan sucediendo las cosas)

## Debuggear con GDB

Para debugear un programa debemos hacer `gdb <programa-compilado>`

- `set args "<arg1>" "<arg2>" etc..` nos permite pasarle los parametros que quiero al programa.
- `CTRL + X + A` y nos abre la vista del codigo que esta ejecutando.
- `ulimit -c unlimited `esto nos permite tener un archivo core con el contexto del momento en que fallo nuestro programa
- y lo podemos levantar con gdb en el programa como `core-file core`  o `core-file <nombre_archivo_core>`

### Comandos esenciales

- `run` : corre todo el programa completo
- `start`: inicial el programa y frena en la primer linea del main
- `n` : *next *avanza una linea
- `s` : *step,* si estamos en una invocacion a una funcion podemos entrar a debugear la funcion completa

## Sobre header files (.h)

Protectores de encabezado estan dados por

```c
#ifndef <nombre_encabezado>_H_
#define <nombre_encabezado>_H_

// declaraciones de las funciones

#endif
```

