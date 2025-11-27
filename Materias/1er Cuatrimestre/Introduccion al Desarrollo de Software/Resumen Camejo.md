---
base: "[[Introduccion al Desarrollo de Software.base]]"
cover: "[[Resumen Camejo.jpeg]]"
Fecha: 2025-05-28T22:58:00
Descripción: ""
Diapos: []
---
[https://www.youtube.com/@IntroalDesarrollodeSoftw-bi8xj](https://www.youtube.com/@IntroalDesarrollodeSoftw-bi8xj)

## Temas para el primer parcial

- [ ] **Bash + Comandos de Linux:** Aquí abordaremos cómo usar la shell de bash y los comandos de Linux para navegar y manipular el sistema operativo.
- [ ] **Git + Github:** Este tema cubrirá el uso de Git, una herramienta de control de versiones, y GitHub, una plataforma para alojar código y colaborar en proyectos de desarrollo de software.
- [ ] **Ingeniería de Software:** Finalmente, exploraremos las metodologías y prácticas de la ingeniería de software, incluyendo el desarrollo ágil, la gestión de proyectos, y la calidad del software.
- [ ] **Frontend:** En esta sección, discutiremos la creación de la interfaz de usuario de una aplicación, incluyendo HTML, CSS, y JavaScript.
- [ ] **Python: **Es una introduccion a python, dada en una sola clase.
- [ ] **Backend + Flask:** Este tema se centrará en el servidor, la base de datos, y la lógica de la aplicación, que funcionan detrás de escena para hacer que una aplicación funcione.

# Videos en orden de temas

### Primer parte ( Bash + Linux )

### Segunda parte ( **Git + Github** )

### Tercera parte ( **Ingeniería de Software** )

### Cuarta parte ( **Frontend** )

### Quinta parte “Parte extra”( Python )

### Sexta parte ( Backend + flask )

# Síntesis de la materia

# **Bash + Comandos de Linux**

  **Bash Shell:**
Bash es una interfaz de línea de comandos (CLI) para sistemas operativos Unix y Linux. Proporciona un entorno para escribir, ejecutar y automatizar scripts.

**Navegación en el Sistema de Archivos:**

- `pwd`: Muestra el directorio actual.
- `ls`: Lista los archivos y directorios en el directorio actual.
- `cd`: Cambia el directorio de trabajo.
- `mkdir`: Crea un nuevo directorio.
- `rmdir`: Elimina un directorio vacío.

*Ejemplo en Bash:*

```bash
$ pwd
/home/usuario/proyecto

```

**Manipulación de Archivos:**

- `touch`: Crea un nuevo archivo vacío o actualiza la marca de tiempo de un archivo existente.
- `cp`: Copia archivos y directorios.
- `mv`: Mueve o renombra archivos y directorios.
- `rm`: Elimina archivos y directorios.

*Ejemplo en Bash:*

```bash
$ touch nuevo_archivo.txt

```

**Visualización de Contenido de Archivos:**

- `cat`: Muestra el contenido completo de un archivo.
- `less`: Permite desplazarse por el contenido de un archivo.
- `head`: Muestra las primeras líneas de un archivo.
- `tail`: Muestra las últimas líneas de un archivo.

**Edición de Archivos de Texto:**

- `nano`: Editor de texto simple en la terminal.
- `vi / vim`: Editor de texto avanzado en la terminal.

**Redirección de Entrada/Salida y Tuberías:**

- `>`: Redirige la salida de un comando a un archivo (sobrescribe).
- `>>`: Redirige la salida de un comando a un archivo (agrega al final).
- `<`: Redirige la entrada de un comando desde un archivo.
- `|`: Pasa la salida de un comando como entrada a otro.

**Permisos de Archivos:**

- `chmod`: Cambia los permisos de archivo.
- `chown`: Cambia el propietario y el grupo de un archivo.
- `chgrp`: Cambia el grupo de un archivo.

**Buscar Archivos:**

- `find`: Busca archivos y directorios en el sistema.
- `grep`: Busca texto dentro de archivos.

**Gestión de Procesos:**

- `ps`: Muestra los procesos en ejecución.
- `kill`: Termina un proceso.
- `top`: Muestra los procesos en ejecución en tiempo real.

Dominar estos comandos básicos de la terminal de Linux te permitirá navegar por el sistema de archivos, manipular archivos y directorios, y realizar una variedad de tareas administrativas y de desarrollo en un entorno de línea de comandos.

# **Git + Github**

**Git y GitHub:**
Este tema aborda el uso de Git, una herramienta de control de versiones, y GitHub, una plataforma para alojar código y colaborar en proyectos de desarrollo de software.

**Git:**

- **Descripción:** Git es un sistema de control de versiones distribuido que permite el seguimiento de cambios en el código fuente durante el desarrollo de software.
- **Características clave:**
    - Control de versiones distribuido.
    - Permite ramificar y fusionar cambios fácilmente.
    - Realiza un seguimiento de los cambios a nivel de línea.
    - Facilita la colaboración en equipos de desarrollo.

**GitHub:**

- **Descripción:** GitHub es una plataforma en línea que utiliza Git para alojar y gestionar repositorios de código. También ofrece herramientas para la colaboración en proyectos de software.
- **Características clave:**
    - Alojamiento de repositorios de código.
    - Control de acceso y permisos para colaboradores.
    - Seguimiento de problemas y solicitudes de extracción.
    - Integración con servicios de integración continua y despliegue.

**Uso conjunto:**

- Los desarrolladores utilizan Git para realizar un seguimiento de los cambios en su código localmente.
- GitHub se utiliza para alojar repositorios remotos, permitiendo la colaboración entre desarrolladores y facilitando la revisión de código, el seguimiento de problemas y la implementación de nuevas características.

**Beneficios:**

- Facilita la colaboración entre equipos de desarrollo distribuidos.
- Permite un historial completo de cambios en el código.
- Mejora la productividad al simplificar el seguimiento de problemas y la implementación de nuevas características.
- Fomenta las mejores prácticas de desarrollo de software, como la revisión de código y la integración continua.

**Resumen de comandos para utilizar Git desde la terminal:**

**Configuración inicial:**

- `git config --global user.name "Tu Nombre"`: Configura el nombre de usuario en Git.
- `git config --global user.email "tu@email.com"`: Configura el correo electrónico asociado a tu cuenta de Git.
- `git init`: Inicializa un nuevo repositorio Git localmente en tu proyecto.

**Enlazar GitHub con la PC:**

- `git remote add origin <URL_del_repositorio>`: Enlaza tu repositorio local de Git con un repositorio remoto en GitHub.

**Subir archivos a GitHub:**

- `git add .`: Añade todos los archivos modificados al área de preparación.
- `git commit -m "Mensaje del commit"`: Realiza un commit con un mensaje descriptivo.
- `git push origin master`: Sube los cambios locales al repositorio remoto en GitHub.

**Pulls y Pushes:**

- `git pull origin master`: Descarga y fusiona los cambios desde el repositorio remoto en GitHub al repositorio local.
- `git push origin master`: Sube los cambios locales al repositorio remoto en GitHub.

**Ejemplo de Uso:**
Supongamos que tienes un repositorio en GitHub llamado "mi-proyecto" y quieres subir tus cambios desde la terminal:

Estos comandos básicos te permitirán trabajar con Git desde la terminal y realizar operaciones comunes como subir cambios a GitHub, hacer commits y sincronizar tu repositorio local con el repositorio remoto.

# Mini parcial

[https://forms.gle/Cw9gKsrdAys5Qhyq9](https://forms.gle/Cw9gKsrdAys5Qhyq9)

# INGENIERIA DE SOFTWARE

[[RESUMEN DE LA CLASE DE ING EN SOFTWARE.pdf]]

La ingeniería de software es la disciplina que se encarga de los principios de ingeniería para el desarrollo completo de software, desde su concepción y diseño inicial hasta su implementación, prueba, despliegue y mantenimiento continuo. Se caracteriza por un enfoque iterativo e incremental, donde el desarrollo de software se realiza en ciclos repetitivos, cada uno centrado en agregar nuevas funcionalidades o mejorar las existentes.

Las etapas de la ingeniería de software incluyen:

1. <u>Análisis de requerimientos</u>:    Comprende las necesidades del cliente y los usuarios finales del software. Identifica los objetivos del proyecto, cómo se utilizará el software y qué funcionalidades debe tener.
2. <u>Diseño</u>:              
Después de entender los requerimientos, se procede al diseño del software. Aquí se toman decisiones sobre la arquitectura del software, se seleccionan tecnologías y herramientas adecuadas, y se crea una estructura detallada del sistema.
3. <u>Implementación</u>:           Es el proceso de traducir el diseño del software en código fuente ejecutable. Es importante que la implementación sea organizada y siga las mejores prácticas de codificación para garantizar la legibilidad, eficiencia y seguridad del código.
4. <u>Testing y validación</u>:    Son procesos críticos para asegurar la calidad y confiabilidad del software. El testing implica realizar pruebas exhaustivas en todas las partes del sistema para identificar y corregir errores o defectos. La validación, por otro lado, se enfoca en demostrar que el software cumple con los requerimientos y expectativas del cliente.
5. <u>Despliegue</u>:              Una vez que el software ha sido probado y validado, se procede al despliegue en entornos de producción. Esto implica configurar y lanzar el software en servidores y sistemas en vivo, asegurándose de que esté disponible para su uso por parte de los usuarios finales.
6. <u>Mantenimiento</u>:            Es un proceso continuo que ocurre después del despliegue. Esto incluye la corrección de errores, la aplicación de parches de seguridad, la actualización de funciones y la incorporación de nuevos requerimientos a medida que surgen.

La ingeniería de software es fundamental en el desarrollo de sistemas y aplicaciones informáticas de calidad. Un enfoque estructurado y disciplinado en el proceso de desarrollo de software ayuda a garantizar que los productos sean confiables, seguros, eficientes y fáciles de mantener. Además, la ingeniería de software promueve la colaboración entre equipos multidisciplinarios y la adopción de mejores prácticas de desarrollo, lo que resulta en soluciones de software de mayor calidad y satisfacción del cliente.

# Mini parcial

[https://forms.gle/4G6YGRKM8rzv84QJ8](https://forms.gle/4G6YGRKM8rzv84QJ8)

# FRONTEND : HTML/CSS/JS/BST

  

# HTML ( HyperText Markup Language )

  

HTML es el lenguaje estándar utilizado para crear la estructura de una página web. Se utiliza para definir los elementos y su contenido, como encabezados, párrafos, imágenes, formularios, etc. Proporciona la base estructural sobre la cual se construye una página web.

## Palabras Claves

- `index.html` es el archivo principal.
- `<p></p>` para párrafos.
- `<em></em>` para cursiva.
- `<mark></mark>` para resaltar.
- `<strong></strong>` para texto en negrita.
- `img` es la carpeta donde se deben guardar las imágenes.
- `<img src="img/banner.png" alt="Esto es para accesibilidad." width="200">` para insertar imágenes.
- `<a href="<https://google.com>" target="_blank">Buscar en Google</a>` es para enlazar a otra página web.
- `<br>`  es un salto de línea.
- `<div></div>` ocupa todo el ancho de la página.
- `<span></span>` es un contenedor in-line similar a div.
- `<main></main>` define el contenido principal de la página web.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi primera página con HTML</title>
</head>
<body>
    <main>
        <div>
            <h1>Bienvenido a mi página web</h1>
            <p><strong>Este</strong> es un párrafo de bienvenida. Espero que disfrutes navegando por mi sitio.</p>
            <p>Si quieres saber más sobre HTML, puedes <a href="<https://google.com>" target="_blank"><em>buscar en Google</em></a>.</p>


            <p>Aquí hay una imagen destacada:</p>
            <img src="img/banner.png" alt="Un hermoso paisaje" width="200">
        </div>
        <div>
            <p><mark>Aquí hay un texto resaltado</mark> para llamar la atención.</p>
            <span>Y esto es un texto dentro de un elemento span.</span>
        </div>
    </main>
</body>
</html>
```

# CSS (Cascading Style Sheets)

  

CSS es un lenguaje de estilo que se utiliza para:

- Dar estilo y diseño a los elementos HTML.
- Controlar aspectos visuales como colores, fuentes, márgenes, alineación, etc.
- Mejorar la presentación y la experiencia del usuario en la interfaz de usuario.

## Palabras Claves

Se pueden agregar estilos CSS de tres maneras diferentes:

7. Dentro de `<head></head>` con `<style></style>`.
8. Dentro de `<head></head>` con `<link rel="stylesheet" href="/assets/styles.css">`.
9. En un archivo externo .css enlazado con `<link>`.

## Ejemplo de uso de CSS

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi primera página con CSS</title>

    <!-- Método 1: Estilos internos -->
    <style>
        body {
            background-color: lightblue;
        }
        h1 {
            color: white;
            text-align: center;
        }
    </style>

    <!-- Método 2: Enlazar a un archivo CSS externo -->
    <link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
    <h1>Bienvenido a mi página web</h1>
    <p>Esta es una página con estilos CSS.</p>
</body>
</html>
```

```css
/* Ejemplo de un archivo CSS externo: /assets/styles.css */

body {
    font-family: Arial, sans-serif;
}

h1 {
    color: darkblue;
}
```

En este ejemplo, los estilos se aplican a los elementos `body` y `h1` utilizando el método interno. También se muestra cómo enlazar a un archivo CSS externo y se proporciona un ejemplo de cómo podría verse este archivo CSS externo.

# JavaScript

JavaScript es un lenguaje de programación utilizado para agregar interactividad y dinamismo a una página web. Permite realizar acciones como validar formularios, crear efectos visuales, manipular el contenido de la página en tiempo real, entre otros. Es fundamental para crear aplicaciones web modernas y mejorar la experiencia del usuario.

**Características de JavaScript:**

- JavaScript tiene un tipado dinámico, débil e implícito:
    - Dinámico: una variable puede cambiar de tipo de dato.
    - Débil: se pueden realizar operaciones con diferentes tipos de dato.
    - Implícito: infiere el tipo de dato de una variable.

**Inclusión de JavaScript en HTML:**

Se puede agregar JavaScript a HTML utilizando la etiqueta `<script></script>` dentro del cuerpo (`<body>`), preferiblemente al final.

**Funciones útiles en JavaScript:**

- `alert()`: muestra un mensaje en un cuadro emergente en el navegador.
- `prompt()`: solicita al usuario un input en un cuadro emergente.
- `confirm()`: muestra un cuadro emergente con opciones de confirmación (sí/no).
- `parseInt(n)`: convierte n a tipo de dato entero.

**Llamar a una función JavaScript desde un botón:**

Para llamar a una función JavaScript desde un botón se utiliza: `<button onclick="nombreDeLaFuncion()"></button>`.

**Manipulación de elementos HTML desde JavaScript:**

Al asignar un id a un elemento HTML, se crea una variable en JavaScript para acceder y modificar ese elemento.

**Ejemplo de código JavaScript:**

```html
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript en el HTML</h2>

<button type="button" onclick="myFunction()">Click me</button>

<p id="demo">This is a demonstration.</p>

<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Hello JavaScript!";
}
</script>

</body>
</html>

```

En este ejemplo, cuando se hace click en el botón, se llama a la función JavaScript `myFunction()`, la cual cambia el contenido del párrafo con id "demo".

En términos generales, HTML, CSS y JavaScript constituyen los tres pilares fundamentales en la creación de aplicaciones web interactivas y atractivas. HTML se encarga de establecer la estructura básica de la página web, proporcionando el esqueleto sobre el cual se construye todo lo demás. CSS, por otro lado, se utiliza para embellecer y personalizar estos elementos HTML, controlando aspectos visuales como colores, fuentes, márgenes y alineación. Por último, JavaScript inyecta vida a la página, permitiendo la creación de funcionalidades dinámicas e interactivas que mejoran significativamente la experiencia del usuario. En conjunto, estas tres tecnologías trabajan de manera sincronizada para ofrecer una experiencia de usuario completa y satisfactoria en cualquier aplicación web.

# Bootstrap

Bootstrap es un marco de diseño (framework) de código abierto que facilita la creación de sitios web y aplicaciones web receptivos y móviles. Bootstrap proporciona una serie de estilos CSS y componentes de interfaz de usuario, así como complementos de JavaScript.

## Características de Bootstrap

- **Responsive:** Bootstrap se adapta automáticamente a diferentes tamaños de pantalla y resoluciones.
- **Componentes predefinidos:** Bootstrap ofrece una amplia gama de componentes reutilizables para interfaz de usuario, como botones, menús desplegables, formularios, tarjetas, carruseles, etc.
- **Personalizable:** Puedes personalizar Bootstrap según tus necesidades, eligiendo solo los componentes que necesitas.

## Ejemplo de Uso de Bootstrap

A continuación, se muestra un ejemplo de cómo usar Bootstrap para crear una tarjeta con imagen y texto:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Bootstrap Ejemplo</title>
    <!-- Importar CSS de Bootstrap -->
    <link rel="stylesheet" href="<https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css>">
</head>
<body>
    <div class="container">
        <!-- Tarjeta de Bootstrap -->
        <div class="card" style="width: 18rem;">
            <img src="ruta_a_tu_imagen" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Título de la Tarjeta</h5>
                <p class="card-text">Algun texto de ejemplo para construir el cuerpo de la tarjeta.</p>
                <a href="#" class="btn btn-primary">Ir a alguna parte</a>
            </div>
        </div>
    </div>

    <!-- Importar JS de Bootstrap -->
    <script src="<https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js>"></script>
</body>
</html>

```

En este ejemplo, hemos importado la hoja de estilos de Bootstrap y el archivo JavaScript desde un CDN. Luego, hemos usado las clases de Bootstrap para crear una tarjeta con una imagen, un título, un texto y un botón.

## Extras

Aparte del diseño responsive y los componentes predefinidos, Bootstrap también ofrece:

- **Grilla:** Bootstrap incluye un sistema de grilla flexible y receptivo para estructurar el contenido.
- **Utilidades:** Bootstrap viene con una serie de utilidades de CSS para realizar tareas comunes de diseño, como ajustar los márgenes, añadir relleno, modificar las fuentes y los colores, etc.
- **Complementos de JavaScript:** Bootstrap también incluye varios complementos de JavaScript para añadir funcionalidades interactivas, como modales, tooltips, carruseles, etc.
- **Documentación detallada:** La página oficial de Bootstrap ofrece una documentación detallada y ejemplos de código para todos los componentes y funciones.

# Mini parcial

[https://forms.gle/cLE9Pfyhug7zLN147](https://forms.gle/cLE9Pfyhug7zLN147)

# CLASE EXTRA DE PYTHON

Python es un lenguaje de programación multiparadigma que soporta programación imperativa, orientada a objetos y funcional. Es de tipado fuerte y dinámico.

Beneficios de Python:

- Fácil lectura y comprensión debido a su sintaxis similar al inglés.
- Mayor productividad al requerir menos líneas de código.
- Gran biblioteca estándar con códigos reutilizables.
- Fácil integración con otros lenguajes de programación como Java, C y C++.
- Comunidad activa de millones de desarrolladores alrededor del mundo.
- Amplia disponibilidad de recursos de aprendizaje en línea.
- Portabilidad a través de diferentes sistemas operativos.

Usos comunes de Python:

- Desarrollo web del lado del servidor
- Automatización con scripts de Python
- Realización de tareas de ciencia de datos y machine learning
- Desarrollo de software
- Automatización de pruebas de software

Python es un lenguaje interpretado, fácil de utilizar, tipeado dinámicamente, de alto nivel y orientado a los objetos.

Existen bibliotecas de Python para diversas aplicaciones, incluyendo desarrollo web, ciencia de datos y machine learning (ML). Las más populares incluyen Matplotlib, Pandas, NumPy, Requests, OpenCV-Python y Keras.

Los marcos de Python (frameworks) son colecciones de paquetes y módulos que permiten a los desarrolladores crear aplicaciones de Python de manera más rápida y sencilla.

### Ejemplos para entender un poco mejor:

**Hola Mundo:**
El programa "Hola Mundo" es el más simple en cualquier lenguaje de programación. En Python, se ve así:

```python
print("¡Hola Mundo!")

```

**Variables y Operaciones Matemáticas:**
Python permite la definición de variables y la realización de operaciones matemáticas de manera muy sencilla.

```python
# Definición de variables
x = 3
y = 5

# Operaciones matemáticas
suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y

print("La suma de x e y es: ", suma)
print("La resta de x e y es: ", resta)
print("La multiplicación de x e y es: ", multiplicacion)
print("La división de x e y es: ", division)

```

**Estructuras de Control:**
Python también permite el uso de estructuras de control como los bucles "for" y "while", y las estructuras condicionales "if" / "else".

```python
# Bucle for
for i in range(5):
    print(i)

# Bucle while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Condicional if/else
x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5")

```

**Definición de Funciones:**
Python permite definir funciones para encapsular bloques de código que realizan una tarea específica.

```python
# Definición de una función
def saludo(nombre):
    print("¡Hola, " + nombre + "!")

# Llamada a la función
saludo("Juan")

```

Estos son solo algunos ejemplos básicos. Python es un lenguaje de programación muy versátil y poderoso, y hay mucho más que se puede hacer con él.

# BACKEND + FLASK

  


El backend, en términos generales, se refiere a la parte de una aplicación o sistema que está encargada de procesar y manejar los datos, la lógica de negocio y la comunicación con el servidor. Aquí, nos enfocaremos en comprender los protocolos de comunicación entre cliente y servidor, así como en el uso del framework Flask en Python para desarrollar aplicaciones web.

## Protocolos de comunicación

Los protocolos de comunicación se dividen en dos categorías: textuales y binarios. Los protocolos textuales, como HTTP (Hiper Text Transfer Protocol), son legibles por humanos y se utilizan comúnmente en la web para la transferencia de datos. Por otro lado, los protocolos binarios, como WebSocket, no son legibles por humanos pero suelen ser más rápidos.

HTTP es un protocolo basado en texto que sigue un modelo de solicitud-respuesta. Una solicitud HTTP consta de un objetivo (URL), un método (GET, POST, PUT, DELETE, etc.) y encabezados (headers), mientras que una respuesta HTTP incluye un código de estado, encabezados y un cuerpo (body) opcional.

Es importante destacar que HTTP es un protocolo sin estado (stateless), lo que significa que cada solicitud es independiente de las anteriores, pero no necesariamente sin sesión (sessionless). Esto implica que no hay una conexión continua entre el cliente y el servidor, lo que puede hacer que sea más eficiente en situaciones de alto tráfico. Sin embargo, HTTP también puede admitir conexiones continuas y streaming en la actualidad.

## Flask

Flask es un framework web ligero y flexible para Python que proporciona herramientas para desarrollar aplicaciones web de manera rápida y sencilla. Algunas de las características que ofrece Flask son:

- Manejo de conexiones.
- Sistema de plantillas web.
- Caché de datos.
- Seguridad.
- Acceso y configuración de bases de datos, entre otros.

Para comenzar a trabajar con Flask, primero necesitamos configurar nuestro entorno. A continuación se muestra cómo hacerlo:

- Instala virtualenv para crear entornos virtuales de Python:

```bash
pip install virtualenv

```

- Crea un nuevo entorno virtual llamado "venv":

```bash
virtualenv venv

```

- Activa el entorno virtual. Esto aislará tu entorno de desarrollo y evitará conflictos con otras dependencias de Python instaladas globalmente:

```bash
source venv/bin/activate

```

- Una vez que estés dentro del entorno virtual, puedes instalar Flask usando pip:

```bash
pip install Flask

```

Ahora estás listo para comenzar a desarrollar aplicaciones web con Flask en un entorno aislado y controlado. Aquí tienes un ejemplo básico de una aplicación Flask:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello world!</p>'

if __name__ == '__main__':
    app.run(port=8000)

```

En este ejemplo, definimos una ruta raíz ("/") que retorna un saludo simple "Hello world!" cuando se accede a través de un navegador web. Flask facilita la creación de aplicaciones web al proporcionar una estructura clara y flexible para el desarrollo.

### Tema de Backend que talvez entra ( dijo algo en la clase de repaso )

### ¿Qué Son los Códigos HTTP?

Un código HTTP es un número de tres dígitos que genera un servidor en respuesta a la petición de un navegador, indicando si la solicitud fue exitosa o si hubo un error. Por ejemplo, el código 404 indica que el servidor no pudo encontrar el recurso solicitado.

### Estructura de los Códigos HTTP

El primer dígito indica la categoría del código:

- **1xx**: Informativo
- **2xx**: Éxito
- **3xx**: Redirección
- **4xx**: Error del Cliente
- **5xx**: Error del Servidor
Los dos dígitos siguientes especifican detalles adicionales.
![[response-codes.png]]

### Categorías y Códigos HTTP Comunes

**1xx - Informativo**

- **100 Continue**: El servidor ha recibido los encabezados y el cliente puede proceder con el cuerpo de la solicitud.
- **101 Switching Protocols**: El servidor acepta cambiar a un protocolo diferente.
- **102 Processing**: El servidor está procesando la solicitud.
- **103 Early Hints**: Permite al cliente precargar recursos mientras se prepara la respuesta.

**2xx - Éxito**

- **200 OK**: La solicitud ha sido exitosa.
- **201 Created**: La solicitud ha resultado en la creación de un nuevo recurso.
- **202 Accepted**: La solicitud ha sido aceptada pero aún está en proceso.
- **204 No Content**: La solicitud ha sido exitosa, pero no hay contenido que enviar.

**3xx - Redirección**

- **300 Multiple Choices**: Hay varias opciones para el recurso solicitado.
- **301 Moved Permanently**: El recurso se ha movido permanentemente a una nueva URL.
- **302 Found**: El recurso se encuentra temporalmente en una ubicación diferente.
- **304 Not Modified**: El recurso no ha sido modificado desde la última solicitud.

**4xx - Error del Cliente**

- **400 Bad Request**: La solicitud no puede ser procesada debido a una sintaxis incorrecta.
- **401 Unauthorized**: La solicitud requiere autenticación.
- **403 Forbidden**: El servidor se niega a autorizar la solicitud.
- **404 Not Found**: El servidor no puede encontrar el recurso solicitado.

**5xx - Error del Servidor**

- **500 Internal Server Error**: El servidor encontró un error inesperado.
- **501 Not Implemented**: El servidor no soporta la funcionalidad requerida.
- **502 Bad Gateway**: El servidor recibió una respuesta inválida del servidor upstream.
- **503 Service Unavailable**: El servidor no está disponible temporalmente, generalmente debido a mantenimiento o sobrecarga.

# PARCIAL COMPLETO

# ADICIONAL