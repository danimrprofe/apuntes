# Sistemas de partículas

Un sistema de partículas es un conjunto de partículas que se mueven de forma coordinada. En Blender, un sistema de partículas se puede usar para crear efectos como humo, nieve, lluvia, etc.

Los sistemas de partículas en Blender se pueden configurar de forma muy detallada, permitiendo a los usuarios controlar cosas como la velocidad, el tamaño y la forma de las partículas. 

![](media/image1.png)

## Partículas

Crearemos un árbol de navidad y crearemos un efecto de nieve para practicar los sistemas de partículas. 

![](media/image2.png)

La simulación con sistemas de partículas permite obtener animaciones complejas de objetos que responden a fuerzas gravitatorias y acciones como las que produce el viento o un campo magnético. De esta forma podemos recrear lluvia, nieve, y otros.

Vista lateral del resultado

![](media/image3.png)

## 1. Crear el objeto que va a caer como si fuera un copo

El copo que vamos a crear es una icosfera y, a partir de ella se crearán múltiples copias.

![](media/image4.png)

Colocamos una icosfera con shift a mesh

Con G nos la colocamos en un sitio que no vea la cámara,  fuera de plano. Esto que véis es desde  shading

![](media/image4.png)

Le damos material y color para que se vea. Vamos a crear un material nuevo y le vamos a cambiar el nombre a nieve.

![](media/image5.png)

Le damos las características que queramos, que hagan que los copos se vean lo más similares posibles a la nieve real.

Metálico y especular son ambos tipos de materiales que se pueden usar en Blender. Los materiales **metálicos** generalmente se usan para crear objetos metálicos, mientras que los materiales **especulares** se usan para crear objetos más brillantes o reflectantes.

![](media/image6.png)

## 2. Crear un plano con emisiones

Los sistemas de partículas en Blender se pueden controlar usando **emisores**, que son objetos que se usan para generar las partículas. 

Los **emisores** pueden estar configurados para emitir partículas de forma continua o bajo ciertas condiciones, como cuando se colisionan con otro objeto.

Shift+a plano, y colocamos un plano

Lo pondremos encima del árbol, pero que no salga en el plano de la cámara. con GZ lo movemos hacia arriba, para colocarlo sobre la escena. 

Con S escalamos para que cubra toda la zona en la que queremos que nieve.

![](media/image7.png)

Al plano que lanza nieve le he cambiado el nombre para poder luego identificarlo más fácilmente.

![](media/image8.png)

## 3. Configuramos el plano para que emita partículas

Seleccionamos el plano generador de nieve

![](media/image8.png)

Le agregamos un particlesystem y configuramos los parámetros necesarios. Yo le he cambiado el nombre con F2 a partículas de nieve para identificarlo.

![](media/image9.png)

Configuramos los parámetros necesarios como número de copos, frames de inicio y fin y vida de los copos (cantidad de frames hasta que desaparecen).

![](media/image10.png)

Podemos ver la animación (tecla espacio), y veremos el efecto creado. De todos modos, tal como está en el render final no aparecerían las partículas.

## 4. Cambiamos el tipo de emisión para emitir objetos


Elegimos más abajo en **render** elegimos **render as object**.

El objeto tiene un **flag** que indica si el emisor está activo o no. Si se activa un emisor, se empieza a emitir partículas de forma continua, y si se desactiva, se para la emisión. Puede usar esta función para crear efectos de partículas en respuesta a eventos del juego (por ejemplo, una explosión).

En el submenú object seleccionamos en instance object la icosfera que habíamos creado. De este modo, le estamos diciendo que cree todos los objetos a partir de este.

<img src="media/image11.png" id="image13">

También cambiaremos velocity y physics para ajustar el comportamiento de los copos  y que este sea más realista.

<img src="media/image12.png" id="image14">

Volved a simular la animación y veréis que ya se comportan más como copos de nieve.

<img src="media/image13.png" id="image15">

## Colisiones y amortiguación

Al fondo hay que ponerle un modificador de colisión para que las partículas no lo atraviesen.

<img src="media/image14.png" id="image16">

Veréis que los copos rebotan como si fueran canicas, esto se puede modificar. En Physics podéis cambiar el comportamiento para que amortigüe los copos al tocar el suelo.

<img src="media/image15.png" id="image17">

Ahora los copos ya no atraviesan el plano y no rebotan, sino que se quedan parados en el suelo.

<img src="media/image16.png" id="image18">

## 6. Iluminación

Vamos a colocar una luz sobre la escena a fin de iluminar correctamente todos los objetos.

<img src="media/image17.png" id="image19">

## Insertar luz de área

Insertar una **luz de área** que esté justo encima de los objetos que queremos iluminar

<img src="media/image18.png" id="image20">

## Potencia

Propiedades de la luz. En mi caso le he puesto 1000 W de potencia y me ha parecido  suficiente.

<img src="media/image19.png" id="image21">

## Altura de la luz

En mi caso he colocado la luz a 12 metros de altura, como referencia, por si lo queréis hacer así, y centrado en origen de coordenadas para la x y la y.

<img src="media/image20.png" id="image22">

## Cámara

La cámara la podéis poner donde queráis. Yo la he modificado a ojo y en una posición en la que se vea bien la escena.

<img src="media/image21.png" id="image23">

## Escena final

Aquí podéis ver un resumen de como queda la escena, con todos los elementos.

<img src="media/image22.png" id="image24">
Copo de nieve

Árbol

Cámara

Plano emisor de la nieve

Luz que ilumina la escena

Fondo

Render final

<img src="media/image24.png" id="image25">