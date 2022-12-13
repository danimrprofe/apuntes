# Sistema de archivos

* El sistema de archivos
  * __Estructura__  que utiliza una partición de un disco para almacenar en ella los datos\.
  * __Formatear:__  Proceso de asignar un sistema de archivos a una partición
  * Al formatear una partición se puede optar por un determinado sistema de archivos\.
* ¿Por qué es tan importante?
  * El SO que queramos instalar influye a la hora de elegir el tipo de sistema de archivos
  * Algunos SO se pueden instalar en varios tipos de sistemas de archivos y viceversa
* Para elegir el sistema de archivos
  * Deberemos tener en cuenta
    * El  __SO__  con el que trabajemos\.
    * Las limitaciones en cuanto al  __tamaño de archivos __
    * Las  __compatibilidades__

* Sistema de archivos  <span style="color:#FF0000">FAT</span>
  * Desarrollados para Windows pero  _compatibles con entornos Linux_ \.
  * Crean una  __tabla de asignación __ de archivos \(File Allocation Table\)
  * Alojada en los primeros sectores del disco, con una copia de su contenido por si la primera se daña\.
  * Formato muy popular \(disquetes, tarjetas de memoria y dispositivos similares\)
  * Produce bastante  __fragmentación__  en el disco
  * __Limitaciones__
    * No permite particiones  _superiores a los 32 GB _
    * No permite archivos  _mayores de 4 GB\._
* Tipos de FAT
  * Existen  __3__  modalidades de FAT

![](img/Discos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria10.png)

![](img/Discos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria11.png)

* Sistema de archivos  <span style="color:#FF0000">NTFS</span>
  * Diseñado para versiones modernas de Windows \(NT \- Windows 8\.1\)
  * Soluciona limitaciones de FAT
  * Compatible con entornos Linux \(ahora\)
  * Dispone de un registro de transacciones \( __journaling__ \)
    * Anotan las acciones realizadas sobre la escritura de un archivo
    * Se utiliza para restaurarse en caso de fallo
  * __Límite:__  Particiones < 256 TB \(recomendado < 2 TB\)
* Inconveniente
  * Necesita  __mucho espacio en disco __ para gestión de los archivos\.
  * No recomendable para discos o particiones < 10 GB\.

![](img/Discos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria12.png)

__Mac OS X __ sólo puede leer las unidades NTFS, no escribirlas\.

__Linux__  Algunas distribuciones pueden habilitar el soporte de escritura NTFS, pero algunas pueden ser de sólo lectura\.

__PlayStation__  Ninguna de las consolas PlayStation de Sony admite NTFS\.

__Xbox 360__  no puede leer las unidades NTFS, Xbox One puede

* Sistema de archivos extendido  <span style="color:#FF0000">EXT</span>
  * Sistema característico de los entornos  __Linux__
  * __Incompatible__  con entornos Windows\.
  * Diferentes versiones:
    * Ext2, ext3 y ext4
    * Cada versión incluye mejoras sobre la anterior\.
  * La versión más moderna \( __ext4__ \) es capaz de
    * Archivos <  __16 TB __
    * Particiones <  __1 EB __ \(exabyte\)
  * Linux utiliza un espacio en el disco denominado  __swap__ , mediante el cual puede guardar información que no se mantiene en memoria\.

![](img/Discos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria13.jpg)
