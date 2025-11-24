---
base: "[[Introduccion al Desarrollo de Software.base]]"
Clase Grabada: https://youtu.be/naeX6KrP-Xs?si=JS8p-PF1NRI6Ezj0
Fecha: 2025-05-28T22:58:00
Descripción: GIT
Diapos:
  - 2243f454-0dd6-80ea-b898-c7917ef07d39
---
# GIT

## Que es GIT

- Es un sistema de control de versiones distribuido, disenado para manejar desde proyectos pequenos hasta proyectos enormes con rapidez y eficiencia
- Surgió en 2005 gracias a Linus Torvalds para gestionar el desarrollo del kernel de Linux.
- Proporciona un historial detallado de cambios en el código, facilitando la colaboración entre desarrolladores y permitiendo el seguimiento de las modificaciones a lo largo del tiempo.

## Para que Sirve

- Git es esencial en el desarrollo de software, ya que permite la colaboración efectiva, la gestión de versiones y la ramificación del código.
- Entre sus alternativas, se encuentran sistemas como Subversion (SVN) y Mercurial, que aunque ofrecen funcionalidades similares, difieren en su enfoque y uso. Sin embargo, Git es ampliamente preferido por su velocidad y flexibilidad.

## Conceptos Basicos

### Repositorio

Conjunto de Archivos

### Rama / Branch

Linea de trabajo

### Commit

Instantanea de un conjunto de cambios

### Archivo

## Comandos

### init

- Inicializa un nuevo repositorio Git en el directorio de trabajo actual.
- Crea los archivos y directorios necesarios para almacenar el historial de confirmaciones, las ramas y otra información del repositorio.

### add

- Agrega archivos cambiados al área de preparación.
- El área de preparación es una etapa temporal donde los archivos se almacenan antes de ser confirmados en el repositorio.
- Solo los archivos que se agregan al área de preparación se incluirán en la siguiente confirmación.

### status

- Muestra el estado actual del repositorio.
- Indica qué archivos se han cambiado y si se han agregado al área de preparación.
- También muestra el último estado del repositorio remoto y si hay cambios que aún no ha extraído.

### commit

- Registra los cambios almacenados en el área de preparación en el repositorio.
- Crea una nueva instantánea del estado del repositorio.
- Permite agregar un mensaje de confirmación que describe los cambios que ha realizado.

### log

- Muestra el historial de confirmaciones del repositorio.
- Muestra una lista de todas las confirmaciones que se han realizado en el repositorio, junto con el mensaje de confirmación, el autor y la fecha de la confirmación.
- Puede usar opciones para filtrar el historial de confirmaciones por autor, fecha o mensaje de confirmación.

# GitHub

## Que es GitHub?

- GitHub es una plataforma de alojamiento de código fuente basada en la nube que permite a los desarrolladores:
    - Alojar y compartir proyectos de código fuente.
    - Realizar un seguimiento de los cambios en el código mediante el control de versiones.
    - Colaborar con otros desarrolladores en proyectos.
    - Descubrir nuevos proyectos de código fuente.

### clone

- Crea una copia completa del repositorio remoto en su computadora local.
- Descarga el historial completo de confirmaciones, ramas y etiquetas del repositorio remoto.
- Permite comenzar a trabajar con el repositorio de inmediato sin necesidad de extraer los cambios manualmente.

### fetch

- Descarga los cambios del repositorio remoto al repositorio local.
- No fusiona los cambios con su rama local actual.
- Permite ver qué cambios se han realizado en el repositorio remoto desde la última vez que extrajo.

### push

- Envía los cambios locales al repositorio remoto.
- Actualiza el repositorio remoto con los últimos cambios que ha realizado en su repositorio local.
- Permite compartir sus cambios con otros colaboradores.
- Para pusher en una rama en especifico hacemos 

### pull

- Obtiene los últimos cambios del repositorio remoto y los fusiona en su repositorio local.
- Actualiza su repositorio local con los últimos cambios que han realizado otros colaboradores.
- Permite asegurarse de que está trabajando con la última versión del código.

### merge

- Se utiliza para combinar dos o más historiales de confirmaciones en un solo historial.
- Se puede utilizar para integrar cambios de diferentes ramas o para resolver conflictos de fusión que pueden surgir.
- merge es una herramienta esencial para trabajar con equipos de desarrollo y para mantener un historial de confirmaciones limpio y organizado.

## Conflictos

- Los conflictos de Git se producen cuando dos personas están trabajando en los mismos archivos y realizan cambios en las mismas líneas de código.
- Cuando intenta fusionar los cambios de las dos ramas, Git no puede combinar automáticamente los cambios y se produce un conflicto.
- Deberá resolver el conflicto manualmente editando los archivos y decidiendo qué cambios desea conservar

## Esquema de Ramas

![[image 48.png]]

## Pull Request

- Solicitud de integración de cambios en una rama principal del proyecto
- Revisión y discusión de código por parte de otros desarrolladores
- Proceso clave en el desarrollo colaborativo
- Beneficios:
    - Revisión de Código: Permite detectar y corregir errores antes de la integración.
    - Colaboración: Fomenta la comunicación y el trabajo en equipo.
    - Documentación: Registra el historial y la justificación de cambios.

# Links

[https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)