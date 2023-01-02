# Particiones

* Unidades físicas y lógicas
  * Cada disco duro constituye una  __unidad física__
  * Cada unidad física puede contener una o más  __unidades lógicas__ , denominadas  _particiones_ \.
* Tabla de particiones
  * Contiene el registro de las particiones de un disco
  * Está en el sector  __MBR__
  * Se indica cuál es la  __partición activa __ del disco\.
    * A la que se dirige el bootstrap para iniciar el arranque del sistema\.

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria5.gif)

## Tipos de particiones

* Partición  _primaria_
  * División simple del disco destinada, a contener SO \(aunque también puede contener datos\)
  * __Máximo 4 __ particiones primarias en un disco
  * A cada una se asigna una  __letra__  de unidad \(G, D:\. etc\.\)
  * Pueden tener asociado un nombre que permite identificarlas más rápidamente \( __etiqueta__ \)\.
  * La partición primaria puede ser una partición  __activa__ \.
* Partición  _extendida_
  * Destinada exclusivamente a ser contenedor de particiones llamadas lógicas\.
  * Máximo una en un mismo disco\.
  * Las particiones extendidas  _no tienen letra de unidad_
* Partición  _lógica_
  * Es una subdivisión de la partición extendida\.
  * Pueden existir  __varias particiones lógicas__  dentro de la misma  __partición extendida__ \.
  * Al igual que a las primarias, se les asigna una letra de unidad\.
  * Las particiones lógicas no pueden ser particiones activas\.

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria6.gif)

## Ejemplos de particiones

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria7.jpg)

Esquema lógico con particiones primarias

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria8.jpg)

Esquema lógico con una partición extendida

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria9.jpg)

Esquema lógico con particiones lógicas en la partición extendida