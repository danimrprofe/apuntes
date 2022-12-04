![](img/Gestion%20de%20imagenes%20de%20disco0.png)

## Montaje y mantenimiento de sistemas y componentes informáticos

_Implantación de sistemas operativos_

## Gestión de imágenes de disco

## Introducción

* ¿Por qué no simplemente arrastrar y soltar?
  * Tener cuidado al hacer copias
  * Se puede hacer para datos que no sean del sistema operativo
  * __NO__  se puede arrastrar y soltar un sistema operativo\.
  * Si es la unidad desde la que se inicia\, sólo la clonación o la creación de imágenes pueden confeccionar una copia de trabajo de forma fiable\.

![](img/Gestion%20de%20imagenes%20de%20disco1.jpg)

![](img/Gestion%20de%20imagenes%20de%20disco2.jpg)

## Gestión de imágenes de disco

* Imagen de un disco
  * El producto de hacer una copia\, sector por sector
  * De un soporte de almacenamiento \(HDD\, CD\, DVD\, pendrive\, etc\.\)
  * Puede hacerse
    * De un disco completo
    * De una partición en concreto
* La imagen se puede crear de 2 maneras:
  * __Cloning__
  * __Imaging__

![](img/Gestion%20de%20imagenes%20de%20disco3.jpg)

* Clonación de un disco a otro disco
  * Copia el contenido completo de una unidad a otra
    * Archivos\, tablas de particiones y MBR
  * Para mover los datos de un disco a otro
  * Solución más fácil y rápida
  * __Funcionamiento__
    * Se conecta una nueva unidad al equipo
    * Se inicia el software y se clona todo el disco en ella
    * Una vez clonado\, funciona directamente sin ningún programa
    * Se sustituye un disco o partición por el clon
  * Se utiliza fundamentalmente para  _despliegues_

![](img/Gestion%20de%20imagenes%20de%20disco4.jpg)

* Creación de una imagen a partir del disco \(Imaging\)
  * A partir de  __unidad o partición __ de un HD\, DVD\, pendrive\, etc\.
  * Copia todos los datos  _a un solo archivo: _  __imagen de disco \(ISO\)__
  * Guardado en otra unidad
* Imagen de disco
  * __Contiene los datos__ \, estructura e información del disco
  * Se puede  __restaurar la imagen__
    * En la unidad existente
    * En otra nueva
  * Se utiliza fundamentalmente como  _copia de seguridad_ \.
  * Necesita de un programa para poderse utilizar

![](img/Gestion%20de%20imagenes%20de%20disco5.png)

* ¿Para qué se usan las imágenes de un disco?
  * __Copia de seguridad__
    * Se hace una imagen\, utilizando el procedimiento de  _Imaging_
    * Disponer de ella si el disco original sufriera algún problema\.
  * __Clonación para despliegues__
    * La creación imagen mediante  _cloning_  \(clonación\)
    * Replicar en otros PC de forma directa \(tantas veces como deseemos\)
    * Se utiliza cuando se necesita:
      * Replicar el estado de un equipo \(con configuraciones\, programas\, etc\.\)
      * A otros PC\, sobre todo cuando el número de equipos es elevado\.
    * Despliegue = procedimiento de instalar la imagen original en otros equipos\.

## Software para la gestión de imágenes de disco

* Se pueden utilizar diferentes programas para la gestión de imágenes\, en función del soporte que se quiera replicar\.
* Imágenes de  _discos ópticos_
  * Las imágenes de discos ópticos se puede realizar con una amplia gama de software
    * Gratuito \(ImgBurn\, CDBurnerXP\, ISODisk\, etc\.\)
    * De pago \(CloneDVD\. PowerlSO\, Nero\, Alcohol 120 %\. etc\.\)\.
  * El formato más extendido para este tipo de imágenes es ISO\.
  * Cada aplicación suele tener además un formato propio
* Imágenes de  _discos duros_
  * Hay programas dedicados a este tipo de imágenes\, como  __ODIN__  o  __Clonezilla__  \(gratuitos\)
  * Lo habitual es que también gestionen las copias de seguridad de los discos
    * Acronis True Image\, Redo Backup & Recovery o Paragon Hard Disk Manager\.
* Imágenes de  _dispositivos de almacenamiento extraíble_
  * Tarjetas de memoria y discos USB
  * Pueden ser tratados como discos duros u ópticos\, según finalidad

![](img/Gestion%20de%20imagenes%20de%20disco6.png)

## Clonación de un disco

* Problemas al clonar un disco con SO
  * __Equipos con diferente hardware que el original__
    * Algunos SO no están preparados para cambios en el hardware
    * Pueden dar problema con los controladores\.
  * __Problemas de seguridad__
    * Cada equipo Windows basado en arquitectura NT tiene un número único que lo identifica llamado  __SID__  \(Security IDentificator\. identificador de seguridad\)\.
    * A partir de ese número se generan SIDs para usuarios\, de acuerdo con los cuales el sistema organiza los permisos\, el control de accesos\, etc\.
    * La réplica limpia del disco conllevaría una réplica en los SID\.
    * Puede originar graves problemas de seguridad al interconectar los equipos\.

![](img/Gestion%20de%20imagenes%20de%20disco7.png)

