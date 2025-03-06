s- [Unity](#unity)
- [Unity](#unity)
  - [Proyectos](#proyectos)
  - [Objetivos](#objetivos)
  - [Instalación y configuración](#instalación-y-configuración)
  - [Crear un proyecto](#crear-un-proyecto)
- [Cambiar resolución](#cambiar-resolución)
- [Cambiar el layout](#cambiar-el-layout)
- [05. Componentes](#05-componentes)
  - [Componentes de un objeto](#componentes-de-un-objeto)
  - [4. Crear pelota](#4-crear-pelota)
  - [Crear Jugadores y Paredes](#crear-jugadores-y-paredes)
  - [Duplicar objetos](#duplicar-objetos)
  - [Sprites](#sprites)
  - [Crear Paredes de los Lados](#crear-paredes-de-los-lados)
  - [07. Nombrando los objetos](#07-nombrando-los-objetos)
  - [08. Creando los jugadores](#08-creando-los-jugadores)
- [Pelota](#pelota)
  - [09. Componentes Rigid Body](#09-componentes-rigid-body)
  - [10. Ordenar objetos](#10-ordenar-objetos)
  - [11. Movimiento de personajes](#11-movimiento-de-personajes)
- [CONTROLES](#controles)
  - [Redefinir controles](#redefinir-controles)
  - [Controles para segundo jugador](#controles-para-segundo-jugador)
  - [Dentro de los scripts, podemos acceder a los diferentes controles por su nombre](#dentro-de-los-scripts-podemos-acceder-a-los-diferentes-controles-por-su-nombre)
- [SCRIPTS](#scripts)
  - [13. Script de programación](#13-script-de-programación)
  - [14. Asignar script al jugador](#14-asignar-script-al-jugador)
  - [Cambiar el booleano para player2](#cambiar-el-booleano-para-player2)
  - [Asignar rigidbody al script](#asignar-rigidbody-al-script)
  - [Crear método reset en el script](#crear-método-reset-en-el-script)
  - [Crear script para la pelota](#crear-script-para-la-pelota)
  - [Asignar script a la bola](#asignar-script-a-la-bola)
  - [Asignar el rigibody](#asignar-el-rigibody)
  - [Crear material para la pelota](#crear-material-para-la-pelota)
  - [Restringir movimientos en los players](#restringir-movimientos-en-los-players)
  - [Reorganizar archivos](#reorganizar-archivos)
  - [Crear interfaz puntuación](#crear-interfaz-puntuación)
  - [Cambiar posición](#cambiar-posición)
  - [Cambiar pelota y hacerla redonda](#cambiar-pelota-y-hacerla-redonda)
  - [Crear el script del juego](#crear-el-script-del-juego)
  - [Añadir las referencias a objetos](#añadir-las-referencias-a-objetos)
  - [Marcar trigger en las porterías](#marcar-trigger-en-las-porterías)
  - [Crear script para las porterías](#crear-script-para-las-porterías)
  - [Asignar scripts](#asignar-scripts)
  - [Asignar etiqueta a la bola](#asignar-etiqueta-a-la-bola)
  - [Crear referencias](#crear-referencias)
  - [Cambiar colores](#cambiar-colores)
  - [Inteligencia artificial](#inteligencia-artificial)
- [ESCENAS](#escenas)
  - [Crear botones](#crear-botones)

# Unity

En este tema vamos a trabajar el desarrollo de videojuegos. Para crear un videojuego, hacen falta conocimientos de diseño y de programación. Para el diseño, utilizaremos un motor de videojuegos llamado ``Unity``, que nos permite crear proyectos 2D y 3D. También existen otros motores, como **unreal engine**, pero más complejos y caros.

Unity es un motor de videojuegos **multiplataforma**. Es decir, que permite desarrollar juegos en 2D y 3D para diversas plataformas, como:

- PC
- Consolas
- Móviles
- Gafs de realidad virtual

Además del propio diseño, la lógica del juego y el comportamiento de sus diferentes elementos se programan con un lenguaje de programación, en nuestro caso el lenguaje utilizado es **C#**. Para la programación, cualquier IDE es válido. Nosotros utilizaremos **Visual Studio Code**.

![](img/2025-02-19-12-34-23.png)

## Proyectos

Durante este curso haremos dos proyectos guiados. Para ambos nos vamos a basar en los tutoriales del canal de **luiscanary**.

**Proyecto 1:** pong

El primer proyecto es un proyecto 2D sin físicas de gravedad, el juego clásico de Pong. En él, dos palas accionadas con control del teclado harán rebotar una pelota, intentando que entre en la portería contraria.

Playlist: https://www.youtube.com/watch?v=Mk8e5an2mG8&list=PLNEAWvYbJJ9ltqR_CI5-ZV7p6Emz-v-di

![](img/2023-12-02-20-05-58.png)

**Proyecto 2:** plataformas 2D

En este proyecto aumentará la complejidad pues:

- Los sprites contendran imágenes de tipo pixel art. En nuestro caso utilizaremos una librería de **assets** o recursos gratuitos, para evitarnos tener que crear todas las imágenes.
- Incorporaremos **físicas** relacionadas gravedad, por lo que nuestro jugador tendrá que saltar.
- Crearemos **materiales** que variaran el comportamiento de las diferentes superficies.

Playlist: https://www.youtube.com/watch?v=-m7ZaHhkDAc&list=PLNEAWvYbJJ9kZpaIg2RfzAc_KZixBgchT

![](img/2023-12-02-20-05-14.png)

## Objetivos

Aprendremos a:

- Crear ``objetos`` de sprite 2D y colocarlos en escena
- Programar ``scripts`` que, asignados a los objetos, controlen su comportamiento
- Utilizar ``controles`` de teclado para mover los objetos
- Asignar `componentes` como los ``rigidbody`` para agregar respuesta a físicas en nuestros sprites
- Agregar ``colliders`` a los objetos para controlar las colisiones entre ellos y modificar el comportamiento del juego.

## Instalación y configuración

Para instalar necesitaremos seguir los siguientes pasos:

1. Descargar ``unity hub`` desde la página oficial: https://unity.com/download
2. Crear un ``usuario`` de unity
3. Instalar el ``editor de unity``

### Unity Hub

En primer lugar nos descargaremos el ``Unity hub``, una aplicación desde la que podremos gestionar las instalaciones y actualizaciones de todos los programas relacionados con Unity.

![Alt text](image.png)

Además de instalarlo, tendremos que crear una cuenta de unity.

También se nos mostrarán los proyectos que tenemos creados.

![](img/2023-03-02-08-13-56.png)

### Cuenta de usuario

Para gestionar nuestras instalaciones, necesitaremos crear una cuenta de usuario de ``Unity``, que deberemos crear para poder iniciar sesión y trabajar en nuestros proyectos.

### Editor de Unity

Posteriormente, instalaremos el ``editor de unity``, que nos permitirá crear nuestros juegos.

## Crear un proyecto

### Abrimos unity

Ahora mismo tenemos instalados dos programas: el Hub, y el Unity editor en sí (color negro). Este es el que tenemos que abrir.

![](2023-03-02-12-50-36.png)

### Carga de unity

Se nos abre la pantalla de carga de ``Unity``.

![](2023-03-02-12-50-21.png)

Finalmente veremos la ``pantalla de proyectos``, desde la que podremos abrir un proyecto existente o crear un proyecto nuevo.

![](2023-03-02-12-51-44.png)

### Información de proyectos existentes

Podemos observar los proyectos, la carpeta en la que se guarda el proyecto, así como la ``versión del editor`` con el que ha sido creado el proyecto.

![](2023-03-02-12-52-35.png)

### Plantillas

Existen diferentes ``plantillas`` de proyecto que podemos utilizar y que vienen configuradas con diferentes opciones, según el tipo de juego que queramos hacer,

![](img/2025-02-19-12-36-54.png)

### Crear nuestro proyecto

En nuestro caso vamos a utilizar la plantilla ``2D core`` y le ponéis el nombre que queráis.

Arriba podréis elegir la versión del editor con la que vais a crear el proyecto.

![plantillas](2023-03-02-12-47-35.png)

# Cambiar resolución

En Unity, la relación de **aspecto** (aspect ratio) se refiere a la proporción entre el ancho y la altura de la pantalla en la que se renderiza el juego. Esto es clave para asegurarse de que los elementos en pantalla se vean correctamente en diferentes dispositivos y resoluciones.

![](2023-03-02-12-54-52.png)

# Cambiar el layout

En Unity, puedes cambiar el **layout** de las ventanas para adaptarlo a tu flujo de trabajo.

![](img/2025-02-19-12-40-05.png)

Cómo Cambiar el Layout en Unity

1. Abrir el menú de layouts
2. En la barra superior de Unity, ve a ``Window > Layouts``.
3. Aparecerán varias opciones predefinidas. Seleccionar "2 by 3"
4. Unity reorganizará las ventanas en **dos** columnas a la izquierda y **tres** filas a la derecha.

# 05. Componentes

En un juego de Unity, los **objetos** o GameObjects representan los elementos del juego, y sus **componentes** definen su apariencia y comportamiento.

## Componentes de un objeto

En ``Unity``, cada objeto tiene asociados **componentes** que modifican su comportamiento y cada uno de ellos presenta sus propias opciones. Esto permite personalizar el objeto y darle una funcionalidad específica.

 ``Unity`` permite personalizar los objetos para darles una funcionalidad específica mediante el uso de componentes asociados a cada uno. Por ejemplo, para un objeto 'player' los **componentes** incluyen:

- El componente ``Transform`` para controlar la posición, rotación y la escala,
- El componente ``Spriterenderer`` para controlar el color, material y el orden de los objetos
- El componente ``BoxCollider 2D`` para controlar las colisiones
- El componente ``Rigidbody`` para hacer que se apliquen físicas al objeto.

Los componentes no son obligatorios, sinó que se añaden a cada objeto en función de las características que queramos que tenga.

## 4. Crear pelota

Dentro de nuestra ventana lo que vamos a hacer es ``clic derecho`` y darle a ``spritesquare`` y se pone un cuadrado que es el que vamos a utilizar para la bola.

![](2023-03-02-12-56-44.png)

El **2D Object > Sprite > Square** en Unity solo tiene dos componentes principales:

- **Transform**: Controla la posición, rotación y escala del objeto.
- **Sprite Renderer**: Se encarga de dibujar el sprite en la pantalla.

Además de estos, podemos agregarle más componentes si lo necesitamos.

## Crear Jugadores y Paredes

Para construir los jugadores y las paredes en **Pong**, utilizaremos **GameObjects** escalables en diferentes ejes sin necesidad de descargar ningún recurso adicional. Todo se creará directamente en Unity.

### 1. Crear las Paredes (Superior e Inferior)

1. **Crear un GameObject:** Ve a **GameObject > 2D Object > Sprite > Square** para añadir un objeto cuadrado.
2. **Escalar en el eje X:** En el **Inspector**, ajusta la **escala en X** a **18** para que cubra el ancho de la pantalla.
3. **Posicionar en el centro:** Ajusta la **posición en X e Y** a **(0,0)** para centrarlo.
4. **Mover la pared superior:**
   - Selecciona el objeto y usa la herramienta de mover (atajo de teclado **W**).
   - Arrástralo hacia arriba para colocarlo en la parte superior de la pantalla.

Repite el proceso para la pared inferior, pero moviéndola hacia abajo.

## Duplicar objetos

Podemos ``duplicar`` un objeto en lugar de crear uno nuevo. este que tenemos y ponerlo pues abajo del todo para ello pues lo que podéis hacer es control de o ``clic derecho > duplicate`` se duplicará y ahora lo único que tenemos que hacer es en vez de ir arrastrando lo va a estar en la posición contraria a 5 en este caso pues sería menos 5 a esta

## Sprites

Un ``sprite`` es una imagen bidimensional que se utiliza como elemento gráfico en un videojuego. Se dibuja con herramientas de gráficos vectoriales o bitmap y se usa para representar **personajes, objetos, entornos** o cualquier otra imagen.

Estos ``sprites`` se pueden importar directamente desde un archivo de imagen o se pueden crear desde cero usando ``Unity``.

Los ``sprites`` se pueden mover, girar, escalar y rotar fácilmente con ``Unity``. También se pueden usar para crear animaciones y efectos especiales.

![](img/2023-02-07-15-58-21.png)

Todos los objetos por defecto tienen una posición y un tamaño\. Esto se cambia en el ``componente Transform``

## Crear Paredes de los Lados

### 1. Crear la Primera Pared

A partir de un jugador:

1. **Duplicar el objeto:** Haz clic derecho sobre el objeto y selecciona **Duplicate**.
2. **Escalar el objeto:** Ajusta la escala hasta que se coloque correctamente.
3. **Paneo con la rueda del ratón:** Si pulsas la rueda del ratón, puedes hacer un paneo en la escena.

Ahora, para colocar la pared en su lugar:

1. **Posicionar en el eje Y:** Coloca la posición en **Y** a **0**.
2. **Posicionar en el eje X:** Modifica la posición en el eje **X**. Por ejemplo, ponla en **X = 8** o una posición similar que se ajuste a lo que buscas. Estas paredes deben estar fuera de la vista, en los bordes de la pantalla.

Una vez colocada, ajusta la posición en **X** a **9.5** para que quede en el lugar adecuado.

### 2. Crear la Segunda Pared

Para crear la segunda pared:

1. **Duplicar el objeto:** Duplicamos la pared que ya hemos creado.
2. **Colocarla en el lado contrario:** Coloca la segunda pared en el lado opuesto, simplemente poniendo un valor negativo en el **X** (por ejemplo, **X = -9.5**). Esto pondrá la pared en el otro lado de la pantalla.

### Comportamiento de las Paredes
Estas paredes laterales deben ser diferentes a las paredes superior e inferior en cuanto a **colisiones**. No deben hacer que la pelota rebote. En lugar de eso, deben funcionar como las **porterías** de un jugador o del otro, lo que significa que cuando la pelota colisione con estas paredes, se añadirá un **punto** a un jugador.

## 07. Nombrando los objetos

Es importante nombrar las cosas porque vamos a empezar a tener muchos ``objetos`` y nos podemos confundir. Además, deberemos poder identificarlos en los ``scripts`` que crearemos para manipularlos.

Para renombrar un objeto hacéis doble clic o con ``F2``. La portería derecha vamos a llamarle en ``goal1`` porque va a ser la portería en la que tiene que colar el jugador 1 que va a estar a nuestra izquierda.

## 08. Creando los jugadores

Vamos a crear los ``players``. entonces vamos a hacer control de sobre ese amigo aquí de la derecha lo voy a arrastrar a esta posición que de hecho lo vamos a poner en la posición 8 y ahora hay que reducir la escala. Así imaginaros que vuestro ``player`` es así de grande en 3 cuando venga la bola va a rebotar sí o sí, al ser demasiado grande.

### Crear ``jugador2``

Vamos a reducirlo unpoco a lo que sería en el eje y a 2.5 luego pues podemos modificar elmovimiento de la velocidad de la bolapodemos modificar muchas cosas pues paraque se adapte a lo que cada uno puesesté buscando en este caso como está ala derecha pues lo llamaremos player2.

### Crear jugador 1

Duplicamos el jugador con ``Ctrl``+``D`` y lo llevamos a la posición contraria

# Pelota

Ahora lo único que ayudaría sería pues nuestra ``pelota`` del medio así que podemos hacer directamente clic derecho dentro de nuestro ``Unity`` su día dietsprite square y si la colocamos en el 0,0.

Para poder diferenciar lo mejor vamos a cambiarle el color y esto lo podéis hacer con todos los objetos

## 09. Componentes Rigid Body

``Rigid Body 2D`` es un componente de ``Unity`` que se utiliza para añadir físicas a un objeto 2D. Un ``Rigid Body 2D`` le permite a un objeto 2D ser afectados por:

- La gravedad
- El empuje
- La fricción
- Otras fuerzas físicas.

Esto permite a los desarrolladores añadir realismo y jugabilidad a los juegos 2D.

Asignaremos los componentes ``Rigidbody 2D``  a nuestros jugadores y a la pelota. Podemos seleccionar todos los objetos y seleccionar el componente ``Rigidbody 2D``  para añadirlo.

### Modificar gravedad

Al dar a ``play`` los objetos con Rigidbody caerán, pues sobre ellos actúa la gravedad. Para quitarles el efecto de la gravedad, donde pone gravity podemos ponerlo a 0 y así ya no se caerán.

![](2023-03-02-13-03-45.png)

Los ``rigidbodies`` son componentes que añadiremos a nuestros ``players`` y para nuestra ``pelota`` y se encargarán del tema de física para el movimiento.

- Vamos a seleccionar nuestro ``player`` y nuestra ``bola``.
- A continuación seleccionamos todos en el componente ``Rigid Body 2D`` y ahí le añadimos.

Si dejamos esto así tal cual cuando yo le diera el ``play`` vais a ver qué los elementos caen. Esto es porque tienen física y por tanto, les afecta la gravedad. En nuestro caso esto no lo queremos.

Lo que tenemos que hacer es dentro de nuestro componente ``Rigid Body 2D``  donde pone ``gravity`` es que a uno vamos a ponerlo a 0 y así ya no se caerán.

## 10. Ordenar objetos

tra cosa que modificando que a lo mejor les ocurre es que la línea del centro se está dibujando por encima de nuestra pelota yeso pues la verdad que no queda muy buena lo mejor sí a lo mejor lo queréis vale pues lo dejáis lo dejáis así si os gusta pues lo dejáis pero si no lo que podéis hacer es se detiene al puesto al bola

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos11.png)

En el elemento ``sprite renderer`` podemos cambiar el orden. Esto sirve para diferenciar la altura a la que se dibujan las diferentes elementos dentro de nuestra pantalla porque ahora mismo son todo imágenes entonces para saber diferenciar cuál está por delante de una de otra utilizamos el orden y léger\. __

__Podemos poner un 2 ya se dibuja por encima así que así no habrá problema\.__

La ``línea del centro`` se está dibujando por encima de nuestra ``pelota``.

Para modificarlo, seleccionamos el objeto ``bola`` y en el elemento ``Sprite Renderer`` en el ``orden`` ponemos un número más alto. Esto sirve para diferenciar la altura a la que se dibujan las diferentes elementos dentro de nuestra pantalla. Ahora la ``bola`` se dibuja por encima.

## 11. Movimiento de personajes

Ahora vamos a pasar directamente a lo que sería el tema de los movimientos de nuestros personajes. Vamos a hacerlo con:

- Teclas ``w`` y ``s`` para el ``jugador1`` (izquierda)
- Teclas flecha de arriba y hacia abajo para el ``jugador2`` (derecha)

De este modo, podremos jugar 2 jugadores en el mismo teclado.

# CONTROLES

Los ``controles`` son las teclas que utilizaremos para las diferentes acciones durante el juego.

## Redefinir controles

Para redefinir los controles, vamos a ir a ``Edit > Project Settings > Input Manager``. Aquí vemos que hay varias cosas declaradas, como ``Axes``. Estos son los controles que ``Unity`` tiene asignados por defecto para las teclas de nuestro teclado.

![input manager](2023-03-02-13-06-37.png)

Por ejemplo, para el eje **horizontal**, está asignado a las teclas de flechas o el número 'A' para izquierda y derecha.

![](2023-03-02-13-08-14.png)

Para el eje **vertical**, está asignado a las teclas de W, A, S y D, y las flechas de arriba y abajo. Así que si queremos cambiar estos controles, podemos hacerlo en el Input Manager.

![](2023-03-02-13-08-35.png)

## Controles para segundo jugador

Tenemos que crear el elemento ``vertical2`` que es para nuestro ``player2``. Tenemos que diferenciar pues que uno utilice el WS y el otro utilice la flecha hacia arriba y hacia abajo. Lo tenemos que diferenciar entonces lo que vamos a hacer es del vertical vamos a borrar el SW que tenemos aquí. Vamos a duplicarlo para tener un vertical2 para nuestro jugador 2; clic
`derecho duplicate element y se duplicará que vendrá por aquí otra como ``vertical`` y lo llamamos ``vertical2``.
`
Lo que faltaría es cambiarle los controles del player1 juega con la flecha de arriba y hacia abajo. Nosotros con el jugador 2 jugaremos con la W y S. En negativo ponemos S y en positivo W. Dentro del objeto player, en función de si es el 1 o el 2, seleccionaremos el control oportuno.

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos14.png)

## Dentro de los scripts, podemos acceder a los diferentes controles por su nombre

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos15.png)

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos16.png)

# SCRIPTS

## 13. Script de programación

Los ``scripts`` son pequeños programas que controlan el comportamiento de los objetos y la dinámica del juego en ``Unity``.

Estos se crean utilizando el ``lenguaje C#``  y se guardan en archivos con extensión ``.cs``. Para editarlos se utiliza Visual Studio Code, y se guardan dentro de la carpeta ``assets``.

Dentro dela carpeta ``assets`` vamos a hacer clic ``derecho > new folder`` que vamos a llamar ``scripts`` y así tendremos guardados todos nuestros programas en esta carpeta. Para crear un ``script``, hacemos clic derecho en la carpeta y elegimos la opción ``create C# script``.

![](2023-02-21-09-46-09.png)

Ahora vamos a pasar a crear nuestro script vamos aquí a entrar a la carpeta que acabamos de crear y vamos a hacer ``clic derecho > create C# script``. A este script le vamos a llamar ``Player.cs``. Podríamos abrirlo y vamos a utilizar el programa visual studio.

![](2023-02-21-09-46-50.png)

### Estructura de un script

Los scripts en ``Unity`` tienen una estructura básica compuesta por dos partes principales: la parte de declaración de variables, y las funciones.

La parte de **declaración de variables** es donde se definen los campos, variables y propiedades que se usarán en el script.

La segunda parte es la **sección de funciones**, donde se escribe el código que controla el comportamiento de objetos en el juego.

- La función ``Start()`` se llama al comienzo del juego (una vez) y generalmente se usa para inicializar variables y configurar el estado inicial del objeto.
- La función ``Update()`` se llama una vez por frame y se usa para actualizar el estado del objeto.

Además de estas dos funciones, podemos crear todas las funciones que queramos para controlar el comportamiento de un objeto, desde eventos de entrada (como cuando un usuario presiona una tecla) hasta eventos de salida (como cuando un objeto sale del juego). Estas funciones se pueden llamar en el script para ejecutar el código deseado.

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }
}
```

### Errores de programación

Los errores de programación más comunes en ``Unity`` son errores de sintaxis. Estos se producen cuando el programador escribe algo de forma incorrecta, por ejemplo, olvidarse de poner ; al final de las líneas o cerrar un \}, o escribiendo mal mayúsculas o minúsculas.

Si hay errores de sintaxis, ``Unity`` no podrá ejecutar el juego correctamente, por lo que el programador debe solucionar los errores antes de poder continuar.

Algunas de las formas más comunes de solucionar estos errores son comprobar el código con cuidado, revisar la documentación para asegurarse de que está escribiendo cada línea correctamente

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos27.png)

### Crear script players

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Players : MonoBehaviour
{

    public bool player1;
    public float speed = 3;
    public Rigidbody2D rb;

    private float move;
    private Vector2 startPos;

    void Start()
    {
        startPos = transform.position;
    }
    void Update()
    {
        if(player1)
        {
            move = Input.GetAxisRaw("Vertical");
        }

        else
        {
            move = Input.GetAxisRaw("Vertical2");
        }

        rb.velocity = new Vector2(rb.velocity.x, move*speed );
    }
    public void Reset()
    {
        rb.velocity = Vector2.zero;
        transform.position = startPos;
    }
}
```

## 14. Asignar script al jugador

Para que un script tenga efecto, hay que ``asignar`` el script a uno o más objetos. Para ello los scripts se arrastran y sueltan sobre los objetos que queremos que los utilicen.

Cada vez que volvamos a ``Unity`` después de modificar nuestros scripts, se recargará el proyecto para incluir los cambios.

En el caso de haber errores de programación, deberemos primero subsanarlos.

Una vez terminado, podemos asignar el script ``player.cs`` a los objetos ``player1`` y ``player2``, arrastrándolos y soltándolos sobre estos objetos.

## Cambiar el booleano para player2

![](2023-02-21-11-25-50.png)

## Asignar rigidbody al script

![](2023-02-21-11-26-35.png)

## Crear método reset en el script

![](2023-02-21-11-28-04.png)

## Crear script para la pelota

Crearemos un script para la pelota al que llamaremos ``ball.cs``.

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Goal : MonoBehaviour
{
    public bool player1Goal;
    public GameObject gameManager;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.CompareTag("Ball"))
        {

            if (player1Goal)
            {
                gameManager.GetComponent<GameManager>().Player1Scored();
            }

            else
            {
                gameManager.GetComponent<GameManager>().Player2Scored();
            }
        }
    }
}
```

## Asignar script a la bola

## Asignar el rigibody

![](2023-02-21-11-36-16.png)

## Crear material para la pelota

![](2023-02-21-11-36-57.png)

![](2023-02-21-11-37-23.png)

## Restringir movimientos en los players

Solo queremos que los jugadores se muevan en un eje, por lo que restringimos los otros dos.

![](2023-02-21-11-38-12.png)

## Reorganizar archivos

![](2023-02-21-11-45-01.png)

## Crear interfaz puntuación

Crearemos las puntuaciones. Al crear una UI, este objeto se nos pondrá dentro de una carpeta ``canvas``.

![](2023-02-21-11-46-04.png)

## Cambiar posición

![](2023-02-21-11-47-30.png)

Una vez creado el texto y colocado, lo duplicaremos para tener dos objetos texto, a los que modificaremos el nombre y se llamarán ``Player1Text`` y ``Player2Text``.

## Cambiar pelota y hacerla redonda

En el ``Sprite Renderer`` tenéis que cambiar la propiedad ``Sprite`` por un círculo.

## Crear el script del juego

Crearemos un ``script`` que llamaremos ``GameManager`` (veréis que cambia el icono por un engranaje).

Borraremos los métodos ``start()`` y ``update()``.

Crearemos los métodos ``Player1Scored()`` y ``Player1Scored()``.

Al marcar un gol:

1. La pelota vuelve al centro
2. Las palas vuelven a su posición iniciar
3. Cambiamos los valores del marcador

``ResetPosition()`` será un método que resteará los objetos.

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public GameObject bola;
    public GameObject player1;
    public GameObject player1goal1;
    public GameObject player2;
    public GameObject player2goal2;

    public Text player1Text;
    public Text player2Text;

    private int player1Score;
    private int player2Score;

    public bool IAGame;

    public int maxScore = 7;

    public void CheckVictory()
    {
        if(player1Score >= maxScore){
            SceneManager.LoadScene("VictoryPlayer1");
        }

        if(player2Score >= maxScore){
            SceneManager.LoadScene("VictoryPlayer2");
        }
    }

    public void Player1Scored()
    {
        player1Score``;
        player1Text.text = player1Score.ToString();
        CheckVictory();
        ResetPosition();
    }

    public void Player2Scored()
    {
        player2Score``;
        player2Text.text = player2Score.ToString();
        CheckVictory();
        ResetPosition();
    }

    private void ResetPosition()
    {
        if (IAGame)
        {
            bola.GetComponent<Ball>().Reset();;
            player2.GetComponent<Players>().Reset();
        }
        else
        {
            bola.GetComponent<Ball>().Reset();;
            player2.GetComponent<Players>().Reset();
            player1.GetComponent<Players>().Reset();
        }
    }
}
```

## Añadir las referencias a objetos

Arrastraremos todos los objetos a las propiedades del script ``GameManager``.

## Marcar trigger en las porterías

Necesitamos marcar la opción ``is Trigger`` del componente ``Box Collider 2D``.

## Crear script para las porterías

Creamos un script llamado ``Goal.cs``.  Utilizaremos el método ``OnTriggerEnter2D()`` para detectar colisión entre la pelota y alguna de las porterías.

``CompareTag`` comprobará si el objeto que colisiona es la bola y, en caso de ser así, según si colisiona con ``Goal1`` o con ``Goal2`` cambiaremos la puntuación correspondiente.

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Goal : MonoBehaviour
{
    public bool player1Goal;
    public GameObject gameManager;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.CompareTag("Ball"))
        {

            if (player1Goal)
            {
                gameManager.GetComponent<GameManager>().Player1Scored();
            }

            else
            {
                gameManager.GetComponent<GameManager>().Player2Scored();
            }
        }
    }
}
```

## Asignar scripts

Vamos a asignar el script creado a ``Goal1`` y a ``Goal2`` y marcamos en ``Goal1`` el check player1goal.

## Asignar etiqueta a la bola

Necesitamos asignar el ``tag`` que llamaremos ``ball`` al objeto pelota, seleccionando en ``Tag`` y ``Add Tag``.

## Crear referencias

Nos hemos dejado crear referencias en el script ``Goal.cs``. Una vez lo hayamos hecho, arrastramos ``GameManager`` a las referencias.

## Cambiar colores

Utilizar la página ``coolors`` para elegir paletas.

![w:300px](img/2023-03-08-18-37-06.png)

## Inteligencia artificial

Vamos a hacer que un jugador sea controlado por la máquina. Para ello, debemos crear un programa que siga las instrucciones propias de la IA y simular las acciones de un jugador.

Crear el script ``IA.cs`` y la completamos.

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IA : MonoBehaviour
{
    public float speed=3;
    public GameObject ball;
    private Vector2 ballPos;

    void Update()
    {
        Move();
    }

    void Move() {
        ballPos = ball.transform.position;

        if (transform.position.y > ballPos.y)
        {
            transform.position += new Vector3(0, -speed*Time.deltaTime);
        }

        if (transform.position.y < ballPos.y)
        {
            transform.position += new Vector3(0, speed*Time.deltaTime);
        }
    }
}
```

Una vez completado el script, necesitamos asignarloo a un objeto.

Asignamos el script ``IA.cs`` a ``Player1`` y desamarcamos el checkbox del scripts ``Players`` para que no interfiera.

Arrastramos la referencia de ``Bola`` al script.

Crear variable en ``GameManager`` para decidir si el juego es PvP o PvsPC. Será un booleano. En ``ResetPosition()`` miraremos este valor para decidir resetear o no.

Seleccionar el objeto ``GameManager``  y marcar la opción ``IA Game``.

# ESCENAS

- Un juego suele estar compuesto de múltiples escenas
- Cada escena tiene sus propios ``objetos``.

Nuestro juego tendrá 3 escenas:

| Nombre         | Función             |
| -------------- | ------------------- |
| PlasyerVSIA    | Juego contra la IA  |
| PlayerVSPlayer | Modo de 2 jugadores |
| Mainmenu       | Menú principal      |

 Ahora solo tenemos la escena ``Main``. Le vamos a cambiar el nombre para diferenciarla y la vamos a a llamar ``PlayerVSIA`` para diferenciarla.

La duplicamos y a la copia le llamamos ``PlayerVSPlayer``. En esta escena, desmarcamos el check de ``IA Game``.

Creamos una escena 2D nueva yendo a ``File > New scene > 2D``.

Las escenas deberán estar todas dentro de la carpeta ``Scenes``. Haciendo clic en cada una de ellas, podremos abrirlas y modificarlas

![](img/2023-02-22-18-31-45.png)

## Crear botones

Para movernos entre escenas utilizaremos botones. Existe un objeto ``button`` para ello.
Para crear el botón, deberemos hacer clic derecho en ``Hierarchy`` y ``Create > UI > Button``.

El botón se hará grande o pequeño según la resolución y el aspect ratio. Si queremos fijar su tamaño, haremos lo siguiente.

Iremos al objeto ``Canvas`` en el que se ha creado el botón y en el componente ``Canvas Scaler`` vamos a la propiedad ``UI Scale Mode`` y elegimos ``Scale With Screen Size``.

Duplicamos el botón y le colocamos el texto ``Player VS Player``. Lo movemos y lo situamos.

### Colocar texto con nombre del juego

Pondremos un texto y le cambiaremos el texto por **PONG**, y lo haremos más grande. Para evitar problemas al hacerlo grande o pequeño, vamos al ``inspector`` y buscamos en paragraph las opciones ``horizontal overflow`` y ``vertical overflow`` y les asignamos el valor ``overflow``.

Lo hacemos grande y lo situamos.

Guardamos la escena (que ahora se llama ``Untitled*``) con **Ctrl + S**  y le llamaremos ``MainMenu``.

### Crear script MainMenu.cs

A continuación programaremos el comportamiento del menú principal. Para ello, crearemos un script nuevo llamado ``MainMenu.cs``.

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            Application.Quit();
        }
    }

    public void PlayerVSIA(){
        SceneManager.LoadScene("PlayerVSIA");
    }

    public void PlayerVSPlayer(){
        SceneManager.LoadScene("PlayerVSPlayer");
    }
}
```

### Asignar script al canvas

Tendremos que asignar el script ``MainMenu.cs`` al ``canvas`` de la escena del menú, arrastrándo el ``script`` y soltando encima de ``canvas``.

Seleccionamos ``PlayerVSPlayer``.

![](img/2023-02-22-18-35-22.png)

Por último tendremos que arrastrar ``canvas`` a las referencias de los dos botones.

![](img/2023-02-22-18-35-48.png)

Cambiamos el ``onclick`` para que llame a las funciones correspondientes. Elegimos la función ``MainMenu > PlayerVSPlayer``:

![](img/2023-02-22-18-36-27.png)

### Modificación de build settings

Los ``Build Settings`` permiten a los desarrolladores configurar y compilar proyectos de Unity para distintas plataformas de destino. Tenemos que agregar las escenas que formarán parte en el juego en el orden correcto.

Para agregar escenas, sigue estos pasos:

1. Ve al menú ``File`` (Archivo) y selecciona ``Build Settings`` (Configuración de compilación).
2. En la ventana ``Build Settings``, verás una lista de escenas. En la parte inferior deberemos colocar las escenas que van a formar parte de nuestra ``build``.

![](img/2023-02-22-18-38-41.png)

### Comprobación

Comprobaremos que ejecutando el juego, podemos pasar del menú a cada una de las dos escenas siguientes.
