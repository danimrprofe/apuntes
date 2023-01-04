# Componentes

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos6.png)

## Los componentes se añaden a un objeto y modifican sus propiedades

Debajo veréis que se pueden agregar más componentes \( __add component__ \) según este objeto lo necesite\.

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos7.png)

## Componentes de un objeto

En Unity, cada objeto tiene asociados componentes que modifican su comportamiento y cada uno de ellos presenta sus propias opciones. Esto permite personalizar el objeto y darle una funcionalidad específica.

 Unity permite personalizar los objetos para darles una funcionalidad específica mediante el uso de componentes asociados a cada uno. Por ejemplo, para un objeto 'player' los componentes incluyen el ``Transform`` para controlar la posición, rotación y la escala, el ``Spriterenderer`` para controlar el color, material y el orden de los objetos, el ``BoxCollider 2D`` para controlar las colisiones y el ``Rigidbody`` para hacer que se apliquen físicas al objeto.

## Componente `` Rigidbody 2D``

``Rigidbody2D`` es un componente de Unity que se utiliza para añadir físicas a un objeto 2D. Un Rigidbody2D le permite a un objeto 2D afectado por la gravedad, el empuje, la fricción y otras fuerzas físicas. Esto permite a los desarrolladores añadir realismo y jugabilidad a los juegos 2D.

## Rigid bodies

Asignaremos los componentes `` Rigidbody 2D``  a nuestros jugadores y a la pelota. Podemos seleccionar todos los objetos y seleccionar el componente `` Rigidbody 2D``  para añadirlo. Al dar a play los objetos con Rigidbody caerán, pues sobre ellos actúa la gravedad. Para quitarles el efecto de la gravedad, donde pone gravity podemos ponerlo a 0 y así ya no se caerán.

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos8.png)

## POsición del objeto

Para cambiar la posición de un objeto, cambiamos su __Transform__. Esto define donde se encuentra el objeto, así como si cambia de forma o rota. El rigidbody permite que las físicas modifiquen estas propiedades automáticamente. Esto significa que el objeto puede recibir fuerzas para moverse de forma realista. Por ejemplo, la __gravedad__ afectará la posición del objeto para simular su efecto, haciendo que caiga hacia abajo en el eje Y.

## Componente BOX COLLIDER 2D

## Los colliders permiten detectar colisiones y tomar decisiones en función de estas

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos9.png)

## Componente Box Collider

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos10.png)

Los colliders permiten detectar colisiones y tomar decisiones en función de estas. Para ello tenemos que agregarles el componente necesario. Seleccionamos todos los objetos que queramos con ++shift++ pulsado y luego añadir componente y añadimos un box collider 2D. Si no queremos que alguno tenga colisiones, no lo debemos seleccionar.