---
base: "[[Introduccion al Desarrollo de Software.base]]"
cover: "[[Resumen CSS.jpeg]]"
Fecha: 2025-05-28T22:58:00
Descripción: ""
Diapos: []
---
# Introducción a CSS (Cascading Style Sheet)

CSS se encarga de la parte de apariencia y funcionamiento de una página web. Con CSS, podemos controlar el color del texto, el estilo de las fuentes, el espaciado entre párrafos, el tamaño y la disposición de las columnas, las imágenes o colores de fondo que se utilizan, así como una variedad de otros efectos.

## Ventajas de CSS

- **CSS ahorra tiempo**: Podes escribir CSS una vez y reutilizar la misma pagina en varias páginas HTML. Podes definir un estilo para cada elemento HTML y aplicarlo a tantas páginas web como quieras.
- **Fácil mantenimiento**: Para realizar un cambio global, simplemente cambie el estilo y todos los elementos en todas las páginas web se actualizarán automáticamente.
- **Estilos superiores a HTML**: CSS tiene una gama mucho más amplia de atributos que HTML, por lo que puede darle una apariencia mucho mejor a su página HTML en comparación con los atributos HTML.

## ¿Cómo lo incluimos en nuestro HTML?

Existen tres formas principales de incluir CSS en un documento HTML:

1. **Estilo en línea:** Se aplica directamente a un elemento HTML mediante el atributo style. Este método es útil para aplicar estilos específicos a un solo elemento.
```html
<h1 style="color: blue; text-align: center;">¡Hola!</h1>

```
2. **Estilo interno**: Se define dentro de la etiqueta `<head>` del documento HTML utilizando la etiqueta `<style>`. Este método es ideal para aplicar estilos a múltiples elementos en una única página.
```html
<head>
    <style>
        body {
            background-color: #f0f0f0;
        }
        p {
            font-family: Arial, sans-serif;
            color: #333;
        }
    </style>
</head>

```
3. **Estilo externo**: Se utiliza un archivo CSS separado que se enlaza al documento HTML mediante la etiqueta `<link>` en el `<head>`. Esta es la forma más recomendada, ya que permite una gestión centralizada de los estilos.
```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

# Sintaxis

- **Selector**: Un selector es una etiqueta HTML a la que se aplicará un estilo. Puede ser cualquier etiqueta, como `<h1>` o `<table>`, etc.
- **Propiedad**: Una propiedad es un tipo de atributo de una etiqueta HTML. En pocas palabras, todos los atributos HTML se convierten en propiedades CSS. Pueden ser; color,border, etc.
- **Valor**: Se asignan valores a las propiedades. Por ejemplo, la propiedad de color, puede tener "red" o #01010Por ejemplo, definir el borde de una tabla se puede realizar con:Aca la tabla es un selector y el borde una propiedad, y el valor seria 1px solid red. Se pueden definir selectores en varias maneras, depende de cada uno. Vamos a explicar estos selectores uno por uno.
```css
selector { propiedad: valor }

```
```css
table{
border : 1px solid red;
}

```

## Selectores

- **Selectores de tipo**: Es como el selector del ejemplo, una vez más le daremos color a todos los headings de nivel 1 (h1).
```css
h1 {
color: red;
}

```
- **Selectores universales**: En lugar de seleccionar elementos de un tipo específico, el selector universal simplemente coincide con el nombre de cualquier tipo de elemento.
```css
* {
color: #000000;
}

```
- **Selectores de descendiente**: Aplica estilos a elementos dentro de un contenedor específico. Esto aplicará el color azul a todos los párrafos (`<p>`) que estén dentro de un contenedor `<div>`.
```css
div p{
    color: blue;
}

```
- **Selectores de ID**: Puede definir reglas de estilo basadas en atributos de ID de los elementos. Todos los elementos que tienen esa ID se formatean según la regla definida.
```css
#black {
    color: #000000;
}

```
- **Múltiples estilos**: Es posible que se necesite definir varias reglas de estilo para un solo elemento. Se pueden definir estas reglas para combinar varias propiedades y valores correspondientes en un solo bloque, como en el siguiente ejemplo:
```css
h1 {
    color: #36C;
    font-weight: normal;
    margin-bottom: 1em;
}

```
- **Agrupar selectores**: Se puede aplicar un estilo a varios selectores, para eso hay que separarlos con una coma.
```css
h1, h2, h3 {
    color: orange;
    font-weight: normal;
} /*( El estilo se aplicará a los elementos h1,h2,h3 .)*/

