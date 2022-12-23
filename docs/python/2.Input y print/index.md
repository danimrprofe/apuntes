

¡Hola mundo!
Mi primera línea de código
Es tradición que el primer programa que se escriba cuando uno aprende un lenguaje sea que aparezca por pantalla.
El comando para poder “escribir” en pantalla es print.  Entre paréntesis le decimos lo que tiene que imprimir, en este caso una frase

Al darle a run, ves que a la derecha muestra el resultado de nuestro programa.
Nota: verás que este archivo se llama main.py. Py es la extensión del archivo, sirve para saber que no es ni una canción (mp3) ni un documento (.pdf), sino un programa escrito con el lenguaje python.
Mi primer fallo
Ahora prueba esto. Verás que a la derecha te aparece mucho texto en rojo (malas noticias) y en inglés. Este texto te intenta decir que ha habido un error, seguramente por tu culpa, y te intenta explicar qué tipo y dónde se ha producido.

A veces nos daremos cuenta rápidamente de nuestro error, pero en otras ocasiones esto no es tan sencillo.
Intentando saber cuál es el fallo
Verás que pone:
File main.py. El error está en este archivo
Line 1. El error está en la línea 1 (solo tenemos una ahora mismo)
Tipo de error: Syntaxerror. Es decir, de sintaxis. No has escrito bien algo.
Con el tiempo, aprenderás los errores más comunes. En este caso, nos habíamos olvidado de las comillas y por eso no funcionaba.
La función print
¡Los paréntesis!
Poned las palabras que queráis ver escritas dentro de un paréntesis y entre comillas (simples o dobles, funcionan ambas)
Algo así como:
 Veréis que os sale la frase que habéis mandado sacar por pantalla. print es lo que llamamos una FUNCIÓN.
Cómo funciona
Una función es como un CONJURO. Cuando lo dices, pasa algo. En este caso, que salen cosas por pantalla.
Sabemos que algo es una función porque va seguido por un paréntesis, aunque esté vacío.
Los parámetros
Las cosas que van entre paréntesis se llaman parámetros. Pueden ser palabras, números, texto, variables, etc. Con ellos la función hace cosas.
Los parámetros se separan con comas, como una lista de la compra. Aquí print utiliza 3 parámetros, 2 frases y una variable

En la función PRINT debe ponerse dentro del paréntesis lo que quieras que aparezca en pantalla. También podemos hacer esto:

## Input

A veces necesitamos que el usuario nos escriba datos como un nombre, un número, etc. para guardarlo en algún sitio, o hacer operaciones. Para eso usamos la función input.
Cómo utilizar input

Como es una función, ya sabes que debe ir seguida de unos paréntesis, así que escribiremos:

Esta función hará aparecer en pantalla un cursor parpadeante y la posibilidad de que escribamos algo.  Hasta que no le des a la tecla intro, él espera pacientemente.

Pero claro... ¿dónde va a guardarse lo que yo escriba? Necesitamos reservar un espacio de memoria donde podamos guardar lo que escriba el usuario y un “indicador” para poder ir luego a buscarlo si queremos usar ese dato.

## Las variables
Y así llegamos al concepto de variable. Digamos que una variable es una CAJA donde voy a almacenar un dato.
Vamos a ver este ejemplo:

Aquí hago 3 cosas, escribir un texto, pedir información al usuario con el input y guardar esta información en una variable llamada nombre. En cualquier sitio que utilice esta palabra “nombre”, se cambiará por su valor, en este caso “Homer”.
Mira el siguiente ejemplo, pruébalo e intenta comprender qué hace cada instrucción. Aquí utilizaremos dos variables, nota y nombre.


Actividades
Actividad 1
Crea un programa que escriba en una línea diferente tu nombre y tus apellidos (3 líneas en total) utilizando print (sin utilizar input)
Daniel
Moreno
Rossello
Actividad 2
Crea un programa que te pida introducir los nombres de los miembros de tu familia uno a uno y te imprima una lista. Los nombres que tienen que aparecer se tienen que recoger con input
Mi padre se llama Juan
Mi madre se llama Cathelyn
Mi hermana pequeña se llama Arya
Actividad 3
Modifica el programa para que te pida escribir tu nombre y el nombre de tus padres y diga (cambiando los nombres por los de tu familia):
Me llamo Arya. padre se llama Eddard y mi madre Cathelyn.





