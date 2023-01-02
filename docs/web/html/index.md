# HTML

## 1. INTRODUCCIÓN AL LENGUAJE HTML

El lenguaje HTML (Hyper Text Markup Language) es un lenguaje que sirve
para escribir hipertexto, es decir, documentos de texto presentado de forma
estructurada, con enlaces (links) que conducen a otros documentos o a otras
fuentes de información (por ejemplo bases de datos) que pueden estar en tu propia
máquina o en máquinas remotas de la red. Todo ello se puede presentar
acompañado de cuantos gráficos estáticos o animados y sonidos seamos capaces
de imaginar.

Todas las codificaciones de efectos en el texto que forman el lenguaje HTML
no son más que instrucciones para el visualizador (navegador o browser).
Actualmente existen multitud de ellos, aunque los más conocidos son el Internet
Explorer de Microsoft (IE), el Google Chrome, o el Mozilla Firefox, y sin olvidar el navegador Opera.

Una página escrita en HTML no es más que texto normal, escrito con
cualquier editor, acompañado de ciertos códigos para indicar el efecto deseado. A
estos códigos se les llama etiquetas o elementos del lenguaje.

## 2. ESTRUCTURA DE UN DOCUMENTO HTML.

El principio esencial del lenguaje HTML es el uso de las etiquetas (tags).
Funcionan de la siguiente manera:
<CÓDIGO> Este es el inicio de una etiqueta.
</CÓDIGO> Este es el cierre de una etiqueta.
Las letras de la etiqueta pueden estar en mayúsculas o minúsculas,
indiferentemente. Por claridad, usaremos las mayúsculas.
Lo que haya entre ambas etiquetas estará afectada por ellas. Por ejemplo,
todo el documento HTML debe estar entre las etiquetas <HTML> y </HTML>:

```html
<HTML>
     [Todo el documento]
</HTML>
```

El documento en sí está dividido en dos zonas principales:

- La CABECERA: comprendido entre las etiquetas <HEAD> y </HEAD>
Dentro del encabezamiento hay información del documento, que no se ve en
la pantalla principal, principalmente el título del documento, comprendido entre
las etiquetas <TITLE> y </TITLE>. El título debe ser breve y descriptivo de su
contenido, pues será lo que vean los demás cuando añadan nuestra página a sus
favoritos.
- El CUERPO: comprendido entre las etiquetas <BODY> y </BODY>
Dentro del cuerpo está todo lo que queremos que aparezca en la pantalla
principal (texto, imágenes, etc.). Por tanto, la estructura queda de esta manera:

```html
<HTML>
 <HEAD>
 <TITLE> Título de la página </TITLE>
 </HEAD>
 <BODY>
 [Aquí van las etiquetas que visualizan la página]
 </BODY>
</HTML>
```

## 3. EJEMPLO DE UN DOCUMENTO HTML

Antes de crear nuestra primera página, unas consideraciones sobre el texto:

- Cuando escribimos en el documento el texto que queremos que aparezca
en la pantalla, veremos que éste se acomoda a ella, sin que tengamos que
pulsar el retorno del carro. Si queremos separar el texto en distintos párrafos
debemos usar la etiqueta <P>, (que tiene su correspondiente etiqueta de
cierre </P>).
- El texto se puede colocar entre las etiquetas <H1> y </H1>, <H2> y </H2>,
etc. (hasta el número 6). Este número indica el tamaño del mismo. El tamaño
mayor es el correspondiente al número 1.
- La etiqueta para centrar es <CENTER> y </CENTER>. Nos centra todo lo que
esté dentro de ella, ya sea texto, imágenes, etc.
- Si queremos separar los párrafos, o cualquier otro elemento, pero sin dejar
una línea en blanco, usamos una etiqueta parecida <BR> (romper la línea).
- También tenemos los separadores que se consiguen con la etiqueta <HR>
(no existe la correspondiente de cierre). Con ella se obtiene una línea
horizontal tan ancha como la pantalla.

**EJEMPLO PRÁCTICO 1**

En el Bloc de notas copiamos lo siguiente:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Esto es el nombre de la página</title>
    </head>
    <body>
        <h1>Esto es un título</h1>
        <p>Esto es un párrafo</p>
    </body>
