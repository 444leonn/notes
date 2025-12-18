---
base: "[[Fundamentos de Programacion.base]]"
Descripcion: Introduccion y Archivos Binarios
Fecha: 2025-05-28T22:58:00
Archivo: []
---
# Manejo de Archivos en C

## Introducción a los Archivos

Un archivo es una colección de información relacionada que se almacena como una unidad en un dispositivo físico. Los archivos permiten que los datos persistan más allá de la ejecución de un programa.

### Características principales:

- **Persistencia**: Los datos se mantienen después de cerrar el programa
- **Tamaño dinámico**: Pueden crecer o reducirse según necesidad
- **Tipos principales**: Binarios y de texto

## Tipos de Archivos

1. **Archivos Binarios**
    - Almacenan datos en formato binario
    - La interpretación depende del programa que los crea/lee
    - Más eficientes en espacio y velocidad
    - No son legibles directamente por humanos
2. **Archivos de Texto**
    - Almacenan datos como caracteres ASCII/Unicode
    - Legibles por humanos y editores de texto
    - Requieren conversión de tipos de datos
    - Menos eficientes que los binarios

## Modalidades de Acceso

### Acceso Secuencial

- Se accede a los datos en orden, uno tras otro
- Para llegar al registro N, deben leerse los N-1 anteriores
- Solo permite agregar datos al final
- No permite modificación directa de registros existentes

**Operaciones básicas**:

3. Apertura del archivo
4. Lectura secuencial
5. Escritura al final
6. Cierre del archivo

### Acceso Directo/Aleatorio (no cubierto en este curso)

- Permite acceder a cualquier registro directamente
- Permite modificar registros existentes
- Requiere conocer la posición del registro

## Implementación en C (Archivos Binarios Secuenciales)

7.  Apertura de archivos

```c
FILE *archivo;
archivo = fopen(nombre, modo);
if (archivo == NULL) {
    printf("Error al abrir el archivo %s\\n", nombre);
}

// Modos comunes:
// "rb" - Lectura binaria
// "wb" - Escritura binaria (crea o trunca)
// "ab" - Append binario (escribe al final)
// "r+b" - Lectura/escritura binaria

```

8. Escritura de datos

```c
typedef struct {
    int id;
    char nombre[50];
    float precio;
} Producto;

void escribirProducto(FILE *archivo, Producto p) {
    fwrite(&p, sizeof(Producto), 1, archivo);
}

```

9. Lectura secuencial

```c
void leerArchivo(FILE *archivo) {
    Producto p;

    rewind(archivo); // Volver al inicio

    while(fread(&p, sizeof(Producto), 1, archivo) == 1) {
        printf("ID: %d, Nombre: %s, Precio: %.2f\\n",
               p.id, p.nombre, p.precio);
    }

    if(feof(archivo)) {
        printf("Fin de archivo alcanzado\\n");
    } else {
        printf("Error de lectura\\n");
    }
}

```

10. Cierre de archivo

```c
fclose(archivo);
```

11. Ejemplo completo.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;
    char nombre[50];
    float precio;
} Producto;

int main() {
    // Crear y escribir archivo
    FILE *archivo = abrirArchivo("productos.dat", "wb");

    Producto productos[] = {
        {1, "Laptop", 999.99},
        {2, "Mouse", 19.99},
        {3, "Teclado", 49.99}
    };

    for(int i = 0; i < 3; i++) {
        escribirProducto(archivo, productos[i]);
    }

    cerrarArchivo(archivo);

    // Leer archivo
    archivo = abrirArchivo("productos.dat", "rb");
    leerArchivo(archivo);
    cerrarArchivo(archivo);

    return 0;
}
```

## Consideraciones importantes

12. **Verificación de errores**: Siempre verificar retorno de funciones de archivos
13. **Buffer**: Usar `fflush` cuando sea necesario
14. **Fin de archivo**: Usar `feof` para detectar fin de archivo correctamente
15. **Modo de apertura**: Elegir el modo adecuado para la operación requerida

## Limitaciones del acceso secuencial

16. Para modificar un registro, debe:
    - Crearse un archivo temporal
    - Copiar todos los registros hasta el deseado
    - Modificar el registro
    - Continuar copiando el resto
    - Reemplazar el archivo original
17. No permite búsquedas directas (siempre debe recorrerse desde el inicio)

## Buenas prácticas

18. Usar nombres descriptivos para archivos
19. Cerrar archivos cuando ya no se necesiten
20. Verificar siempre operaciones de E/S
21. Usar estructuras de tamaño fijo para consistencia
22. Documentar el formato de los archivos binarios

# Manejo de Archivos en C - Segunda Parte

## Pasos para trabajar con archivos

23. **Declaración del puntero a FILE**:

```c
FILE *archivo;  // Variable para manejar el archivo
```

24. **Apertura del archivo**:

```c
archivo = fopen("nombre_archivo", "modo");
```

## Modos de apertura principales:

| Modo | Descripción |
| --- | --- |
| "r" | Lectura (debe existir) |
| "w" | Escritura (crea o trunca) |
| "a" | Append (agrega al final) |
| "r+" | Lectura/escritura (debe existir) |
| "w+" | Lectura/escritura (crea o trunca) |
| "a+" | Lectura/append (escribe al final) |

Para archivos binarios, agregar "b" (ej: "rb", "wb+")

25. **Verificación de apertura**:

```c
if (archivo == NULL) {
    printf("Error al abrir el archivo\\n");
}

