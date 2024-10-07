
- [CSS](#css)
  - [¿Qué es CSS?](#qué-es-css)
  - [Formas de incluir CSS](#formas-de-incluir-css)
  - [Selectores en CSS](#selectores-en-css)
  - [Propiedades y valores comunes en CSS](#propiedades-y-valores-comunes-en-css)
- [Identificadores y Clases en CSS](#identificadores-y-clases-en-css)
  - [1. ¿Qué es un Identificador 1(ID)?](#1-qué-es-un-identificador-1id)
  - [2. ¿Qué es una Clase (class)?](#2-qué-es-una-clase-class)
  - [3. Diferencias clave entre ID y Clase:](#3-diferencias-clave-entre-id-y-clase)
  - [4. Uso de ID y Clases combinados](#4-uso-de-id-y-clases-combinados)
  - [5. ¿Cuándo usar ID y cuándo clases?](#5-cuándo-usar-id-y-cuándo-clases)

# CSS

CSS (**Cascading Style Sheets**) es el lenguaje que usamos para describir la presentación de un documento HTML. Controla cómo se muestran los elementos en una página web.

## ¿Qué es CSS?

CSS permite aplicar estilos a los elementos de una página HTML. Estos estilos incluyen colores, tamaños de texto, disposición de los elementos, y mucho más. CSS está formado por:

- **Selectores**: Definen qué elementos HTML se estilizarán.
- **Propiedades**: Definen qué aspecto de los elementos se está cambiando (ej. `color`, `font-size`, etc.).
- **Valores**: Son los valores aplicados a las propiedades (ej. `red`, `16px`, etc.).

## Formas de incluir CSS

### 1. **CSS en línea** (Inline CSS)

Se utiliza directamente dentro del atributo `style` de un elemento HTML. Se recomienda evitarlo para no mezclar estructura y diseño.

```html
<p style="color: blue; font-size: 18px;">Este es un párrafo estilizado en línea.</p>
```

### 2. CSS en la cabecera

Se coloca dentro de la etiqueta ``<style>`` en el encabezado ``<head>`` del documento HTML. Esto permite tener todos los estilos en un solo lugar.

```html
<head>
  <style>
    p {
      color: red;
      font-size: 16px;
    }
  </style>
</head>
```

### 3. CSS en archivo externo

Es la mejor práctica para proyectos más grandes. Colocas el CSS en un archivo separado con extensión .css y lo enlazas a tu documento HTML usando la etiqueta ``<link>`` en el ``<head>``.

```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

Y en el archivo ``styles.css``, este deberá contener la información de los estilos que queramos definir:

```css
p {
  color: green;
  font-size: 14px;
}
```

## Selectores en CSS

Los selectores especifican qué elementos HTML serán afectados por las reglas CSS. Aquí algunos de los más comunes:

### Selector de tipo

Selecciona todos los elementos de un tipo específico (como p, h1, div).

```css
p {
  color: blue;
}
```

### 2. Selector de clase

Selecciona elementos que tienen un atributo class. Se utiliza un punto (.) antes del nombre de la clase.

```css
.texto-azul {
  color: blue;
}
```

Y en HTML:

```html
<p class="texto-azul">Este texto es azul.</p>
```

### 3. Selector de ID

Selecciona un elemento que tenga un atributo id. Se utiliza una almohadilla (#) antes del nombre del ID.

```css
#titulo-principal {
  color: red;
  font-size: 24px;
}
```

Y en HTML:

```html
<h1 id="titulo-principal">Este es el título principal</h1>
```

### 4. Selector universal

Selecciona todos los elementos de la página.

```css
* {
  margin: 0;
  padding: 0;
}
```

## Propiedades y valores comunes en CSS

### 1. Propiedades de texto

color: Cambia el color del texto.

```css
p {
  color: blue;
}
```

font-size: Cambia el tamaño del texto.

```css
h1 {
  font-size: 36px;
}
```

text-align: Alinea el texto (puede ser left, center, right, o justify).

```css
p {
  text-align: center;
}
```

font-family: Cambia la fuente del texto.

```css
body {
  font-family: Arial, sans-serif;
}
```

### 2. Propiedades de fondo

background-color: Cambia el color de fondo de un elemento.

```css
body {
  background-color: lightgrey;
}
```

background-image: Aplica una imagen de fondo.

```css
div {
  background-image: url('imagen.jpg');
}
```

### 3. Propiedades de caja (Box Model)

margin: Establece el espacio externo de un elemento.

```css
div {
  margin: 20px;
}
```

padding: Establece el espacio interno entre el contenido y el borde.

```css
div {
  padding: 15px;
}
```

border: Define el borde de un elemento.

```css
p {
  border: 1px solid black;
}
```

### Modelo de caja (Box Model)

El modelo de caja en CSS describe cómo se estructura el espacio de los elementos en la página. Consiste en:

- Contenido: El área donde se muestra el contenido (texto, imágenes, etc.).
- ``Padding``: El espacio entre el contenido y el borde.
- Borde (``Border``): El borde alrededor del padding.
- Margen (``Margin``): El espacio fuera del borde, separando un elemento de otros.

```css
div {
  width: 300px;
  padding: 10px;
  border: 5px solid black;
  margin: 20px;
}
```

# Identificadores y Clases en CSS

## 1. ¿Qué es un Identificador 1(ID)?

- Un identificador (ID) es un nombre único que se asigna a un solo elemento HTML para estilizarlo de manera exclusiva.
- Se define en HTML con el atributo id, y en CSS, se selecciona utilizando el símbolo #.

Ejemplo en HTML:
<div id="header">Encabezado</div>

Ejemplo en CSS:
#header {
  background-color: blue;
  color: white;
}

Reglas:
- Cada ID debe ser único en toda la página.
- Se utiliza para aplicar estilos específicos a un solo elemento.

## 2. ¿Qué es una Clase (class)?

- Una clase es un grupo de estilos que puede aplicarse a múltiples elementos en una página.
- Se define en HTML con el atributo class, y en CSS, se selecciona usando el símbolo .

Ejemplo en HTML:
<div class="box">Caja 1</div>
<div class="box">Caja 2</div>

Ejemplo en CSS:
```css
.box {
  background-color: lightgray;
  padding: 20px;
}
```

Reglas:
- Se puede usar la misma clase en múltiples elementos.
- Útil cuando varios elementos necesitan los mismos estilos.

## 3. Diferencias clave entre ID y Clase:

| Característica  | ID                      | Clase                                           |
| --------------- | ----------------------- | ----------------------------------------------- |
| Símbolo en CSS  | #nombreID               | .nombreClase                                    |
| Unicidad        | Un solo elemento por ID | Varios elementos pueden compartir una clase     |
| Uso recomendado | Estilos únicos          | Agrupar elementos que comparten el mismo estilo |

## 4. Uso de ID y Clases combinados

A veces es útil combinar ID y clases para lograr un estilo más específico.

Ejemplo en HTML:
<div id="main" class="container">Contenido principal</div>

Ejemplo en CSS:

```css
#main {
  font-size: 20px;
}

.container {
  padding: 15px;
  background-color: #f0f0f0;
}
```

En este caso, el div tiene un ID único para aplicar estilos exclusivos, pero también usa la clase container para compartir estilos con otros elementos.

## 5. ¿Cuándo usar ID y cuándo clases?

- Usa IDs cuando necesites identificar un único elemento.
- Usa clases cuando quieras aplicar el mismo estilo a varios elementos.
- En general, se recomienda preferir el uso de clases, ya que es más flexible y evita conflictos.
