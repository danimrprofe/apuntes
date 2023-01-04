# Scripts

## Programación de scripts

Los scripts son pequeños programas que controlan el comportamiento de los objetos y la dinámica del juego en Unity. Estos se crean utilizando el lenguaje C##  y se guardan en archivos con extensión .CS. Para editarlos se utiliza Visual Studio Code, y se guardan dentro de la carpeta "assets". Dentro de esta carpeta, creamos una nueva carpeta llamada "scripts", donde se guardarán todos nuestros programas. Para crear un script, hacemos clic derecho en la carpeta y elegimos la opción "create C##  script".s

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos18.png)

## Asignar scripts a objetos

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos19.png)

__Para que un script tenga efecto\, hay que __  __asociarlo __  __a uno o más objetos\.__

__Para ello l__  __os scripts se arrastran y sueltan sobre los objetos que queremos que los utilicen\.__

__Cada vez que volvamos a Unity después de modificar nuestros scripts\, se recargará el proyecto para incluir los cambios\.__

__En el caso de haber errores de programación\, deberemos primero subsanarlos\.__

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos20.png)

## Variables

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos22.png)

__Las __  <span style="color:## 9900FF"> __variables __ </span>  __creadas son accesibles desde fuera del programa para cambiar parámetros__

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos23.png)

## Estructura de scripts

Los scripts en Unity tienen una estructura básica compuesta por dos partes principales: la parte de declaración de variables, y las funciones.

La parte de **declaración de variables** es donde se definen los campos, variables y propiedades que se usarán en el script.

La segunda parte es la **sección de funciones**, donde se escribe el código que controla el comportamiento de objetos en el juego.

* La función ``Start()`` se llama al comienzo del juego (una vez) y generalmente se usa para inicializar variables y configurar el estado inicial del objeto.
* La función ``Update() ``se llama una vez por frame y se usa para actualizar el estado del objeto.

Además de estas dos funciones, podemos crear todas las funciones que queramos para controlar el comportamiento de un objeto, desde eventos de entrada (como cuando un usuario presiona una tecla) hasta eventos de salida (como cuando un objeto sale del juego). Estas funciones se pueden llamar en el script para ejecutar el código deseado.

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos25.png)

## Errores en programación

Los errores de programación más comunes en Unity son errores de sintaxis. Estos se producen cuando el programador escribe algo de forma incorrecta, por ejemplo, olvidarse de poner ; al final de las líneas o cerrar un \}, o escribiendo mal mayúsculas o minúsculas.

Si hay errores de sintaxis, Unity no podrá ejecutar el juego correctamente, por lo que el programador debe solucionar los errores antes de poder continuar.

Algunas de las formas más comunes de solucionar estos errores son comprobar el código con cuidado, revisar la documentación para asegurarse de que está escribiendo cada línea correctamente

![](img%5CTaller%20de%20creaci%C3%B3n%20de%20videojuegos27.png)
