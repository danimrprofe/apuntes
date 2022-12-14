# HTML

## 1. INTRODUCCIÓN AL LENGUAJE HTML.

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

## 6. LISTAS CON HTML

Una lista permite organizar un documento HTML estructurándolo de la
forma más clara posible, para hacerlo más perceptible al lector.

Las listas se utilizan para dividir el documento así como para efectuar numeraciones de objetos.

HTML define varios tipos de listas:

### Listas sin numeración

```html
<UL> Elementos de la lista </UL>
```

Los elementos de la lista irán precedidos por un símbolo (fijo por defecto) que
puede variar según el nivel de anidamiento de la lista. Cada elemento de la misma
llevará la etiqueta: <LI> Primer elemento </LI>
Ejemplo de lista no ordenada:

### Listas con numeración

```html
<OL> Elementos de la lista </OL>
```
La etiqueta `<OL>` se utiliza para una lista ordenada o numerada. Cada marca
`<LI>` incrementará el número que se visualizará delante del elemento de la lista.

Ejemplo de lista numerada:

Las listas numeradas no sólo se pueden ordenar con números. También se
pueden utilizar letras y numeración romana tanto en mayúsculas como
minúsculas.

Para esto se utiliza el comando TYPE de la etiqueta `<OL>` con los
siguientes valores:

- TYPE=1, (por defecto) para números.
- TYPE=A, para letras mayúsculas.
- TYPE=a, para letras minúsculas.
- TYPE=I, para numeración romana en mayúsculas.
- TYPE=i, para numeración romana en minúsculas.

Por ejemplo:

```html
<OL TYPE=A> Elementos numerados con letras </OL>
```

**EJEMPLO PRÁCTICO 4.**

Realiza con el Bloc de notas, las siguientes listas.
Guarda el fichero con el nombre web04.html y ábrelo con el navegador.
Comprueba el resultado.

- Listas de definición: ``<DL>`` Elementos de la lista ``</DL>``

Una lista de definición es una lista no enumerada en la que se da una
descripción de cada uno de sus elementos. Un ejemplo típico es un glosario. Las
listas descriptivas están definidas por los siguientes elementos:

- Etiqueta ``<DL>``: abre una lista descriptiva y se cierra con ``</DL>``.
- Etiqueta ``<DT>``: precede a cada término de la lista. No tiene etiqueta de cierre.
- Etiqueta ``<DD>``: corresponde a la zona de definición de cada término. No tiene etiqueta de cierre.

## 7. ENLACES O HIPERVÍNCULOS.

Este elemento es uno de los más importantes del HTML, ya que es el que
realmente permite "navegar" por uno o varios documentos, que pueden
encontrarse en cualquier parte. Se definen los hipervínculos o hiperenlaces del
documento Web mediante la etiqueta ``<A>``.

Sus comandos más importantes son: NAME, HREF y TARGET.

Vamos a distinguir tres tipos de enlaces:

- Enlaces dentro de la misma página.
- Enlaces con otra página, que puede encontrarse dentro o fuera de nuestro
sistema.
- Enlaces con una dirección de correo electrónico.

### 7.1 ENLACES DENTRO DE LA MISMA PÁGINA.

A veces, en el caso de documentos (o páginas) muy extensos, nos puede
interesar dar un salto desde una posición a otra determinada.
Podemos realizarlo de dos formas:

```html
<A HREF="#marca"> Zona Activa </A> (marca puede ser cualquier palabra).
<A NAME="marca">Zona Activa </A> (marca puede ser cualquier palabra).
```

### 7.2 ENLACES A OTRA PÁGINA

En este caso, simplemente sustituimos lo que hemos llamado marca (el
destino del enlace) por el nombre del fichero html.

```html
<A HREF="web02.html"> Zona Activa </A>
```

Si queremos hacer un enlace a una dirección web (URL), simplemente
sustituimos lo que hemos llamado marca (el destino del enlace) por la dirección de
la página web.

```html
<A HREF=“http://colegioliceosorolla.es"> Zona Activa </A>
```

### 7.3 ENLACE A UNA DIRECCIÓN DE CORREO ELECTRÓNICO.

La estructura de la etiqueta es:
```html
<A HREF="mailto: dirección de email"> Zona Activa </A>
```

### 7.4 ENLACE EN UNA NUEVA VENTANA.

Se utiliza el comando TARGET. La estructura de la etiqueta será:
```html
<A HREF="indice.html" TARGET="ventana2"> Nueva ventana </A>
```
## 8. IMÁGENES CON HTML

En HTML se debe indicar el nombre y la localización de un fichero que
contiene una imagen. Para ello utilizamos la etiqueta IMG con el comando SRC que
sirve para indicar donde se encuentra la imagen. La estructura de la etiqueta es:
```html
<IMG SRC=“C://Mis Documentos/Imagenes/imagen.gif">
```
### 8.1 COMANDOS PARA LAS IMÁGENES.

- ALT: El comando ALT permite introducir una descripción (una palabra o una
frase breve) indicativa de la imagen.
```html
<IMG SRC="imagen.gif" ALT="descripción">
```
- ALIGN: Alinea la imagen, según la posición que se le indique, respecto a la
línea de texto en la que está. Puede tomar los siguientes valores:
* TOP: Alinea la parte superior de la imagen con la línea actual.
```html
<IMG SRC="images/flor.gif" ALIGN="top">
```
* MIDDLE: Alinea el centro de la imagen con la línea actual.
```html
<IMG SRC="images/flor.gif" ALIGN="middle">
```
* BOTTOM: Alinea la base de la imagen con la línea actual.
```html
<IMG SRC="images/flor.gif" ALIGN="bottom">
```
- WIDTH: Redefine el ancho de la imagen.
- HEIGHT: Redefine el alto de la imagen.
```html
<IMG SRC="images/flor.gif" ALIGN="right" WIDTH=30 HEIGHT=30>
```
- BORDER: Dibuja un marco alrededor de la imagen.
```html
<IMG SRC="images/flor.gif" ALIGN="right" BORDER=2>
```

