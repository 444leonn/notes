---
base: "[[Introduccion al Desarrollo de Software.base]]"
cover: "[[banner-debian.jpeg]]"
Clase Grabada: https://youtu.be/oix2WMpNBB4?si=Mnti59pDk-_1UJCC
Fecha: 2025-05-28T22:58:00
Descripción: Instalación Linux, Comandos (continuación), Variables, Scripts, Ejercicios.
Diapos:
  - 2243f454-0dd6-807b-95a2-c5abe365a4a5
---
## Instalación de Linux

Alternativas de instalación y consulta para los que no tienen el SO instalado

- [Windows Subsystem for Linux (WSL)](https://www.youtube.com/watch?v=Tlx7qZCPIsA) (No recomendable para más adelante)
- Virtual Machine: [VMWare](https://www.vmware.com/) o [VirtualBox](https://www.virtualbox.org/) (solución recomendada)
- Dual Boot

## Comandos (continuación)

### ¿Como saber que hace un comando?

ej.: comando <date>

En la shell podemos ejecutar:

- `date --help`
- `man date`
- `info date`

### **¿Qué nos permiten hacer?**

- Recorrer el sistema de archivos (`<cd>`)
- Ver el contenido, seleccionar y procesar archivos de texto (<`cat`>, <`more`>, <`less`>, <`ls`>, <`mkdir`>)
- Buscar dentro de uno o más archivos algún dato (<`grep`>)
- Crear y borrar archivos (<`touch`> y <`rm`>)
- y mucho más…

### **Procesamiento de texto**

- `awk` - Pattern scanning and processing language
- `cat`- Display file(s)
- `cut` - Extract selected fields of each line of a file
- `diff` - Compara dos archivos.
- `grep` - Busca texto en un archivo y tambien patrones.
- `head` - Display the first part of files
- `less` - Display files on a page-by-page basis
- `sed` - Stream editor, sirve para modificar y cambiar archivos.
- `sort` - Ordena archivos de texto.
- `split` - Separa archivos.
- `tail` - Display the last part of a file
- `tr` - Translate/delete characters
- `uniq` - Filter out repeated lines in a file
- `wc` - Cuenta palabras, lineas o caracteres en un archivo.
- `touch`- Crea un archivo nuevo vacío.

### Editores de Texto dentro de LINUX

- Vim → **sudo apt install vim**
- Nano → **sudo apt install nano**
- ne – The Nice Editor → **sudo apt install ne**
- **GNU Emacs → sudo apt install emacs**
- entre otros…

## Variables y Variables de Ambiente

### ¿Que es una variable?

Una *variable* es una herramienta que nos permite **almacenar información** de algún tipo, en particular puede ser: String, Integer, Array o Constantes.

Además, las variables pueden ser:

### Variables de Ambiente

Para conocer las variables de ambiente se puede usar el comando `**env**` o `**printenv**`.

Algunas de ellas son:

### Variables Locales

Se definen como: `**VARNAME="value"**`

Para usarlas en otros subshells se deberán exportar: `**export VARNAME="value"**`

### Variables Especiales

Bash también tiene algunas variables especiales que son útiles en scripts:

### Declaración de Variables de sólo Lectura

Si querés que una variable no pueda ser modificada después de su asignación, podés declararla como de sólo lectura usando el comando `readonly`:

Cualquier intento de modificar `PI` después de su declaración resultará en un error.

### Eliminar Variables

Podés eliminar una variable del entorno utilizando el comando `unset`:

Después de esto la variable `nombre` ya no estará definida.

## Script

### ¿Que es un script?

Un script es una **secuencia de comandos y operaciones que el shell puede interpretar y ejecutar**.

Esta secuencia de comandos se suelen guardar en un archivo de texto con la extensión .sh (ejemplo *mi_script.sh*) que luego se podrá ejecutar utilizando el comando `**bash**`, `**./**`, `**sh**`, etc. según el shell que estemos utilizando.

De esta forma podremos automatizar tareas.

### **¿Qué esperamos?**

Un Script debería:

## Ejercitación

### Ejercicio 1

1. Crear la siguiente estructura de directorios: Intro → Ejercicio1
    1. Dentro de Ejercicio1 crear un archivo llamado **datos_personales.txt**
2. Listar el contenido para verificar que exista.
3. Editar el archivo creado y agregar: 
28.764.999;Bruno;gutierrez;soltero;36
22.222.222;Alberto;Garcia;casado;55
33.333.333;Claudia;Riccio;soltera;40
55.555.555;Soledad;Villamil;soltera;24

**Solución:**
```bash
mkdir Intro Intro/Ejercicio1
cd Intro/Ejercicio1
touch datos_personales.txt
ls
nano datos_personales.txt
# Edito el archivo agregando la info y lo guardo con CTRL + X + Y
```

### Ejercicio 2

4. Visualizar el contenido del archivo **datos_personales.txt**
5. Realizar una copia del archivo datos_personales.txt, con el nombre **datos_personales_modif.txt**
6. Modificar el archivo **datos_personales_modif.txt**, cambiando la palabra soltero por casado
7. Contar la cantidad de letras del archivo **datos_personales.txt**

### Ejercicio 3

Crear un script que le pregunte al usuario por una **extensión**.

A continuación, el script debe evaluar la existencia de archivos con esa extensión y **listarlos por pantalla**.

```bash
#!/bin/bash

read -p "Ingrese la extension de un tipo de archivo: " ext
find -type f -name "*.$ext"
```

### Ejercicio 4

Crear un script que reciba un parámetro y determine:

```bash
#!/bin/bash

parametro=$1
if [ -d $parametro ]; then
	ls -a $parametro
elif [ -f $parametro ]; then
	cat $parametro
else
	echo "No es archivo, ni directorio"
fi
```