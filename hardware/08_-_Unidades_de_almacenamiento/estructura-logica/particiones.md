# Particiones

Cada disco duro es una unidad física que puede contener una o más ``unidades lógicas`` denominadas ``particiones``. Para llevar un control de estas particiones, se encuentra en el sector ``MBR`` (Master Boot Record) una tabla con los registros de las particiones de un disco llamada ``tabla de particiones``.

Esta tabla también indica cuál es la ``partición activa`` del disco, la cual es a la que se dirige el bootstrap para iniciar el arranque del sistema.

![imagen](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria5.gif)

## Tipos de particiones

### Partición primaria
  * División simple del disco destinada, a contener SO \(aunque también puede contener datos\)
  * __Máximo 4 __ particiones primarias en un disco
  * A cada una se asigna una  __letra__  de unidad \(G, D:\. etc\.\)
  * Pueden tener asociado un nombre que permite identificarlas más rápidamente \( __etiqueta__ \)\.
  * La partición primaria puede ser una partición  __activa__ \.
### Partición  _extendida_

  * Destinada exclusivamente a ser contenedor de particiones llamadas lógicas\.
  * Máximo una en un mismo disco\.
  * Las particiones extendidas  _no tienen letra de unidad_

### Partición  _lógica

Las ``particiones lógicas`` son una subdivisión de la partición extendida, en la que se pueden crear varias particiones lógicas al interior de la misma.

Se les asigna una letra de unidad al igual que a las particiones primarias, pero no se pueden usar como particiones activas.

![imagen](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria6.gif)

## Ejemplos de particiones

![imagen](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria7.jpg)

Esquema lógico con particiones primarias

![imagen](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria8.jpg)

Esquema lógico con una partición extendida

![imagen](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria9.jpg)

Esquema lógico con particiones lógicas en la partición extendida