```

## Lectura de datos

### Función fread:

```c
size_t fread(void *ptr, size_t size, size_t count, FILE *stream);
```

Ejemplo con estructura:

```c
typedef struct {
    int id;
    char nombre[50];
    float precio;
} Producto;

Producto prod;

// Leer un registro
int leidos = fread(&prod, sizeof(Producto), 1, archivo);
if (leidos != 1) {
    // Manejar error o fin de archivo
}
```

## Escritura de datos

### Función fwrite

```c
fwrite ( puntero, tamaño, cantidad, dir_archivo);
```

- **puntero**: dirección a partir de la cual se debe tomar la información a llevar al archivo.
- **tamaño**: cantidad de bytes a escribir.
- **cantidad**: cantidad de elementos a escribir.
- **dir_archivo**: dirección de la estructura FILE. 

La funcion retorna el número de registros grabados

Ejemplo:

```c
Producto nuevo = {1, "Laptop", 999.99};
int escritos = fwrite(&nuevo, sizeof(Producto), 1, archivo);
if (escritos != 1) {
    // Manejar error de escritura
}
```

## Control de fin de archivo

### Función feof:

```c
int feof ( FILE *fichero );
```

```c
while (!feof(archivo)) {
    fread(&prod, sizeof(Producto), 1, archivo);
    if (!feof(archivo)) {  // Verificar nuevamente después de leer
        // Procesar registro
    }
}
```

### Cierre del archivo

-  Luego de realizar los procesos que se deseen efectuar sobre el
archivo, el mismo debe ser cerrado.
- Se sugiere, evitar realizar varias aperturas y cierres de un mismo archivo, es preferible abrirlo y dejarlo abierto a disposición de aquellos módulos que necesiten utilizarlo, salvo que el mismo sea utilizado sólo para una determinada operación.
- Es conveniente que en el mismo módulo en el que se efectúa la
apertura, se efectúe el cierre.

```c
int fclose ( FILE *fichero );
```

# Ejemplo completo

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;
    char nombre[50];
    float precio;
} Producto;

int main() {
    FILE *archivo;
    Producto prod;

    // Escritura
    archivo = fopen("productos.dat", "wb");
    if (archivo == NULL) {
        printf("Error al crear archivo\\n");
        return 1;
    }

    Producto productos[] = {
        {1, "Laptop", 999.99},
        {2, "Mouse", 19.99},
        {3, "Teclado", 49.99}
    };

    for (int i = 0; i < 3; i++) {
        fwrite(&productos[i], sizeof(Producto), 1, archivo);
    }
    fclose(archivo);

    // Lectura
    archivo = fopen("productos.dat", "rb");
    if (archivo == NULL) {
        printf("Error al abrir archivo\\n");
        return 1;
    }

    printf("Contenido del archivo:\\n");
    while (!feof(archivo)) {
        if (fread(&prod, sizeof(Producto), 1, archivo) == 1) {
            printf("ID: %d, Nombre: %s, Precio: %.2f\\n",
                   prod.id, prod.nombre, prod.precio);
        }
    }
    fclose(archivo);

    return 0;
}
```

# Buenas prácticas

26. **Verificar siempre** las operaciones de apertura, lectura, escritura y cierre
27. **Manejar adecuadamente** el fin de archivo (feof)
28. **Cerrar siempre** los archivos cuando ya no se necesiten
29. **Evitar múltiples aperturas/cierres** innecesarios
30. **Usar sizeof** para determinar tamaños de estructuras
31. **Mantener abierto** el archivo mientras se realizan múltiples operaciones
32. **Documentar** el formato de los archivos binarios