## Discos, particiones y sistemas de archivos

## Estructura física del disco duro

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria1.jpg)

* Estructura física del disco
  * Un disco duro puede contar con uno o varios  __discos__ \.
  * Cada disco suele contar con dos  __caras__ \.
  * Cada cara es leída por un  __cabeza de lectura/escritura__
  * Un disco tiene tantas  __cabezas__  como caras
  * Cada una de las caras se divide en anillos llamados  __pistas__ \.
  * La misma pista de cada una de las cabezas se llama  __cilindro__ \.
  * Cada pista se divide en  __sectores__ \.
* Sectores
  * Un  __sector__  es el trozo más pequeño que se puede leer o escribir
  * En cada sector se almacenan 512 Bytes de información\. \(En SSD 4\-16 KB\)
  * La agrupación de varios sectores se denomina  __clúster__ \.
* Para localizar la información en un disco
  * __Identificación:__  Cabeza \- Cilindro \- Sector
  * Las cabezas y los cilindros se comienzan a numerar desde el «0» y los sectores desde el «1»\, así que el primer bloque de información estará situado en la posición «0\-0\-1»\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria2.jpg)

Cabeza – Cilindro – Sector

Primer bloque:  __0 \- 0 \- 1__

## Estructura lógica del disco duro

* MBR
  * Es el  __primer sector __ de cualquier disco duro
  * En él se almacenan
    * La  __tabla de particiones__
    * Un programa de inicialización del sistema \( __bootstrap__  __\)__
  * Los más conocidos son:
    * _NTLDR:_  para sistemas Windows modernos
    * _LILO y GRUB_ : para sistemas Linux
    * _PXE_ : para arranque a través de un entorno de red\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria3.jpg)

* __Espacio particionado: __
  * Espacio que ya se ha asignado para almacenar datos o programas
* __Espacio no asignado: __
  * Zona no accesible del disco a la que todavía no se le ha asignado un fin\.
  * No contiene datos ni programas de ningún tipo\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria4.png)

## Partición de discos

* Unidades físicas y lógicas
  * Cada disco duro constituye una  __unidad física__
  * Cada unidad física puede contener una o más  __unidades lógicas__ \, denominadas  _particiones_ \.
* Tabla de particiones
  * Contiene el registro de las particiones de un disco
  * Está en el sector  __MBR__
  * Se indica cuál es la  __partición activa __ del disco\.
    * A la que se dirige el bootstrap para iniciar el arranque del sistema\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria5.gif)

## Tipos de particiones

* Partición  _primaria_
  * División simple del disco destinada\, a contener SO \(aunque también puede contener datos\)
  * __Máximo 4 __ particiones primarias en un disco
  * A cada una se asigna una  __letra__  de unidad \(G\, D:\. etc\.\)
  * Pueden tener asociado un nombre que permite identificarlas más rápidamente \( __etiqueta__ \)\.
  * La partición primaria puede ser una partición  __activa__ \.
* Partición  _extendida_
  * Destinada exclusivamente a ser contenedor de particiones llamadas lógicas\.
  * Máximo una en un mismo disco\.
  * Las particiones extendidas  _no tienen letra de unidad_
* Partición  _lógica_
  * Es una subdivisión de la partición extendida\.
  * Pueden existir  __varias particiones lógicas__  dentro de la misma  __partición extendida__ \.
  * Al igual que a las primarias\, se les asigna una letra de unidad\.
  * Las particiones lógicas no pueden ser particiones activas\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria6.gif)

## Ejemplos de particiones

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria7.jpg)

Esquema lógico con particiones primarias

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria8.jpg)

Esquema lógico con una partición extendida

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria9.jpg)

Esquema lógico con particiones lógicas en la partición extendida

## Sistema de archivos

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
  * Alojada en los primeros sectores del disco\, con una copia de su contenido por si la primera se daña\.
  * Formato muy popular \(disquetes\, tarjetas de memoria y dispositivos similares\)
  * Produce bastante  __fragmentación__  en el disco
  * __Limitaciones__
    * No permite particiones  _superiores a los 32 GB _
    * No permite archivos  _mayores de 4 GB\._
* Tipos de FAT
  * Existen  __3__  modalidades de FAT

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria10.png)

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria11.png)

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

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria12.png)

__Mac OS X __ sólo puede leer las unidades NTFS\, no escribirlas\.

__Linux__  Algunas distribuciones pueden habilitar el soporte de escritura NTFS\, pero algunas pueden ser de sólo lectura\.

__PlayStation__  Ninguna de las consolas PlayStation de Sony admite NTFS\.

__Xbox 360__  no puede leer las unidades NTFS\, Xbox One puede

