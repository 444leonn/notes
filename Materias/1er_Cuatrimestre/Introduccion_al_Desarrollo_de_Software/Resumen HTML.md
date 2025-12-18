---
base: "[[Introduccion al Desarrollo de Software.base]]"
cover: "[[Resumen HTML.jpeg]]"
Fecha: 2025-05-28T22:58:00
Descripción: Declaracion Tipo, Cabecera <head>, Cuerpo <body>, mas elementos.
Diapos: []
---
Las etiquetas individuales y las de apertura pueden incluir <u>***atributos***</u> para ofrecer información adicional acerca de sus contenidos (por ejemplo, <html lang="es">). Las etiquetas individuales y la combinación de etiquetas de apertura y cierre se llaman elementos. Los elementos compuestos por una sola etiqueta se usan para modificar el contenido que los rodea o incluir recursos externos, mientras que los elementos que incluyen etiquetas de apertura y cierre se utilizan para delimitar el contenido del documento

# Declarando el Tipo de Documento

Lo primero que se debe de hacer a la hora de crear un documento HTML es especificar su tipo, ya que con esto evitamos posibles confusiones o emisiones de lectura por parte de nuestro navegador, para hacerlo debemos de escribir una primer linea en todo documento HTML.

---

`<!DOCTYPE html>` 

---

# Elementos Estructurales

En los documentos HTML existen distintos tipos de elementos que permiten la escritura del codigo, algunos estan encargados de definir secciones generales del documento y otros definen secciones menores o contenido.

Los elementos que se encargan de definir estas secciones generales, algo asi como la* “vertebra” *de nuestro documento son:

Es luego de que declaramos el tipo de documento con `<!DOCTYPE html>` que declaramos estos elementos estructurales

## Cabecera <head> </head>

La estructura basica ya esta lista. Ahora tenemos que construir la pagina, comenzado por la cabece `<head> </head>` . La cabecera incluye todos los recursos e informacio necesarios para generar la pagina. Los siguientes son los elementos disponibles para e<ste proposito.

# Otros elementos importantes de HTML

### **Enlaces** (`<a>`)

Los **anchors** (enlaces) son utilizados para crear hipervínculos que permiten navegar entre páginas o redirigir a secciones específicas dentro de la misma página. El atributo href define el destino del enlace.

```html
<a href="https://intro-camejo.github.io/web/">¡Visita nuestra página!</a>
```

### **Listas** (`<ul>`, `<ol>`, `<li>`)

HTML permite organizar información en listas. Existen dos tipos de listas:

- Listas no ordenadas (`<ul>`), que usan viñetas:
```html
<ul>
<li>Elemento 1</li>
<li>Elemento 2</li>
<li>Elemento 3</li>
</ul>
```
- Listas ordenadas (`<ol>`), que se numeran automáticamente:
```html
<ol>
<li>Primero</li>
<li>Segundo</li>
<li>Tercero</li>
</ol>
```

### **Imágenes** (`<img>`)

Las imágenes en HTML se insertan mediante la etiqueta `<img>`, donde el atributo `src` indica la ruta de la imagen y alt proporciona un texto alternativo en caso de que la imagen no se pueda cargar.

### **Tablas** (`<table>`)

Para mostrar datos en formato de tabla, se utiliza la etiqueta `<table>`, que contiene filas (`<tr>`) y columnas definidas por celdas (`<td>`).

### **Formularios** (`<form>`)

Los formularios permiten a los usuarios interactuar con una página web, proporcionando información o enviando datos.

**Atributos Útiles en Formularios**

- **Placeholders**: El atributo placeholder permite mostrar un texto de ayuda dentro de un campo de entrada. Este texto desaparece cuando el usuario comienza a escribir en el campo. Es útil para indicar el tipo de información que se espera.
```html
<input type="text" id="nombre" name="nombre" placeholder="Ingresa tu nombre">
```
- **required**: Este atributo asegura que un campo de entrada debe ser completado antes de enviar el formulario. Si el usuario intenta enviar el formulario sin completar este campo, se mostrará un mensaje de advertencia.
```html
<input type="email" id="email" name="email" required placeholder="Ingresa tu correo electrónico">
```
- **maxlength**: Limita la cantidad de caracteres que un usuario puede ingresar en un campo de texto.
```html
<input type="text" id="nombre" name="nombre" maxlength="30" placeholder="Máximo 30 caracteres">
```
- **pattern**: Permite establecer una expresión regular que los datos ingresados deben cumplir, útil para validar formatos específicos.
```html
<input type="text" id="telefono" name="telefono" pattern="\d{3}-\d{3}-\d{4}" placeholder="Formato: 123-456-7890">
```

## Elementos de navegación y estructura

### **Navegación** (`<nav>`)

 El elemento `<nav>` se utiliza para definir un bloque de navegación que contiene enlaces a otras páginas o secciones.

```html
<nav>
<ul>
    <li><a href="#inicio">Inicio</a></li>
    <li><a href="#servicios">Servicios</a></li>
    <li><a href="#contacto">Contacto</a></li>
</ul>
</nav>
```

### Pie de página (`<footer>`)

El elemento `<footer>` representa la parte inferior de una página web, donde se incluye información como derechos de autor o enlaces a políticas de privacidad.

```html
<footer>
<p>Todos los derechos reservados.</p>
</footer>
```

## Uso de `<div>` y organización de secciones

### **Divisiones** (`<div>`)

El elemento `<div>` es uno de los elementos más comunes en HTML y se utiliza para agrupar contenido. Sirve como un contenedor genérico que no aporta significado semántico por sí solo, pero permite organizar y aplicar estilos o comportamientos a secciones específicas de la página.

```html
<div>
  <h2>Sección de noticias</h2>
  <p>Últimas noticias sobre Introducción al Desarrollo de Software.</p>
</div>

```

Los `<div>` permiten dividir la página en bloques independientes y son muy útiles cuando se trabaja con CSS o JavaScript para aplicar estilos y acciones a secciones completas.

## `class` e `id`: Identificadores y clases en HTML

Para aplicar estilos personalizados con CSS o manipular elementos con JavaScript, HTML ofrece los atributos `class` e `id`:

### `class` 

Permite aplicar un nombre de clase a varios elementos para agruparlos y poder estilizar o manipular de forma conjunta. Un mismo elemento puede tener múltiples clases.Acá, ambos elementos `<div> y <p>` pueden compartir el estilo de la clase "contenedor" y "texto-destacado" definido en el archivo CSS.

### `id`

Es un identificador único que se asigna a un solo elemento de la página. Permite distinguir ese elemento específico para aplicar un estilo o una acción particular.En este caso, tanto el `id="principal"` como el `id="intro"` identifican elementos únicos dentro de la página, útiles cuando se necesitan realizar manipulaciones precisas mediante JavaScript o cuando se aplican estilos exclusivos.

# Links de Interes

[https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)
