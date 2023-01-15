2.	Estilos de tablas
1.	Dar estilos a las tablas
Para aplicar estilos a nuestra tabla, vamos a incluir dentro de la etiqueta HEAD una etiqueta STYLE, en la que vamos a poner los estilos que queremos que tengan los diferentes elementos.
Con esto, conseguiremos que table, th y td tengan un borde de 1 pixel de grosor, sólido y de color negro.

Como ves, la tabla tiene ahora dos bordes diferentes, uno exterior para toda la tabla  unos interiores para cada celda. Esto lo podemos arreglar.
2.	Cambiar el color del borde

3.	Juntar los dos bordes en uno solo
Para ello, podemos utilizar la propiedad border-collapse:

1.	Efecto tabla sin borde
Otro estilo interesante podría ser hacer como que no existe borde (lo pondremos blanco) y dar un color de relleno a las celdas:

4.	Tamaño de tabla
Especificar el tamaño de la tabla:
Para ocupar el 100% de la pantalla:

5.	Cambiar ancho de una columna
Para que una columna tenga un ancho determinado, tengo que indicarlo en uno de los TD de esa columna.
<td style="width:70%">Firstname</th>

6.	Cambiar altura de una fila
Si quiero que una fila tenga una altura determinada:
<td style="height:200px">

7.	ATRIBUTOS DE LA ETIQUETA <TR>
* VALIGN: permite una alineación del texto en el sentido vertical de la celda.
o	Admite los valores: TOP, BOTTOM, MIDDLE.
* ALIGN: permite una alineación del texto en el sentido horizontal de la celda.
o	Admite los valores: RIGHT, CENTER, LEFT.
8.	ATRIBUTOS DE LA ETIQUETA <TD>
Además de los anteriores para <TR>, tenemos:
-	COLSPAN: define una celda con una anchura múltiplo de la columna básica.
-	ROWSPAN: define una celda con una anchura múltiplo de la fila básica.
9.	COLOR DE FONDO DE LAS CELDAS.
Utilizaremos el comando BGCOLOR, igual que para el fondo de las páginas, dentro de la etiqueta <TD>.
* Ejemplo: <TD BGCOLOR=“red”>.
10.	Espaciado interior y exterior (padding y spacing)
El padding es el espacio entre los bordes y el contenido de la celda

El spacing es la distancia entre dos celdas adyacentes.
