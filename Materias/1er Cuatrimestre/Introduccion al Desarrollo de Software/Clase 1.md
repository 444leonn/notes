---
base: "[[Introduccion al Desarrollo de Software.base]]"
cover: "[[Clase 1.png]]"
Clase Grabada: https://youtu.be/KoHldfY6cL4?si=0SK6-aGhwC2-XBQt
Fecha: 2025-05-28T22:58:00
Descripción: Regimen de Cursada, Sistema Operativo, LINUX, Shell, Terminal y Comandos.
Diapos:
  - 2243f454-0dd6-80dd-a8d3-f62b9ac37b83
---
## Regimen de Cursada

## Sistema Operativo:

Debe poder comunicarse con el HARDWARE, y eso lo hace a través del **KERNEL**, que se encarga del **MULTITASKING **y la gestión de archivos.

Luego también se encuentra el **SHELL** que permite interactuar con el Sistema Operativo, como por ejemplo: “sh”, “bash”.

Y por ultimo están las **UTILIDADES** creadas gracias al **GNU**, como por ejemplo: “sort”, “cat”, “wc”, “gcc”.

### LINUX

Linux es un **sistema operativo** creado bajo el modelo de software libre. Comenzó como el proyecto personal en 1991, paralelo al proyecto GNU que comenzó en 1983.

El estudiante fue Linus Torvalds, y el “hobby” del que habló eventualmente se convirtió en lo que hoy conocemos como Linux.

Linux, un sistema operativo con todas las funciones similar a POSIX (Interfaz de sistema operativo portátil Unix), ha sido desarrollado no sólo por Linus, sino por cientos de programadores de todo el mundo.

<!-- Column 1 -->
Existen muchísimas distribuciones Linux, todas comparten el Kernel.

<!-- Column 2 -->
![[ccD6Iyz_-_Imgur.gif]]

### TERMINAL

Es una interfaz que permite escribir ordenes e interactuar con el SO.

→ Comandos, Variables de Ambiente, Estructuras de Control: (if, bucles, iteraciones).

→ Existen multiples versiones de TERMINALES o SHELLS.

→ El lenguaje que se utiliza en la terminal es **BASH **(GNU Bourne-Again Shell).

### SHELL

El Shell es un programa que interpreta las órdenes que escribimos en la terminal para interactuar con el SO:

- Nos provee de comandos, estructuras de control y variables de ambiente.
- Linux soporta múltiples Shells! Por defecto es **Bash** (The GNU Bourne-Again Shell), pero también existen:
    - The Bourne Shell (sh)
    - The C Shell (csh)
    - The Korn Shell (ksh)
    - The Z Shell (zsh)

Al final de la materia nos van a pedir crear un **SCRIPT** que es un conjunto de comandos que se ejecutan a la vez.

### Sistema de Archivos

![[image 58.png]]

### Implementación del Sistema de Archivos de dos partes

![[image 59.png]]

### LINEA DE COMANDOS

El prompt esta conformado de la siguiente manera:

`<username>@<computer>:<path> $ comando`

![[image 60.png]]

### NAVEGAR EN EL FILESYSTEM

Algunos comandos que podemos utilizar:

- `pwd`: nos indica el directorio actual.
- `ls` : lista los archivos de ese directorio.
- `cd` : cambio de directorio.
- `cp [file1] [file2] ` : copiar archivo.
- `mkdir` : “Make Directory” crea directorio.
- `rmdir` : “Remove (empty) Directory” borre directorio (no borra uno con archivos).
- `mv [file [destination o name]` : Move/Rename file.
- `rm` : Remove -r para recursivo.
- `touch` : Sirve para crear un archivo.
- `file [file]` : Identifica el tipo de archivo.
- `less [file]` : Page through file (Muestra por paginas el contenido de un archivo muy largo).
- `head -n N [file] ` : Display first N lines (muestra las primeras N lineas
- `tail -n N [file]`: Display last N lines (muestra las 
- `ln –s [file] [new]` : Create symbolic link
- `cat [file] [file2…]` : Display file(s)
- `tac [file] [file2…]` : Display file in reverse order
---
Si no nos acordamos para que sirve un comando usamos:
`man “comando”` Y nos va a mostrar todo, absolutamente todo sobre ese comando.
---

### CARACTERES ESPECIALES

- **~** tu directorio home (ejemplo, /usr1/tutorial/tuta1)
- **.** directorio actual
- **..** directorio padre
- ***** comodín (reemplaza cualquier nombre de archivo)
- **?** comodín que reemplaza cualquier caracter
- **TAB** intenta completar cualquier nombre parcialmente escrito

### **Comando <ls>**

- `**ls -a**`** → **lista todos los archivos (incluidos ocultos “.”)
- `**ls –l **`**→ **lista los detalles de un directorio
- `**ls –lR**`** → **lista los detalles de un directorio en forma recursiva
- `**ls –lh **`**→ **lista el directorio en detalle (el tamaño de los archivos se muestra en Kbytes)
- `**ls –lS **`**→ **lista ordenado el directorio por tamaño
- `**ls –lt**`** → **lista los archivos ordenados por fecha de creación