```
- **Selectores de pseudo-clases**: Se utilizan para aplicar estilos a un estado específico de un elemento, como `:hover` o `:first-child`. Este estilo subrayará los enlaces `<a>` al pasar el cursor por encima.
```css
a:hover {
    text-decoration: underline;
}

```

## Diseño y disposición en CSS

Además de los selectores y las propiedades básicas, CSS te permite crear diseños complejos y organizados para tus páginas web. Existen diferentes técnicas y métodos para organizar el contenido en columnas, filas y secciones. A continuación, explicaremos algunas de las más importantes:

### 1. **Modelo de caja (Box model)**

![[kPV82Sm.png]]

En CSS, cada elemento se representa como una caja rectangular que está compuesta por las siguientes partes:

### 2. **Diseño de cuadrícula (Grid layout)**

El modelo de diseño de cuadrícula (grid layout) proporciona un sistema bidimensional para organizar elementos. Es ideal para dividir el espacio en filas y columnas, con un control preciso de cada área.

### 3. **Flexbox**

Flexbox, o Flexible Box Layout, es un modelo de diseño en CSS que permite organizar elementos en una interfaz de manera flexible y eficiente. El primer paso para utilizar Flexbox es declarar un contenedor flex. Para hacerlo, debes establecer la propiedad display como flex o inline-flex en un elemento contenedor.

```css
.contenedor {
    display: flex;
}
```

**Elementos Flex (Flex Items)**

Los elementos directos dentro del contenedor flex son llamados elementos flex. Flexbox les permite alinearse y distribuirse de diversas maneras.

**Propiedades del contenedor flex**

**Propiedades de los elementos flex**

### 4. Posicionamiento

CSS te permite posicionar elementos con precisión en la página usando diferentes valores de la propiedad position:

- `static`: Posicionamiento predeterminado, sin cambios.
- `relative`: Se posiciona de manera relativa a su posición normal.
- `absolute`: Se posiciona en relación a su contenedor más cercano con position diferente a static.
- `fixed`: Se posiciona en relación a la ventana del navegador y no se mueve al hacer scroll.
- `sticky`: Combina características de relative y fixed. El elemento se mantiene en su lugar cuando se alcanza un punto de desplazamiento.

```css
.relativo {
    position: relative;
    top: 10px;
    left: 20px;
}

```

### 5. Pseudo-clases y pseudo-elementos

Las pseudo-clases y pseudo-elementos permiten aplicar estilos a estados o partes específicas de los elementos. Un ejemplo de **pseudo-clase** podría ser `:hover`, que aplica un estilo cuando el cursor pasa sobre el elemento.

```css
a:hover {
    color:red;
}

```

Ejemplos claros de **pseudo-elementos** serían `::before` y `::after`, que permiten insertar contenido antes o después de un elemento.

```css
p::before {
    color: red;
}

```

# Propiedades de estilo avanzadas de CSS

## Transiciones y animaciones

Las transiciones y animaciones hacen que los cambios en las propiedades de CSS sean más suaves y dinámicos, mejorando la experiencia del usuario.

### Transiciones

Las transiciones permiten que los valores de una propiedad cambien gradualmente a lo largo de un período de tiempo. Se pueden aplicar a propiedades como `color`, `background-color`, `width`, y más.

```css
.elemento{
    transition: propiedad duración;
}

```

Por ejemplo:

```css
.boton{
    background-color: blue;
    transition: background-color 0.5s ease;
}

.boton:hover {
    background-color: green;
}

```

## Animaciones

Las animaciones permiten cambios más complejos y definidos a través de múltiples estados utilizando @keyframes. Se pueden animar múltiples propiedades y definir diferentes etapas de la animación.

```css
@keyframes nombre_animacion {
    from {
        propiedad: valor_inicial;
    }
    to {
        propiedad: valor_final;
    }
}

.elemento {
    animation: nombre_animacion duración tipo_de_repetición;
}

```

## Transformaciones

Las transformaciones permiten manipular la posición, tamaño y rotación de los elementos utilizando las propiedades `transform` y `transform-origin`.

### **Propiedades de transformación**:

- **translate(x, y)**: Mueve un elemento a lo largo de los ejes X e Y.
- **scale(x, y)**: Escala un elemento (puede ser de forma uniforme o desigual).
- **rotate(deg)**: Rota un elemento en un número específico de grados.
- **skew(x, y)**: Inclina un elemento a lo largo de los ejes X e Y.