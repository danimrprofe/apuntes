# Gestión de entrada / salida

## Introducción

La gestión de entrada/salida es muy importante para un sistema operativo. Existe una amplia variedad de dispositivos que se conectan a los ordenadores, tales como teclado, disco duro, monitor, impresoras, etc.

## Hardware de E/S

Estos dispositivos se clasifican en **almacenamiento**, **comunicaciones** e **interfaz** de usuario, y se comunican con el ordenador a través de señales de cables o aire.

Los dispositivos se conectan al PC a través de los **puertos**. Un conjunto común de cables conectando múltiples dispositivos se conoce como un **bus**.

Los dispositivos están formados por un dispositivo físico, una tarjeta controladora, una interfaz entre el ordenador y el dispositivo, componentes, sincronización, conversores AD y DA, registros y protocolos de comunicación.

## Proceso genérico E/S

El sistema operativo escribe un comando en el registro de la tarjeta controladora, la cual junto con el dispositivo ejecutan el comando. Mientras tanto, el sistema operativo y la CPU siguen con la ejecución de otros procesos.

Cuando el comando finaliza, el controlador genera una interrupción que el sistema operativo recibe. La CPU atiende la interrupción en función de la prioridad. Los datos leídos se colocan en los registros de la tarjeta para que el sistema operativo los lea.

## Comunicación con el dispositivo

A través de registros

Se asocian una serie de registros a cada puerto

Entrada / salida mapeada a memoria

Parte del espacio de direcciones del procesador se mapea al dispositivo

Se escribe y lee directamente en esas areas

Interesante para dispositivos que mueven grandes cantidades de datos,
como gráficos

Es necesario proteger los spacios de memoria entre procesos

## Tipos de dispositivos según el acceso al sistema

Existen dos tipos de dispositivos según el acceso al sistema: dispositivos de bloque y dispositivos de carácter.

## Tipos de E/S en función de la sincronización del controlador

También se pueden clasificar en función de la sincronización del controlador: E/S programada, E/S por interrupciones, acceso directo a memoria y DMA.

El acceso directo a memoria es ineficiente para los periféricos que generan grandes cantidades de datos.

El acceso por **DMA** permite que la tarjeta controladora realice las transferencias de datos cuando el bus está libre y una vez que se han enviado los datos, genera una interrupción que el sistema operativo atiende.

## Técnicas para gestionar E/S y salidas

Las técnicas de gestión de E/S y salidas son fundamentales para mejorar el rendimiento de los sistemas informáticos.

Una de las técnicas más comunes es el **Buffering**. Esta técnica se usa para almacenar temporalmente los datos en la memoria RAM, para reducir el tiempo de acceso a los dispositivos de E/S.

El **Spooling** es otra técnica de gestión de E/S. Utiliza una memoria intermedia para almacenar datos antes de que se procesen. Esto permite a los dispositivos de E/S trabajar de forma independiente y permite a los usuarios realizar otras tareas mientras se procesan los datos.

Por último, la **Cache** es un almacén temporal de datos que se almacena en la memoria RAM con el objetivo de mejorar el rendimiento. La información se almacena en la memoria RAM, lo que permite a los sistemas informáticos acceder a los datos más rápidamente. Estas tres técnicas juntas mejoran la eficiencia de los sistemas informáticos, permitiendo una mejor gestión de E/S y salidas.

## Software de E/S##

El gestor de E/S forma parte del sistema operativo y permite la gestión de los distintos periféricos. El objetivo del gestor es lograr la independencia de procesos E/S, gestionar los errores, controlar los dispositivos compatibles y dedicados, estructurarse en niveles, permitir la E/S en espacio de usuario y manejar los dispositivos de forma independiente.

## Objetivos##

## Independencia de procesos E/S##

## Gestión de errores##

## Manejo de dispositivos compatibles y dedicados##

## Gestor se estructura en niveles##

## E/S en espacio de usuario##

Funciones de biblioteca de programación que permiten realizar acciones
de E/S

Programas completos fuera del núcleo: sistema de spooling de impresora

## E/S independiente de dispositivo##

## Manejadores de dispositivo

Como ejemplo de un elemento de E/S, podemos nombrar a los **manejadores de dispositivo**, los cuales permiten el acceso directo a los dispositivos y ayudan a controlar la transferencia de los datos.

## Manejadores de interrupciones

Los manejadores de interrupciones son los encargados de manejar las interrupciones generadas por los dispositivos en el sistema, mientras que los estancamientos permiten la detección y solución de los problemas con los dispositivos de E/S.

## Estancamientos##

## Ejemplo de elemento de E/S##
