# Estilos CSS

En HTML, el atributo **style** es una forma de especificar los estilos de un elemento utilizando la notación de CSS (Hoja de Estilos en Cascada). Este atributo es uno de los atributos más importantes de HTML y se utiliza para aplicar diferentes estilos a los elementos HTML.

## Sintaxis

La sintaxis para el atributo style es la siguiente:

```html
<elemento style ="propiedad: valor; propiedad: valor; ...">
```

En esta sintaxis, el elemento representa el elemento HTML al que se le aplicarán los estilos especificados.

## Ejemplos

A continuación se presentan algunos ejemplos de uso del atributo style en HTML.

### Cambiar el Color de Fondo de un Elemento

Para cambiar el color de fondo de un elemento, puede usar el atributo style con la propiedad de fondo. Por ejemplo, para cambiar el color de fondo de un elemento a azul, se puede usar el siguiente código:

```html
<p style="background-color: blue;">Texto aquí</p>
```

### Cambiar el Color de Letra de un Elemento

Para cambiar el color de letra de un elemento, puede usar el atributo style con la propiedad de color. Por ejemplo, para cambiar el color de letra de un elemento p a rojo, se puede usar el siguiente código:

```html
<p style="color: red;">Texto aquí</p>
```

### Cambiar el Tamaño de Letra de un Elemento

Para cambiar el tamaño de letra de un elemento, puede usar el atributo style con la propiedad font-size. Por ejemplo, para cambiar el tamaño de letra de un elemento h1 a 20px, se puede usar el siguiente código:

```html
<h1 style="font-size: 20px;">Texto aquí</h1>
```

### Alinear un Elemento a la Derecha

Para alinear un elemento a la derecha, puede usar el atributo style con la propiedad text-align. Por ejemplo, para alinear un elemento p a la derecha, se puede usar el siguiente código:

```html
<p style="text-align: right;">Texto aquí</p>
```

## Color de fondo

La propiedad CSS background-color define el color de fondo de un elemento HTML.
Podemos aplicarlo a todo el documento:

Podemos aplicarlo a un elemento concreto

## Color de texto

La propiedad CSS color define el color del texto de un elemento HTML:

1.2	Tipo de letra y tamaño
La propiedad CSS font-family define la fuente que se utilizará para un elemento HTML:

La propiedad CSS font-size define el tamaño del texto de un elemento HTML:

Con font-weight podemos definir el grosor de la letra

## Alineación

1. Centrar texto
La propiedad CSS text-align define la alineación horizontal del texto para un elemento HTML:

2. Centrar una imagen
Para centrar una imagen hacen falta estas 3 propiedades:

1.4	Color de borde
Puedes establecer el color de los bordes:

En lugar de solid, puedes escribir dotted o dashed, por ejemplo
1.5	Colores específicos
Los colores, también se pueden especificar según varios sistemas:

En la siguiente página, puedes averiguar el código de un color concreto: https://www.w3schools.com/html/html_colors_hex.asp

## Margin y padding

Los atributos **margin** y **padding** del atributo **style** en HTML son propiedades de la hoja de estilos (CSS) que le permiten controlar el espacio que se muestra alrededor de los elementos de la página web. Estas propiedades pueden ser usadas para separar un elemento del resto del contenido, así como para controlar la presentación visual de los elementos.

## Margin

**Margin** es el espacio entre un elemento y su entorno. Por ejemplo, el espacio entre una imagen y el texto que está alrededor de ella.

Para controlar el **margin**, se usa el atributo **style** con los valores de **margin-top**, **margin-right**, **margin-bottom** y **margin-left**.

Por ejemplo, para definir un **margin** de 10px a lo largo de todos los lados de un elemento, se puede usar el siguiente código:

```html
<p style="margin-top: 10px; margin-right: 10px; margin-bottom: 10px; margin-left: 10px;"></p>
```

## Padding

**Padding** es el espacio entre el contenido de un elemento y sus bordes. Por ejemplo, el espacio entre una imagen y los bordes de la etiqueta <img> que la contiene.

Para controlar el **padding**, se usa el atributo **style** con los valores de **padding-top**, **padding-right**, **padding-bottom** y **padding-left**. Por ejemplo, para definir un **padding** de 10px a lo largo de todos los lados de un elemento, se puede usar el siguiente código:

```html
<p style="padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;"></p>
```