![](img/Gestion%20de%20imagenes%20de%20disco8.jpg)

* Herramienta  __Sysprep \(Windows\)__
  * Prepara el sistema para ser clonado
  * Convierte el disco en un dispositivo autoinstalable
  * La primera vez que se inicia nos obliga a pasar por los mismos pasos de la segunda fase de una instalación limpia del sistema\.
* Instalación desatendida
  * Se puede utilizar un  __archivo de respuesta __ junto con Sysprep
  * Indica al asistente los valores con los que debe completarse de forma totalmente  __desatendida__ \.

![](img/Gestion%20de%20imagenes%20de%20disco9.jpg)

![](img/Gestion%20de%20imagenes%20de%20disco10.jpg)

![](img/Gestion%20de%20imagenes%20de%20disco11.png)

* Despliegue de la réplica
  * Debemos obtener espacio en el disco destino para poder alojar el archivo de réplica\.
  * El despliegue de réplicas de disco con SO requiere activar la partición donde hemos colocado la imagen\.
  * Una vez hecho eso\, con iniciar el equipo se procederá a la «instalación» de la imagen en el disco\.
  * En función de si hemos diseñado un archivo de respuesta o no\, tendremos que terminar la configuración del equipo destino\.

## Clonezilla

![](img/Gestion%20de%20imagenes%20de%20disco12.png)

* Clonezilla
  * Es una herramienta  _Open Source _ \(software distribuido y desarrollado libremente\)
  * Nos permite hacer copias de seguridad y restauración\.
* 2 versiones de Clonezilla
  * __Clonezilla Live__
    * Adecuado para realizar copias de seguridad y de restauración de 1 máquina\.
  * __Clonezilla SE \(Server Edition\)__
    * Se utiliza para el despliegue masivo
    * Puede clonar muchos ordenadores \(40 o más\) al mismo tiempo\.
* Algunas características de Clonezilla son:
  * Es  __software libre \(GPL\)__
  * Muchos sistemas de archivos compatibles
  * Se puede hacer todo a través de  __comandos__  y opciones\.
  * Parámetros de arranque para  __personalizar__  la imagen y clonación
  * Clonezilla SE pueden clonar  __masivamente__  muchos ordenadores\.
  * Se puede utilizar  __remotamente__
  * El archivo de imagen puede ser un  _disco local\, un servidor SSH\, samba o NFS\._

![](img/Gestion%20de%20imagenes%20de%20disco13.gif)

![](img/Gestion%20de%20imagenes%20de%20disco14.png)

## Clonación DISCO a IMAGEN y viceversa

* Creación de la imagen
  * Crear una MV con Windows 7 de 15 GB llamada  __Win7__
  * Agregar un segundo disco duro de 15 GB llamado  __Disco backup__
  * Cargar imagen de Clonezilla
  * Inicializar el disco desde Windows 7 y dar formato al segundo disco
  * Reiniciar MV
  * Crear imagen a partir del disco
* Restaurar imagen a disco
  * Apagar la MV  __Win7 __
  * Crear una segunda MV llamada  __Win7 2 __ idéntica a la primera
  * Agregar el disco duro  __Disco backup__
  * Cargar la imagen del Clonezilla
  * Restaurar imagen al disco duro principal
  * Reiniciar MV y comprobar que funciona bien

* Posibilidades
  * Disco a disco
  * Partición a partición
* Necesitaremos
  * Conectar un segundo dispositivo de almacenamiento \(disco externo o pendrive\)
  * Tiene que tener suficiente espacio
* Posibilidades
  * Guardar la imagen creada como copia de seguridad
  * Aprovechar la imagen para copiarla en otros discos y clonar\.

## Clonación remota

* Clonación disco a disco a través de red
  * Las máquinas tienen que “verse” \(misma red\)\.
  * Adjudicación de IP estática o mediante DHCP

![](img/Gestion%20de%20imagenes%20de%20disco15.png)

![](img/Gestion%20de%20imagenes%20de%20disco16.png)

![](img/Gestion%20de%20imagenes%20de%20disco17.png)

* Clonación disco a disco a través de red
  * Tiempo clonación: 12 minutos aprox\. \(Disco SSD\)

![](img/Gestion%20de%20imagenes%20de%20disco18.png)

![](img/Gestion%20de%20imagenes%20de%20disco19.png)

## Clonación de 1 PC a varios PC (Multicast)

![](img/Gestion%20de%20imagenes%20de%20disco20.png)

* Clonación de una imagen a varios PC
  * En primer lugar\, creamos una imagen de un disco \(image to device\)
  * En Virtualbox\, crear una  __red NAT__
  * Configurar todas las MV como  __red NAT __ para que cada una de ellas tenga su propia IP
* __En __ el Servidor
  * Dentro de Clonezilla\, seleccionar Lite server
  * Configurar DHCP y decir cuantos PC vamos a clonar
  * Se quedará a la espera de la conexión
* En las MV cliente
  * Entrar en modo Shell y ejecutar el comando que nos da el servidor al final
  * Introducir la IP del servidor y esperar

![](img/Gestion%20de%20imagenes%20de%20disco21.png)

![](img/Gestion%20de%20imagenes%20de%20disco22.png)

![](img/Gestion%20de%20imagenes%20de%20disco23.png)

