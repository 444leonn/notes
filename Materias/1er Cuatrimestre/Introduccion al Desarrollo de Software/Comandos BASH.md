---
base: "[[Introduccion al Desarrollo de Software.base]]"
Fecha: 2025-05-28T22:58:00
Descripción: ""
Diapos: []
---
# Comandos utiles en Shell Scripting con Bash.

**cd ("Change Directory"):** Sirve para cambiar y acceder a un directorio.
Ejemplo: cd Desktop
`cd ..` (para ir al directorio padre o uno para atras)

**ls ("List Directory Contents"):** Muestra los directorios.
Ejemplo: ls
`ls -l` (para ver informacion ampliada)
`ls -a `(para ver los directorios ocultos)

**mkdir ("Make Directory"): **Crea directorios
Ejemplo: `mkdir Carpeta1`

**rmdir ("Remove Directory"):** Elimina directorios, si tiene cosas adentro da error.
Ejemplo: `rmdir Carpeta1`

**rm ("Remove"):** Elimina Directorios o archivos. Si agregamos -r es para recursivo y elimina lo que hay dentro del directorio.
Ejemplo:` rm archivo.txt`
`rm -r Carpeta1 `(suponiendo que tiene cosas dentro)

**mv ("Move"): **Sirve para mover archivos, como para tambien renombrarlos.
Ejemplo: mv archivo.txt archivo_renombrado.txt
mv archivo.txt ..

**cp ("Copy"): **Sirve para copiar archivos.
Ejemplo: `cp archivo.txt ..` (copia el archivo con el mismo nombre y todo en el directorio indicado, en este caso es un directorio anterior)
`cp archivo.txt otro.txt` (copia la info del archivo en otro archivo sobrescribiendolo)

**find: **Sirve para buscar archivos o directorios por nombre dependiendo del parametro dado al comando.
Parametro -type (para especificar el tipo de archivo a buscar)
`~f ("file" / "archivo")`
`~d ("directory" / "carpeta")`
Parametro *-name*
Ejemplo: `find -type f -name archivo`
`find /home/leon-acosta/ -type d -name Desktop` (podemos agregar el directorio en el que se realice la busqueda)

**sed:** Editor para buscar y reemplazar palabras.
Se puede utilizar como: `sed 'i/palabra1/palabra2/g' archivo_cualquiera.txt`

**grep:** Sirve para buscar palabras en archivos.
Ejemplo: grep palabra nombre_archivo

**wc ("Word Count"): **Nos permite contar palabras, lineas y/o caracteres en un archivo, dependiendo del parametro que le pasemos.
Ejemplo: wc archivo.txt (cuenta palabras)
`wc -l archivo.txt` (cuenta lineas o renglones)
`wc -c archivo.txt `(cuenta caracteres)

**echo: **Muestra por pantalla el mensaje dado.
Ejemplo: **echo Hola**
Tambien *podemos editar* un archivo de la siguiente manera:
`echo Hola >> archivo.txt`
En donde escribimos el mensaje "Hola" al final de archivo.txt
Si hacemos:
echo Hola > archivo.txt
Sobre escribimos toda la informacion previa del archivo por "Hola", perdiendo lo anterior.

**cat:** Sirve para mostrar por pantalla el contenido de un archivo.
Ejemplo: `cat <archivo>`

**tac:** Al igual que cat, muestra por pantalla el contenido de un archivo pero de manera invertida.
Ejemplo: `tac <archivo>`

**more:** Tambien sirve para mostrar por pantalla el contenido de un archivo, pero, haciendo pausas entre pantallas si el mismo es largo.
Ejemplo: `more <archivo>`

**head:** Muestra las primeras lineas de un archivo.
Ejemplo: `head -n archivo.txt` (siendo n la cantidad de lineas)

**tail:** Muestra las ultimas lineas de un archivo
Ejemplo: `tail -n archivo.txt`  (siendo n la cantidad de lineas)

**passwd: **Sirve para modificar el password del usuario en uso.

**gzip:** Sirve para comprimir un archivo en formato .zip.
Ejemplo: gzip archivo

**gunzip:** Sirve para descomprimir un archivo de formato .zip.
Ejemplo: gunzip archivo

**zcat: **Muestra el contenido de un archivo compreso .zip.

**tar: **Empaquetar y desempaquetar archivos
Ejemplo Empaquetar: tar cvf fichero.tar directorio
Ejemplo Desempaquetar: t`ar xvf fichero.tar`

**nano:** Editor de texto con el cual se pueden crear y modificar archivos.
Ejemplo: nano archivo_existente.txt (edita el archivo)
nano archivo_inexistente.txt (crea el archivo)