</html>
```

Guardamos el fichero con el procesador de textos con el nombre de web01.html y lo
abrimos con el navegador. Comprueba el resultado.

## Títulos

Para crear un título se utilizan las etiquetas h1, h2, etc.

```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
```

## Párrafos

El elemento HTML ``<p>`` define un párrafo.

Un párrafo siempre comienza en una nueva línea y los navegadores agregan automáticamente un espacio en blanco (un margen) antes y después de un párrafo.

```html
<p>Esto es un párrafo</p>
<p>Esto es otro</p>
```

## Estilos

Para destacar alguna parte del texto se pueden usar las siguientes etiquetas:

- NEGRITA: <B> Texto en negrita </B>
- CURSIVA: <I> Texto en cursiva </I>
- SUPERÍNDICES: <SUP> Texto como superíndice </SUP>
- SUBÍNDICES: <SUB> Texto como subíndice </SUB>

## Estilos de párrafo

Para asignar estilos, utilizaremos el atributo ``style``.

```html
<p style="color:red;">Soy rojo</p>
<p style="color:blue;">Soy azul</p>
<p style="font-size:50px;">Soy grande</p>
```

## Color en HTML

Tenemos colores predefinidos en HTML con nombre (red, blue), pero también los podemos definir nosotros. Para ello se puede usar el sistema RGB, que nos permite afinar más el color que queramos.

```html
<p style="color:red;">Esto es rojo</p>
<p style="color:#FF0000;">Esto también es rojo</p>
```

## ¿Cómo podemos especificar un color en concreto?

El color es un código hexadecimal, formado por tres pares de dígitos, precedidos del símbolo #, que pueden ser números y letras entre [ 0 1 2 3 4 5 6 7 8
9 A B C D E F ].

Con estos dígitos el par de menor valor será el 00 y el de mayor valor
será el FF

Los colores primarios son:

- #FF0000 - Rojo
- #00FF00 - Verde
- #0000FF - Azul

Otros colores son:

- #FFFFFF - Blanco
- #000000 - Negro
- #FFFF00 – Amarillo

Oscurecer un color. Para hacer un color más oscuro, hay que reducir el
número de su componente, dejando los otros dos invariables. Así, el rojo #FF0000 se puede hacer más oscuro con #AA0000, o aún más oscuro con #550000.

Aclarar un color. Para hacer que un color tenga un tono más suave (más
pastel), se deben variar los otros dos colores haciéndolos más claros, aumentando
su componente, (número más alto), en una cantidad igual. Así, podemos convertir el
rojo en rosa con #FF7070.


## 5. COLORES E IMÁGENES EN EL CUERPO DE LA PÁGINA.

Existen varios comandos o atributos de la etiqueta ``BODY`` que permiten
controlar el color del fondo de la ventana del navegador, el color de los caracteres
del texto. La sintaxis será:
```html
<BODY atributo1 atributo2 atributo3 ... atributoN >
```
- Comando BGCOLOR. Este atributo permite establecer un color de fondo
para el documento.
```html
<BODY BGCOLOR="#C0C0C0">
```
- Comando BACKGROUND. Este atributo permitirá se utilice una imagen
residente en el servidor, o en un fichero local, como fondo de página.
```html
<BODY BACKGROUND="fichero_gráfico.gif">
```
- Comando TEXT. Permite controlar el color del texto estándar, es decir, todo
texto que no especifique un enlace. Este ejemplo hará que, por defecto, el texto del
documento aparezca de color azul oscuro.
```html
<BODY TEXT="darkblue">
```

**EJEMPLO PRÁCTICO 3.**

Modifica con el Bloc de notas, el documento anterior
añadiendo color y una imagen de fondo. Guarda el fichero con el nombre
web03a.html; web03b.html, respectivamente y ábrelo con el navegador.
Comprueba el resultado.

```html
<HTML>
<HEAD>
<TITLE> Esta es mi Primera página WEB </TITLE>
</HEAD>
<BODY bgcolor="#FFFF99" background="felicidad.jpg">
<H1> <CENTER> <i><b><font color="#FF0000" size="6">Primera página </font>
</b></i> </CENTER> </H1>
<HR>
<font color="#FF0000"><b>Esta es mi primera página, todavía es muy sencilla. La iré
completando poco a poco ya que el </b></font><b><font color="#FF0000">lenguaje HTML no es
difícil. Más adelante realizaré páginas más completas.
</font></b> <P>
<b><font size="4" color="#FF0000">Aquí voy a escribir mi nombre: </font></b>
 </BODY>
</HTML>
```