### 8.2 IMÁGENES Y ENLACES.

Los hipervínculos pueden ser también definidos sobre imágenes de tal forma
que al hacer clic con el ratón sobre algún punto de la superficie de éstas, se pase al documento correspondiente.

Esto suele ser utilizado sobre todo para introducir botones de navegación en
las páginas HTML. Una imagen que actúa de hipervínculo se distingue mediante un
borde de color alrededor de ésta.
```html
<A HREF="forms.htm"><IMG SRC="images/boton1.gif"></A>
```

## TABLAS CON HTML.

La etiqueta general, que engloba a todas las demás es ``<TABLE>`` y ``</TABLE>``.
```html
<TABLE>
[Resto de las etiquetas]
</TABLE>
```

Se puede utilizar con los siguientes comandos:

- ``BORDER``: define el grosor del marco exterior, (puede ser cero, que es el valor
por defecto).
- ``CELLPADDING``: define el espacio alrededor del texto de una celda.
- ``CELLSPACING``: define el espacio entre celdas.

El valor de estos atributos se especifica en **píxeles**. Cuando no se les asigna
ningún valor explícitamente estos atributos tomarán valores definidos por defecto.

Se puede determinar el tamaño de la tabla, bien forzándola a ocupar un
cierto porcentaje de la anchura de la ventana del navegador o definiendo un
tamaño fijo en unidades, mediante los atributos:

- ``WIDTH``: define el ancho de la tabla, bien en % o en unidades.
- ``HEIGTH``: define el alto de la tabla, bien en % o en unidades.

A continuación, debemos comenzar a construir la tabla. Para ello indicamos el
comienzo de la primera fila con la etiqueta ``<TR>``, y después marcamos en cuantas celdas dividiremos la fila con la etiqueta ``<TD>``. Para finalizar cada celda y cada fila cerraremos la etiquetas ``</TD>`` y ``</TR>``. La estructura quedará de la siguiente forma:

```html
<TABLE BORDER=1>
<TR>
<TD>fila1-celda1</TD>
<TD>fila1-celda2</TD>
<TD>fila1-celda3</TD>
</TR>
<TR>
<TD>fila2-celda1</TD>
<TD>fila2-celda2</TD>
<TD>fila2-celda3</TD>
</TR>
</TABLE>
```

### 9.1 COMANDOS DE LA ETIQUETA TR.

- VALIGN: permite una alineación del texto en el sentido vertical de la celda.
Admite los valores: TOP, BOTTOM, MIDDLE.
- ALIGN: permite una alineación del texto en el sentido horizontal de la celda.
Admite los valores: RIGHT, CENTER, LEFT.

### 9.2 COMANDOS DE LA ETIQUETA <TD>.

Además de los anteriores para <TR>, tenemos:
- COLSPAN: define una celda con una anchura múltiplo de la columna básica.
- ROWSPAN: define una celda con una anchura múltiplo de la fila básica.

### 9.3 COLOR DE FONDO DE LAS CELDAS.

Utilizaremos el comando BGCOLOR, igual que para el fondo de las páginas,
dentro de la etiqueta <TD>.
Ejemplo: <TD BGCOLOR=“red”>.

**EJEMPLO PRÁCTICO 5**

En el Bloc de notas, copia el siguiente código HTML.

Guarda el fichero con el nombre web05.html y ábrelo con el navegador.

Comprueba el resultado.

```html
<HTML>
<HEAD>
<TITLE>PÁGINA DE TABLAS: SOMBREADO DE CELDAS</TITLE>
</HEAD>
<BODY><CENTER><H1>CELDAS CON COLOR DE SOMBREADO</H1>
 <TABLE BORDER=5 >
 <TR>
 <TD BGCOLOR="#00FF00">FILA 1, COLUMNA 1;</TD>
 <TD BGCOLOR="#FFFF00"> FILA 1, COLUMNA 2;</TD>
 <TD BGCOLOR="#006600"> FILA 1, COLUMNA3</TD>
 <TD BGCOLOR="#9900FF"> FILA 1, COLUMNA 4;</TD>
 </TR>
 <TR>
 <TD BGCOLOR="#FF0000"> FILA 2, COLUMNA 1</TD>
 <TD BGCOLOR="#C0C0C0"> FILA 2, COLUMNA 2</TD>
 <TD BGCOLOR="#00FFFF"> FILA 2, COLUMNA 3</TD>
 <TD BGCOLOR="#FF0066"> FILA 2, COLUMNA 4</TD>
 </TR>
 <TR>
 <TD BGCOLOR="#0000FF"> FILA 3, COLUMNA 1</TD>
 <TD BGCOLOR="#FF6600"> FILA 3, COLUMNA 2</TD>
 <TD BGCOLOR="#800000"> FILA 3, COLUMNA 3</TD>
 <TD BGCOLOR="#FFFFFF"> FILA 4, COLUMNA 4</TD>
 </TR>
 </TABLE>
</CENTER>
</BODY>
</HTML>
```