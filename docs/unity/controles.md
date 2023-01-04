# Controles

## Movimiento de personajes

Con el uso de las teclas W y S para el jugador 1 (izquierda) y las teclas de flecha de arriba y abajo para el jugador 2 (derecha), podremos jugar dos jugadores en el mismo teclado. Esto nos permitirá controlar los movimientos de nuestros personajes de una manera sencilla y eficiente.

## Redefinir controles

Para redefinir los controles, vamos a ir a ``Edit > Project Settings > Input Manager``. Aquí vemos que hay varias cosas declaradas, como **Axis**. Estos son los controles que Unity tiene asignados por defecto para las teclas de nuestro teclado.

Por ejemplo, para el eje **horizontal**, está asignado a las teclas de flechas o el número 'A' para izquierda y derecha. Y para el eje **vertical**, está asignado a las teclas de W, A, S y D, y las flechas de arriba y abajo. Así que si queremos cambiar estos controles, podemos hacerlo en el Input Manager.

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos13.png)

## Controles para segundo jugador

Tenemos que crear el elemento vertical2 que es para nuestro player2. Tenemos que diferenciar pues que uno utilice el WS y el otro utilice la flecha hacia arriba y hacia abajo. Lo tenemos que diferenciar entonces lo que vamos a hacer es del vertical vamos a borrar el SW que tenemos aquí. Vamos a duplicarlo para tener un vertical2 para nuestro jugador 2; clic derecho duplicate element y se duplicará que vendrá por aquí otra como vertical y lo llamamos vertical2.

Lo que faltaría es cambiarle los controlessi el player1 juega con la flecha de arriba y hacia abajo. Nosotros con el jugador 2 jugaremos con la W y S. En negativo ponemos S y en positivo W. Dentro del objeto player, en función de si es el 1 o el 2, seleccionaremos el control oportuno.

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos14.png)

## Dentro de los scripts, podemos acceder a los diferentes controles por su nombre

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos15.png)

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos16.png)