* Sistema de archivos extendido  <span style="color:#FF0000">EXT</span>
  * Sistema característico de los entornos  __Linux__
  * __Incompatible__  con entornos Windows\.
  * Diferentes versiones:
    * Ext2\, ext3 y ext4
    * Cada versión incluye mejoras sobre la anterior\.
  * La versión más moderna \( __ext4__ \) es capaz de
    * Archivos <  __16 TB __
    * Particiones <  __1 EB __ \(exabyte\)
  * Linux utiliza un espacio en el disco denominado  __swap__ \, mediante el cual puede guardar información que no se mantiene en memoria\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria13.jpg)

## Operaciones sobre particiones

__Creación de particiones primarias__

__ __ Se requiere espacio libre: no asignado\.

__ __ La capacidad depende del espacio del disco y de la ubicación y tamaño de otras\.

Si va a contener un sistema operativo debe estar en los primeros 2 GB del disco\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria14.jpg)

__Creación de particiones lógicas__

__ __ Solamente si van a albergar particiones extendidas\.

No hay límite para la creación de particiones lógicas en una primaria\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria15.jpg)

__Redimensión y desplazamiento de particiones__

__ __ Debe existir espacio disponible en los extremos\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria16.jpg)

__Uso de espacio no asignado__

__ __ Solo se puede asignar espacio a particiones localizadas en el mismo disco\.

__Fusión de particiones__

Las dos particiones deben estar una junto a otra\.

Las dos particiones deben tener sistemas de archivos compatibles entre sí\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria17.jpg)

__Copia de particiones__

__ __ Genera una partición con el mismo tamaño\, sistema de archivos y contenido que la partición original\.

Pueden copiarse particiones en varios discos\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria18.jpg)

__Eliminación y recuperación de particiones__

Eliminar una partición destruye los datos sobrescribiendo los sectores del disco\.

La recuperación no siempre puede llevarse a cabo\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria19.jpg)

* Cambiar el sistema de archivos de una partición
  * Conversión de particiones: modificación de un sistema de archivos a otro\.
  * Conversión entre  __FAT y NTFS __ tiene sus problemas
    * Se permite el cambio con limitaciones \(espacio en disco\, persistencia de los datos\)
  * Conversión sistemas  Windows y Linux es más compleja
  * Si la aplicación lo permite\, el cambio del sistema de archivos se realizaría mediante la opción de convertir\, pudiendo realizar la conversión entre FAT y NTFS\. pero no entre particiones ext\.
* Cambiar el tipo de partición
  * Existe la posibilidad de  _convertir una partición _  _primaria_  _ en _  _lógica_  y viceversa\.
  * Este cambio es bastante útil cuando se agota el cupo de cuatro particiones primarias en el disco

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria20.jpg)

## Formateo de una partición

* Formateo de particiones
  * Proceso de preparar un dispositivo de almacenamiento para un uso inicial\.
  * Formatear no implica borrar los datos\, aunque no sean visibles
  * Se puede formatear un disco completo o una partición
  * __Dos niveles de formateo__
    * Alto nivel \(lógico\)
    * Bajo nivel \(físico\)

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria21.jpg)

* Formateo  _alto nivel \(formateo lógico\)_
  * Borra solo tabla de acceso a los archivos almacenados \(no los datos\)
  * Similar a  __borrar el índice de un libro__ \.
  * Se emplea para asignar el  __sistema de archivos __ a la partición
  * Incluye  __comprobación de errores __ \(físicos o magnéticos\) en el disco\.
  * Dependiendo de la  __configuración__ \, el proceso durará más o menos\.
  * Tener en cuenta
    * No se puede interrumpir la acción de formateo
    * Cuando haya terminado no habrá acceso a los datos antiguos\.
    * Sin embargo\, estos  <span style="color:#FF0000"> __datos no se borran__ </span>
    * Existen herramientas software con las que  __pueden recuperarse__ \.
* _¿Desde dónde puedo formatear?_
  * Desde el  __sistema operativo __
    * Solo en otros discos distintos al que contiene el SO
  * Desde un  __disco de arranque __ \(a todos los discos del equipo\)
    * Mediante cualquiera de las  __aplicaciones de gestión de discos__ \.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria22.jpg)

* Formateo a  _bajo nivel \(o formateo físico\)_
  * __Elimina: __  _particiones de disco \+ datos \+ tablas de archivos_
  * Se vuelve a los valores iniciales de  __fábrica__ \.
  * Coloca  __marcas__  en la superficie del disco para dividirlo de nuevo en pistas y sectores\, eliminando las antiguas referencias\.
  * Este tipo de formateo proporciona más  __seguridad__
  * Recuperación de la información  _difícil pero _ también es  _posible_
  * Solo elimina las marcas divisorias del disco\, no los datos
  * Formateo  __muy lento__
  * En caso de interrumpirse el disco puede quedar inutilizable
* Herramientas
  * Fabricantes de discos
    * Ofrecen gratis herramientas para aplicar este tipo de formateo\.
  * Herramientas genéricas
    * _HDD Low _  _Level_  _ Format Tool _ \(gratuita\)
    * _KillDisk_  \(de pago\)\.

![](img%5CDiscos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria23.jpg)

