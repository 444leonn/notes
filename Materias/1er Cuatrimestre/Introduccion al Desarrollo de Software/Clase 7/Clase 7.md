---
base: "[[Introduccion al Desarrollo de Software.base]]"
Clase Grabada: https://youtu.be/Jcw5Kh77KRc?si=7eisbot8lb-8bUzO
Fecha: 2025-05-28T22:58:00
Descripción: HTML, CSS, Consigna TP2
Diapos:
  - 2243f454-0dd6-807c-867f-ef5f55fb43e3
---

# HTML

## **¿**Que es HTML? **¿**Para que se usa?

HTML *(HyperText Markup Language) *es un **lenguaje de marcado **que define la estructura del contenido de una página Web. Este lenguaje consiste en una serie de elementos que usarás para encerrar diferentes partes del contenido para que se vean o comporten de una determinada manera.

<u>**Importante:**</u>** HTML no es un lenguaje de programación**. Es un lenguaje de marcado. Sirve para indicar una estructura de elementos, no para crear algoritmos.

## Estructura Basica de HTML

```html
<!DOCTYPE html> # Declaración de tipo de documento HTML
<html> # Inicio documento HTML
<head>
    <title>Mi página web</title> # Cabecera de la pagina
</head>
<body>
    <h1>Hola mundo!</h1> # Cuerpo o contenido de la página
</body>
</html> # Fin documento HTML

```

## Etiquetas

![[h1.png]]

### Etiquetas Basicas

- **<html>, <head>, <body> **para la estructura básica de la página Web
- **<h1>, <h2>, …, <h6> **para títulos dentro del contenido
- **<div> **para dividir el contenido en partes con significado distinto
- **<p> **para párrafos
- **<img> **para añadir imágenes al documento
- **<a> **para enlaces
- **<br> **para realizar saltos de línea
- **<span> **para estilizar una parte del texto
- **<form>, <input>, <button>, <label> **para formularios

## Atributos

Los atributos permiten modificar **propiedades de un elemento** HTML. Siempre se escriben dentro de la etiqueta de apertura.

`**<a href=”**`[`**http://google.com/**`](http://google.com/)`**”>Ir a Google </a>**`**  href: **atributo o propiedad, el link es el valor.

*Ejemplo:*

![[machete-input-html.jpeg]]

# CSS

## **¿**Que es CSS? **¿**Para que se usa?

CSS *(Cascading Style Sheets) *u *Hojas de estilo en cascada *es un **lenguaje de hojas de estilo**, es decir, te permite aplicar estilos de manera selectiva a elementos en documentos HTML.

I<u>**mportante:**</u> **CSS no es un lenguaje de programación. Tampoco de marcado.** Es un lenguaje de hojas de estilo. Sirve para dar estilo a elementos que ya fueron previamente indicados y ubicados en una estructura. Otros ejemplos de lenguajes de estilo son XSL y Sass.

## **Estructura básica de CSS**

![[css.png]]

## Selectores

Los selectores nos indican con base en qué criterio CSS selecciona qué elementos de nuestra página va a tomar para aplicarle un conjunto de atributos. En otras palabras: **¿a qué cosas le cambio el estilo?**

Tipos de selectores:

## Atributos

Los atributos CSS se refieren a la **característica visible o estructural** que queremos modificar de un elemento. Por ejemplo: el color del texto o la forma de mostrar un botón con respecto al resto de la página.

Algunos atributos básicos son:

*Ejemplo basico de CSS:*

## **Insertando CSS a una página Web**

Existen 3 formas de insertar código CSS a una página Web:

- **Inline: **inserto el estilo directamente como atributo del elemento HTML.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi página Web</title>
    <style>
        h1 {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Hola mundo!</h1>
</body>
</html>
```
- **Dentro del HTML: **etiqueta **<style>** dentro de la cabecera del documento
`<h1 style="color: red;">Hola mundo!</h1>`
- **Desde un archivo CSS: **lo enlazamos dentro de la cabecera del documento HTML.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi página Web</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hola mundo!</h1>
</body>
</html>
```

# Ejemplo con Flask

![[ejemplo-flask.png]]

# Ejercitacion

Tomar el ejemplo de esta PPT de “Pala Store” y agregarle imágenes a los productos. Las imágenes tienen que tener un tamaño de 150 píxeles x 150 píxeles.

Mostrar la página usando Flask.

Pueden usar tanto el HTML como el CSS de ejemplo.

# **Ejercicio Práctico N° 2: Front**

[[Consigna]]
