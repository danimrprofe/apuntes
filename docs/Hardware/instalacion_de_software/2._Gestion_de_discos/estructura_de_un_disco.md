# Estructura de un disco

## Estructura física del disco duro

![](img/Discos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria1.jpg)

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
  * Las cabezas y los cilindros se comienzan a numerar desde el «0» y los sectores desde el «1», así que el primer bloque de información estará situado en la posición «0\-0\-1»\.

![](img/Discos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria2.jpg)

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

![](img/Discos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria3.jpg)

* __Espacio particionado: __
  * Espacio que ya se ha asignado para almacenar datos o programas
* __Espacio no asignado: __
  * Zona no accesible del disco a la que todavía no se le ha asignado un fin\.
  * No contiene datos ni programas de ningún tipo\.

![](img/Discos%2C%20particiones%20y%20sistemas%20de%20archivo%20-%20teoria4.png)




