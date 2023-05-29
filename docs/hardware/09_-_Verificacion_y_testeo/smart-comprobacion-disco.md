# Comprobación del estado físico del disco

* Problemas:
  * Uso intensivo, Manejo inadecuado, Accidente
* Consecuencia:
  * Acorta vida del disco y ocasiona fallos
  * Necesidad de comprobar anomalías físicas en disco

![imagen](img/5_Herramientas_de_comprobaci%C3%B3n_y_optimizaci%C3%B3n_de_soportes_de_info0.jpg)

## S.M.A.R.T

``S.M.A.R.T.`` es una tecnología avanzada que permite a los usuarios detectar fallos en la superficie del disco duro antes de que esto produzca una pérdida de datos irrecuperable.

Esta tecnología tiene que ser compatible con el BIOS, y debe estar activada y soportada por el disco duro para que funcione correctamente.

Esto permite al usuario realizar una copia de su contenido y reemplazar el disco antes de que resulte en una pérdida de datos significativa.

![imagen](img/5_Herramientas_de_comprobaci%C3%B3n_y_optimizaci%C3%B3n_de_soportes_de_info1.jpg)

\* Self Monitoring Analysis and Reporting Technology

* Cuando  <span style="color:#FFC000">se produce un error </span> detectable
  * BIOS avisa \(mensaje pantalla\)
  * Indica tipo de error producido
  * En este momento: copia de seguridad o reparación
* No detecta todos los errores
* Capaz de detectar mayoría de fallos de degradación

![imagen](img/5_Herramientas_de_comprobaci%C3%B3n_y_optimizaci%C3%B3n_de_soportes_de_info2.jpg)

## Tipos de fallos

Los fallos en un disco duro se pueden clasificar en dos tipos: impredecibles y predecibles.

- Los ``fallos impredecibles`` se producen por sobre voltajes, temperaturas de funcionamiento elevadas, mal funcionamiento de la controladora de interfaz o mala conexión.
- Por el contrario, los ``fallos predecibles`` son causados por el deterioro de la parte mecánica del disco, y representan el 60% del total de fallos.

Los valores de los atributos S.M.A.R.T. van del número 1 al 253, siendo 1 el peor valor y los valores normales se encuentran entre 100 y 200. Estos valores se almacenan en un espacio reservado del disco duro.

## Parámetros característicos

- Temperatura del disco: el aumento de la temperatura a menudo es señal de problemas de motor del disco\.
- Velocidad de lectura de datos: reducción en la tasa de transferencia de la unidad puede ser señal diversos problemas internos\.
- Tiempo de partida \(spin\-up\): cambios en el tiempo de partida pueden reflejar problemas con el motor del disco\.
- Contador de sectores reasignados: la unidad reasigna muchos sectores internos debido a los errores detectados, esto puede significar que la unidad va a fallar definitivamente\.
- Velocidad de búsqueda \(seek time\)\.
- Altura de vuelo del cabezal: la tendencia a la baja en altura de vuelo a menudo presagian un accidente del cabezal\.

Uso de error\-correcting code \(ECC\) y conteo de errores: el número de errores detectados por la unidad, aunque se corrijan internamente, a menudo señala problemas con el desarrollo de la unidad\. La tendencia es, en algunos casos, más importante que el conteo real\.

La herramienta Self Monitoring Analysis and Reporting Technology (SMART) es un sistema de monitoreo de discos duros que permite verificar el estado físico de los mismos.

Esta tecnología es suministrada por los fabricantes de discos duros, como Seagate con su herramienta ``Seatools``, y también existen herramientas de terceros como ``HD Inspector`` y ``HD Tune``, que brindan información avanzada como temperatura, tiempo de funcionamiento, etc. Estas herramientas son útiles para garantizar la salud de los discos duros.

![imagen](img/5_Herramientas_de_comprobaci%C3%B3n_y_optimizaci%C3%B3n_de_soportes_de_info3.jpg)

![imagen](img/5_Herramientas_de_comprobaci%C3%B3n_y_optimizaci%C3%B3n_de_soportes_de_info4.png)

![imagen](img/5_Herramientas_de_comprobaci%C3%B3n_y_optimizaci%C3%B3n_de_soportes_de_info5.png)

## SMART en BIOS

![imagen](img/5_Herramientas_de_comprobaci%C3%B3n_y_optimizaci%C3%B3n_de_soportes_de_info6.jpg)

## Herramientas de comprobación y optimización de soportes de información

![imagen](img/5_Herramientas_de_comprobaci%C3%B3n_y_optimizaci%C3%B3n_de_soportes_de_info16.png)
