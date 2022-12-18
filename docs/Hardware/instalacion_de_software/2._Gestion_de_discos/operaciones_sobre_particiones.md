# Operaciones sobre particiones

__Creación de particiones primarias__

__ __ Se requiere espacio libre: no asignado\.

__ __ La capacidad depende del espacio del disco y de la ubicación y tamaño de otras\.

Si va a contener un sistema operativo debe estar en los primeros 2 GB del disco\.

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria14.jpg)

__Creación de particiones lógicas__

__ __ Solamente si van a albergar particiones extendidas\.

No hay límite para la creación de particiones lógicas en una primaria\.

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria15.jpg)

__Redimensión y desplazamiento de particiones__

__ __ Debe existir espacio disponible en los extremos\.

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria16.jpg)

__Uso de espacio no asignado__

__ __ Solo se puede asignar espacio a particiones localizadas en el mismo disco\.

__Fusión de particiones__

Las dos particiones deben estar una junto a otra\.

Las dos particiones deben tener sistemas de archivos compatibles entre sí\.

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria17.jpg)

__Copia de particiones__

__ __ Genera una partición con el mismo tamaño, sistema de archivos y contenido que la partición original\.

Pueden copiarse particiones en varios discos\.

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria18.jpg)

__Eliminación y recuperación de particiones__

Eliminar una partición destruye los datos sobrescribiendo los sectores del disco\.

La recuperación no siempre puede llevarse a cabo\.

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria19.jpg)

* Cambiar el sistema de archivos de una partición
  * Conversión de particiones: modificación de un sistema de archivos a otro\.
  * Conversión entre  __FAT y NTFS __ tiene sus problemas
    * Se permite el cambio con limitaciones \(espacio en disco, persistencia de los datos\)
  * Conversión sistemas  Windows y Linux es más compleja
  * Si la aplicación lo permite, el cambio del sistema de archivos se realizaría mediante la opción de convertir, pudiendo realizar la conversión entre FAT y NTFS\. pero no entre particiones ext\.
* Cambiar el tipo de partición
  * Existe la posibilidad de  _convertir una partición _  _primaria_  _ en _  _lógica_  y viceversa\.
  * Este cambio es bastante útil cuando se agota el cupo de cuatro particiones primarias en el disco

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria20.jpg)

## Formateo de una partición

* Formateo de particiones
  * Proceso de preparar un dispositivo de almacenamiento para un uso inicial\.
  * Formatear no implica borrar los datos, aunque no sean visibles
  * Se puede formatear un disco completo o una partición
  * __Dos niveles de formateo__
    * Alto nivel \(lógico\)
    * Bajo nivel \(físico\)

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria21.jpg)

* Formateo  _alto nivel \(formateo lógico\)_
  * Borra solo tabla de acceso a los archivos almacenados \(no los datos\)
  * Similar a  __borrar el índice de un libro__ \.
  * Se emplea para asignar el  __sistema de archivos __ a la partición
  * Incluye  __comprobación de errores __ \(físicos o magnéticos\) en el disco\.
  * Dependiendo de la  __configuración__ , el proceso durará más o menos\.
  * Tener en cuenta
    * No se puede interrumpir la acción de formateo
    * Cuando haya terminado no habrá acceso a los datos antiguos\.
    * Sin embargo, estos  <span style="color:#FF0000"> __datos no se borran__ </span>
    * Existen herramientas software con las que  __pueden recuperarse__ \.
* _¿Desde dónde puedo formatear?_
  * Desde el  __sistema operativo __
    * Solo en otros discos distintos al que contiene el SO
  * Desde un  __disco de arranque __ \(a todos los discos del equipo\)
    * Mediante cualquiera de las  __aplicaciones de gestión de discos__ \.

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria22.jpg)

* Formateo a  _bajo nivel \(o formateo físico\)_
  * __Elimina: __  _particiones de disco \+ datos \+ tablas de archivos_
  * Se vuelve a los valores iniciales de  __fábrica__ \.
  * Coloca  __marcas__  en la superficie del disco para dividirlo de nuevo en pistas y sectores, eliminando las antiguas referencias\.
  * Este tipo de formateo proporciona más  __seguridad__
  * Recuperación de la información  _difícil pero _ también es  _posible_
  * Solo elimina las marcas divisorias del disco, no los datos
  * Formateo  __muy lento__
  * En caso de interrumpirse el disco puede quedar inutilizable
* Herramientas
  * Fabricantes de discos
    * Ofrecen gratis herramientas para aplicar este tipo de formateo\.
  * Herramientas genéricas
    * _HDD Low _  _Level_  _ Format Tool _ \(gratuita\)
    * _KillDisk_  \(de pago\)\.

![](img/Discos%2C_particiones_y_sistemas_de_archivo_-_teoria23.jpg)
