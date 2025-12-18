---
base: "[[Organizacion del Computador.base]]"
Fecha: 2025-11-07T12:00:00
Descripción: • Funciones de C en Assembler
Diapos:
  - 2a43f454-0dd6-8017-b658-db11e2704a38
---
# Funciones de C en Assembly - Caso de Estudio Intel

## Manejo de Parámetros

### Convención de Llamada

<!-- Column 1 -->
**Linux:**

- Valor de Retorno: `rax`
- Parámetros: `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9`, stack...

<!-- Column 2 -->
**Windows:**

- Valor Retorno: `rax`
- Parámetros: `rcx`, `rdx`, `r8`, `r9`, stack...

### Ajustes de Stack

<!-- Column 1 -->
**Linux:**

- Restar 8 bytes antes del `call`
- Sumar 8 bytes después del `call`

<!-- Column 2 -->
**Windows:**

- Restar 32 bytes antes del `call` a funciones externas
- Sumar 32 bytes después del `call`

### Registros Caller-Saved

<!-- Column 1 -->
**Linux:** `rax`, `rcx`, `rdx`, `r8-r11`, `rdi`, `rsi`

<!-- Column 2 -->
**Windows:** `rax`, `rcx`, `rdx`, `r8-r11`

---

## Funciones de Entrada/Salida

### puts - Salida Simple por Pantalla

```c
int puts(const char *str)
```

Imprime un string hasta encontrar un 0 binario y agrega fin de línea automáticamente.

### printf - Salida Formateada

```c
int printf(const char *format, arg-list)
```

Convierte parámetros a string con el formato especificado.

**Especificadores principales:**

- `%hhi` - entero con signo 8 bits (Linux)
- `%hi` - entero con signo 16 bits
- `%i`, `%d` - entero con signo 32 bits
- `%li` - entero con signo 64 bits (Linux) / 32 bits (Windows)
- `%lli` - entero con signo 64 bits (Windows)
- `%o` - entero sin signo base 8
- `%x` - entero sin signo base 16
- `%c` - caracter
- `%s` - string

### gets - Entrada por Teclado

```c
char *gets(char *buffer)
```

Lee caracteres hasta presionar 'enter' y agrega un 0 binario al final.

---

## Funciones de Conversión

### sscanf - String a Entero

```c
int sscanf(const char *buffer, const char *format, arg-list)
```

Lee datos desde un string y los convierte al formato indicado. Retorna la cantidad de conversiones exitosas.

### sprintf - Entero a String

```c
int sprintf(char *str, const char *format, arg-list)
```

Convierte parámetros a string con el formato indicado y agrega un 0 binario al final.

---

## Manejo de Archivos

### fopen - Apertura

```c
FILE *fopen(char *fileName, char *mode)
```

Abre un archivo en el modo especificado. Retorna un ID de archivo o código de error (negativo).

**Modos principales:**

- `r` - lectura texto
- `w` - escritura texto (trunca/crea)
- `a` - append texto
- `r+` - lectura + escritura texto
- `rb` - lectura binario
- `wb` - escritura binario
- `ab` - append binario
- `rb+` - lectura + escritura binario

### fgets - Lectura de Texto

```c
char *fgets(char *s, int size, FILE *fp)
```

Lee `size-1` bytes (o hasta fin de línea) y los copia en `s`.

### fread - Lectura Binaria

```c
int fread(void *p, int size, int n, FILE *fp)
```

Lee `n` bloques de `size` bytes. Retorna cantidad de bloques leídos.

### fputs - Escritura de Texto

```c
char *fputs(const char *s, FILE *fp)
```

Copia bytes hasta encontrar 0 binario (no se copia el 0).

### fwrite - Escritura Binaria

```c
int fwrite(void *p, int size, int n, FILE *fp)
```

Escribe `n` bloques de `size` bytes. Retorna cantidad de bloques escritos.

### fclose - Cierre

```c
void fclose(FILE *fp)
```

Cierra el archivo identificado por `fp`.

---

## Notas Importantes

> **Función system:** La función `system()` para ejecutar comandos del sistema operativo **NO FUNCIONA** correctamente en Windows en este contexto.

> **Diferencias críticas:** Las principales diferencias entre Linux y Windows están en los registros usados para parámetros y el espacio de stack que debe reservarse antes de llamar funciones.