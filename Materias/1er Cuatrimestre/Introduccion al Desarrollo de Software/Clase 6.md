---
base: "[[Introduccion al Desarrollo de Software.base]]"
cover: "[[banner-flask.webp]]"
Clase Grabada: https://youtu.be/zr0Vo2Qnj0c?si=OocXReAFApxa7bTx
Fecha: 2025-05-28T22:58:00
Descripción: "Entorno Virtual (con PIPENV),  TEMPLATES: Variables, Iteraciones, Condicionales, LINKS con url_for."
Diapos:
  - 2243f454-0dd6-80cc-81a4-df23dd347ee9
---
# Flask

- Flask es un framework minimalista web muy popular que deja casi todas las decisiones de diseño y arquitectura en manos del desarrollador.
- Para trabajar con distintos proyectos es necesario crear un ambiente virtual (virtual environment), esto permitirá que no hayan incompatibilidades entre diferentes versiones de dependencias instaladas entre un proyecto y otro.
- pipenv: [https://docs.python-guide.org/dev/virtualenvs/](https://docs.python-guide.org/dev/virtualenvs/)

## Creando un Proyecto en Flask

1. Crear un directorio donde usaremos el proyecto: `**mkdir mi_proyecto**`
2. Acceder al directorio: `**cd mi_proyecto**`
3. Ingresar a Visual Studio Code: `**code .**`**(crear el archivo app.py y un directorio .venv)**
4. Crear el ambiente virtual: `**pipenv install flask**`
5. Activamos el proyecto: `**pipenv shell**`
6. Continuamos configurando el proyecto dentro del archivo [app.py](http://app.py/): `**from Flask import Flask**`
7. Una vez dentro del entorno, podemos utilizar comandos de pip y flask normalmente, como por ejemplo:
    - **pip list**
    - **pip install Flask**
    - **pip –version**
    - **flask run**
8. Para salir del entorno virtual utilizamos: `**exit**`

***El comando ***`***pipenv install***`*** nos va a crear todos los subdirectorios en la carpeta .venv si la tenemos creada.***

***Si le agregamos al comando el parametro flask nos va a instalar en el entorno virtual flask. ***`***pipenv install flask***`*** .***

## **Arrancando el Proyecto**

Ejemplo de nuestro archivo **app.py**:

Para ejecutar la app de Flask hay 3 formas:

![[image 57.png]]

## Estructura Básica de un Proyecto (Sin Blueprints)

**/mi_proyecto**

**/.venv**

**/templates**

**...**

**Jinja** nos permite agregar funcionalidad a estos /t**emplates**, haciendo que puedan integrar data desde el template dinámicamente.

## **Templates :: Variables y estructuras**

Dentro de un template, además de tener código HTML, también podremos incorporar en forma dinámica **variables y estructuras** del tipo if o for, entre muchas cosas más.

- **Variables**

Se incorporarán en forma dinámica su valor cuando las llamemos

**{{ nombre_variable }}**

[https://runebook.dev/es/docs/jinja/templates/index?utm_source=chatgpt.com](https://runebook.dev/es/docs/jinja/templates/index?utm_source=chatgpt.com)

### Variables dentro de los Templates

- Los templates pueden soportar muchos tipos de variables, por ejemplo:
    - **Diccionarios.**
    - **Listas.**
    - **Cadenas.**
    - **Objetos.**
    - **Enteros.**

```html
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
```

### **Estructuras IF dentro de los Templates**

- Como dijimos también pueden existir estructuras del tipo condicionales If
Las mismas de deberán estar entre {% ….  %}

### Estructuras FOR dentro de los Templates

- También se podrían utilizar for para hacer iterar una lista o diccionario de datos.
Las mismas de deberán estar entre {% ….  %}
```html
<ul>
		{% for comment in comments %}
				<li>{{ comment }}</li>
		{% endfor %}
</ul>
```

### **LINKS dentro de los Templates**

- Los links dentro de los templates se recomienda que se use el método **url_for()**, de esta forma evitaremos posibles problemas o roturas de nuestro código.
- Los links pueden ser estáticos o dinámicos.
Ejemplos:
`**url_for('static', filename="templates/home.html") **`** ⇒  **[**http://localhost:5000/**](http://localhost:5000/)
`**url_for('user', name='john', _external=True)**`** ⇒ **[**http://localhost:5000/user/john**](http://localhost:5000/user/john)
(la opción _external=True, hace que se escriba la dirección absoluta)

Ejemplo del uso de la opción **_external=True** para utilizar un host externo

Para usar hosts externos hay que setear la variable de entorno **SERVER_NAME**. En nuestro caso no es necesario.

## **Pongamos en Marcha el Proyecto**

Crearemos un pequeño sitio web y veremos:

## Ejercitacion

### Ejercicio 1

Crear un **primer proyecto** en Flask.

Escribir en el navegador “Hola Mundo”

### Ejercicio 2

Continuar con este mismo proyecto, y en la vista donde escribieron hola mundo, incorporar debajo un link que lleve a una nueva vista llamada howiam.html que tenga un texto con una breve reseña del alumno.

## Documentacion de Flask y Jinja

<!-- Column 1 -->
[https://flask.palletsprojects.com/en/stable/quickstart/](https://flask.palletsprojects.com/en/stable/quickstart/)

<!-- Column 2 -->
[https://jinja.palletsprojects.com/en/stable/templates/](https://jinja.palletsprojects.com/en/stable/templates/)

<!-- Column 3 -->

