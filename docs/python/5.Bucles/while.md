BUCLES CONDICIONALES
En los ejemplos anteriores conocíamos el número de iteraciones, pero no siempre es el caso.
Esto es lo que se denomina un bucle condicional. Antes de cada iteración se comprueba si se cumple la condición, en el caso afirmativo se realiza una nueva iteración, en caso contrario, se sale del bucle.
Adivinar número
Pongamos un ejemplo sencillo, adivina un número... hasta que aciertes. Mejor dicho, MIENTRAS falles. Para ello, pediremos al usuario que adivine un número usando un while. Utilizaremos varias variables para ir guardando la información.
Clave guarda el número que tenemos que acertar (Se supone que el jugador solo ve la parte de la derecha).
En prueba guardaremos el número que va escribiendo el jugador

Explicación del programa
El bucle condicional empieza con “while” que significa mientras, se añade la condición que te permite seguir iterando (en este caso que la prueba que escribe en usuario sea distinta a la clave).
Cuando esa condición deje de cumplirse, salimos del bucle y ejecutamos el resto del programa, en este caso, ¡“Acertaste!”.
Algo muy importante en los bucles condicionales es que dentro del bloque de código del condicional SE CAMBIE LA VARIABLE SOBRE LA QUE SE INSPECCIONA LA CONDICIÓN. Si no lo hacemos así, ¿cómo podría dejar de cumplirse la condición y cómo podríamos salir del bucle? Nos quedaríamos “embuclados” ejecutando iteraciones infinitamente o hasta que algo fallara (por ejemplo, un número que anduviera creciendo y que desbordase la memoria, como pasa en la calculadora cuando llegamos a un número demasiado grande para la pantalla).