**shred:** Comando para cifrar, o modificar de manera ilegible el contenido de un archivo.
Ejemplo: shred archivo.txt
Si usamos el parametro -u, luego de cifrar el contenido lo elimina:
`shred -u archivo.txt`

**sudo ("Super User Do"): **Permite ejecutar comandos con permisos de super usuario, lo cual permite realizar acciones que requieren de permisos adicionales.
Ejemplo: sudo nano archivo_con_permisos.txt
sudo apt-get install paquete
Nos permite instalar paquetes/aplicaciones
`sudo apt-get install google-chrome`
`sudo apt purge paquete`
Permite eliminar paquetes/aplicaciones

**man:** Muestra un manual del comando que se desea consultar.
Ejemplo:` man ls`

**clear: **Borra la pantalla, limpia la vista de la terminal.

**pwd:** Muestra el directorio actual de trabajo.

**env:** Muestra las variables de entorno del programa.


Algunos ejemplos de variables de entorno son: $SHELL, $HOME, $PATH, $USER.

**chmod:** Permite darle permisos a un archivo.
Ejemplo: `chmod ``**a+x**`` `[`archivo.sh`](http://archivo.sh/)
Aqui se le estan dando todos los permisos a [archivo.sh](http://archivo.sh/) que es un script, lo cual permite su ejecucion sin errores de permisos.

$RANDOM: No es un precisamente un comando ya que es mas bien un Variable, pero podemos hacer uso de ella como comando. Lo que hace es generar un numero completamente aleatorio.
Ejemplo: echo $RANDOM (da un numero aleatorio)
echo $((RANDOM%10)) (da un numero aleatorio entro 0 y 10)

**while True:** Usar muy pocas veces porque es una MALA PRACTICA.

sleep: Sirve que para que en un bucle se de un descanso al proceso para que no se cargue tanto en procesos a la maquina.
Se suele implementar con los while True

**read: **Crea un input para que el usuario pueda ingresar datos.
Si se agrega el parametro -p permite agregar texto adicional al input
Y si se asigna un nombre la entrada queda guardad en un variable.
Ejemplo:
`read -p "Seleccione una opcion: " opcion`
en este caso el **-p** tiene el texto "Seleccione una opcion: " y se mostrar por pantalaa
y el opcion de al lado corresponde a la variable que se define en ese momento con el valor digitado en el input.

&: Corresponde al numero del proceso.
Guardar en una variable, y usar para matar kill el proceso de [consolidar.sh](http://consolidar.sh/) en el tp1

# Sed

El comando que has proporcionado es un comando `sed` que se utiliza para editar texto en un archivo. Vamos a desglosar cada parte:

```plain text
sed -i 's/soltero/casado/g' datos_personales_modif.txt

```

### Explicación de las partes:

1. `**sed**`: Es el comando principal para el editor de flujo (stream editor), que permite realizar operaciones de búsqueda y reemplazo en texto.
2. `**i**`: Esta opción significa "edición in-place" (en el lugar). Le indica a `sed` que modifique directamente el archivo especificado en lugar de mostrar los cambios en la salida estándar. Sin `i`, `sed` solo mostraría los cambios en la terminal sin alterar el archivo original.
    - **¡Cuidado!** Si usas `i` sin una copia de seguridad, los cambios son permanentes. En algunas versiones de `sed` (como GNU `sed`), puedes usar `i.bak` para crear una copia de seguridad antes de modificar el archivo.
3. `**'s/soltero/casado/g'**`: Esta es la expresión de sustitución (replace) de `sed`.
    - `**s**`: Indica que es una operación de **sustitución** (del inglés *substitute*).
    - `**soltero**`: Es el texto que se busca (expresión regular o palabra exacta).
    - `**casado**`: Es el texto por el que se reemplaza.
    - `**g**`: Significa **global**, es decir, reemplaza todas las ocurrencias de "soltero" en cada línea. Si no se usa `g`, solo se reemplaza la primera ocurrencia en cada línea.
4. `**datos_personales_modif.txt**`: Es el archivo sobre el que se aplica el comando.

### Ejemplo de uso:

Si el archivo `datos_personales_modif.txt` contenía:

```plain text
Juan es soltero.
María es soltero y Pedro es soltero.

```

Después del comando, quedará:

```plain text
Juan es casado.
María es casado y Pedro es casado.

```

### Resumen:

- `i` → Modifica el archivo directamente.
- `s` → Indica sustitución.
- `g` → Reemplaza todas las coincidencias (no solo la primera).

Si tuvieras dudas sobre otras opciones de `sed`, ¡avísame!