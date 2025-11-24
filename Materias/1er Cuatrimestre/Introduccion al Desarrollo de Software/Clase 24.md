---
base: "[[Introduccion al Desarrollo de Software.base]]"
Clase Grabada: https://youtu.be/mIPrGtb4CAA?si=LZJcZZ02LQovxPTt
Fecha: 2025-05-29T18:04:00
Descripción: Docker
Diapos:
  - 2023f454-0dd6-802a-b13b-c1113084cedb
---
# Que es Docker?

Docker es una herramienta utilizada para la virtualización de Sistemas Operativos. Utilizado para el desarrollo, ejecución y entrega de software.

## Para que se utiliza

- Solventar problemas de aplicaciones corriendo en distintos sistemas operativos
- La entrega y despliegue de aplicaciones
- Compartir el trabajo con otros desarrolladores
- Crear ambientes de desarrollo con las herramientas justas y necesarias

# Que es un Contenedor?

Son ligeros “paquetes” de software que incluyen todo lo necesario para que uno de los componentes de tu aplicación se ejecute individualmente.

![[image 22.png]]

## Cómo crear contenedores con Docker

Para crear contenedores, necesitamos conocer dos cosas

- Docker files
- Docker images

# Que es un Dockerfile

Es un archivo donde tenemos un escribimos un set de instrucciones para crear una imagen de Docker

![[image 23.png]]

# Que es una Imagen

Las imágenes son utilizadas como plantillas para crear contenedores de Docker. Contienen TODA la información necesaria para crear un contenedor

![[image 24.png]]

# **Contenedores vs Virtual Machines**

<!-- Column 1 -->
![[image 25.png]]

<!-- Column 2 -->
![[image 26.png]]

# DockerHub

Es el repositorio remoto donde guardamos nuestras imágenes para compartirlas con nuestro equipo o con el mundo de desarrolladores.

Ustedes también pueden subir sus propias imágenes de sus aplicaciones. También es del lugar donde descargan las imágenes de distintos sistemas operativos, bases de datos, gestores de bases de datos, lenguajes de programación, aplicaciones de monitoreo, etc.

Link a DockerHub: https://hub.docker.com/

# **Comandos**

## docker pull

Este comando nos permite **descargar **imágenes desde DockerHub

- `docker pull ubuntu` (Hace default a la última versión)
- `docker pull ubuntu:jammy` (Colocamos un tag para descargar una versión en particular)

## docker images

Es un alias para el comando docker image list, nos permite **listar **todas las imágenes dentro de nuestro repositorio local

- `docker images` (Lista todas las imágenes)
- `docker image ubuntu` (Lista todas las imágenes qué matcheen el tag ubuntu)

## docker run

Este comando nos permite crear un contenedor basado en una imagen

- `docker run –name ubuntu_test ubuntu` (Creamos el contenedor pero no va a funcionar)

Necesitamos de unos flags para hacerlo

- `docker run -d -i -t --name ubuntu_test` (--detach, –interactive, –tty)

Hay muchas más opciones de configuración, las pueden ver en

## docker exec

Este comando nos permite ejecutar comandos dentro de un contenedor que ya esté ejecutándose

- `docker exec -it “bin/bash” ubuntu_test` (Nos permite utilizar la consola del contenedor de ubuntu)

## docker ps

Nos permite listar los contenedores que están ejecutándose.

- `docker ps` (Lista solo contenedores ejecutándose)
- `docker ps -a` (Lista también los contenedores apagados)

## docker stop

Nos permite detener la ejecución de un contenedor

- `docker stop ubuntu_test` (También puede ser el id del contenedor)

## docker rm y docker rmi

Nos permite eliminar contenedores e imágenes que ya no necesitemos

- `docker rm ubuntu_test`
- `docker rmi ubuntu`
    - `docker rmi -f $(docker images -aq)` (Borra todas las imágenes)