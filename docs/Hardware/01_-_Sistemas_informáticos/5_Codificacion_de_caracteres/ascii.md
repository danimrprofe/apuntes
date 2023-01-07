## Código ASCII

Ascii fue creado en 1963, y es una correspondencia entre cadenas de bits y una serie de símbolos (alfanuméricos y otros).

Esto permite comunicación entre dispositivos digitales, así como procesar y almacenar la información.

Caracteres:

![imagen](img/5_Codificacion_de_caracteres4.png)

Ejemplo:

![imagen](img/5_Codificacion_de_caracteres5.png)

* Representaba caracteres utilizando __ 7 bits __
* 128 caracteres posibles, enumerados del 0 al 127
  * _Códigos 0 al 31 _
    * Se denominan  _caracteres de control_
    * Tienen efecto sobre cómo se procesa el texto\.
  * _Códigos 65 al 90 _
    * Representan las letras  _mayúsculas_
  * _Códigos 97 al 122 _
    * Representan las letras  _minúsculas_

![imagen](img/5_Codificacion_de_caracteres6.png)

![imagen](img/5_Codificacion_de_caracteres7.png)

![imagen](img/5_Codificacion_de_caracteres8.png)

![imagen](img/5_Codificacion_de_caracteres9.jpg)

![imagen](img/5_Codificacion_de_caracteres10.jpg)

## Código ASCII Extendido

Los problemas con el ASCII original eran que fue desarrollado para utilizarse con inglés y no poseía caracteres acentuados o caracteres específicos de otros idiomas, por lo que para codificar estos caracteres se necesitaba un sistema de códigos distinto.

La solución fue la extensión del código ASCII para 8 bits (byte) y la codificación de hasta 256 caracteres (ASCII extendido).  Esto permitió añadir caracteres acentuados, símbolos y otras letras de idiomas distintos al inglés.

Sin embargo, el ASCII extendido sigue siendo limitado y no soporta caracteres complejos como los usados en el **chino o el japonés**, para los cuales se usan otros sistemas de codificación.

![imagen](img/5_Codificacion_de_caracteres11.jpg)

* Este código asigna los valores del  __0 al 255 __ para las mayúsculas, las minúsculas, los dígitos, las marcas de puntuación y otros símbolos\.
* _Compatibilidad con ASCII_
* Para no romper la compatibilidad con ASCII, se hace que el primer bit signifique
  * 0: Los 7 bits inferiores siguen la tabla ASCII
  * 1: Los 7 bits inferiores siguen otra tabla
* _Caracteres ASCII extendido_
  * Caracteres alfabéticos no ingleses
  * Símbolos de moneda no ingleses
  * Letras griegas
  * Símbolos matemáticos
  * Caracteres para gráficos
  * Caracteres para gráficos de barras
  * Caracteres sombreados

![imagen](img/5_Codificacion_de_caracteres12.png)

![imagen](img/5_Codificacion_de_caracteres13.png)
