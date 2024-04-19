# Sistema de archivos

El ``sistema de archivos`` es una estructura que utiliza una partición de un disco para almacenar en ella los datos.

El proceso de asignar un sistema de archivos a una partición se conoce como ``formatear``.Al formatear una partición se puede optar por un determinado sistema de archivos.

La elección del sistema de archivos es un paso crítico a la hora de instalar un sistema operativo, ya que el SO que queramos instalar influye a la hora de elegir el tipo de sistema de archivos. Algunos SO se pueden instalar en varios tipos de sistemas de archivos y viceversa.

Para elegir el sistema de archivos deberemos tener en cuenta el sistema operativo con el que trabajemos, las limitaciones en cuanto al tamaño de archivos y las compatibilidades.

## FAT

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

![imagen](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria10.png)

![imagen](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria11.png)

## NTFS

El Sistema de archivos ``NTFS`` fue creado para mejorar las limitaciones de FAT. Está diseñado para ser compatible con entornos Linux y Windows (NT - Windows 8.1). Esto permite a los usuarios compartir archivos entre ambos sistemas operativos.

El sistema de archivos ``NTFS`` posee un registro de transacciones (``journaling``) que anota todas las acciones realizadas sobre la escritura de un archivo. Esto permite que el sistema se auto restaure en caso de fallo.

El límite de particiones es de 256 TB, aunque se recomienda el uso de particiones inferiores a 2 TB. El sistema de archivos ``NTFS`` necesita de una gran cantidad de espacio en disco para organizar los archivos. Por ello, no es recomendable usar particiones o discos inferiores a 10 GB.

### NTFS 6.0

Es la versión de NTFS que se implementó por primera vez en Windows Vista.

- Admite RAID 5.
- Admite compresión de archivos.
- Admite ``EFS`` (cifrado de archivos). Es un sistema de cifrado de archivos integrado en Microsoft Windows que cifra los datos en un disco para protegerlos de acceso no autorizado.
- Admite junctions, reparse points y hardlinks.

## EXT

El Sistema de Archivos Extendido (``EXT``) es un sistema característico de los entornos Linux, que resulta incompatible con entornos Windows.

Existen diferentes versiones del mismo, como ``Ext2``, ``Ext3`` y ``Ext4``, siendo cada una de ellas una mejora de la anterior. La versión más moderna, ``Ext4``, es capaz de manejar archivos de hasta 16 TB y particiones de hasta 1 EB (exabyte). Además, ``Linux`` utiliza un espacio en el disco denominado Swap, mediante el cual puede guardar información que no se mantiene en memoria.

![imagen](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria13.jpg)

## Sistemas de archivos actuales

``Windows 10`` utiliza el sistema de archivos NTFS (New Technology File System). Es un sistema de archivos que ofrece muchas mejoras con respecto al sistema FAT32, incluyendo mayor compatibilidad, mejor seguridad y mayor velocidad. Además, NTFS también ofrece soporte para archivos de gran tamaño y cantidades más grandes de memoria.

``Android`` utiliza el sistema de archivos ext4 para sistemas de 32 bits, y el sistema de archivos F2FS para sistemas de 64 bits.