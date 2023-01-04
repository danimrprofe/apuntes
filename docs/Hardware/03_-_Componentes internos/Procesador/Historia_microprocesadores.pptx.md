# MICROPROCESADORES

UNIDAD CENTRAL DE PROCESOS\)

Un poco de historia

![imagen](img/Historia_microprocesadores5.png)

![imagen](img/Historia_microprocesadores6.gif)

![imagen](img/Historia_microprocesadores7.gif)

![imagen](img/Historia_microprocesadores8.jpg)

## ¿QUE ES EL MICROPROCESADOR?

  Un microprocesador es el     _cerebro_     del ordenador.

  Es un chip, un conjunto de circuitos electrónicos altamente integrado, fabricado en un trozo de silicio.  En su interior existen millones de elementos llamados transistores, ordenados de manera que forman puertas lógicas para poder así, hacer operaciones de toda clase.

  L    os microprocesadores van sobre un elemento llamado socket o zócalo, que se conecta a la placa base.

  La función de los microprocesadores es la de ejecutar e interpretar las instrucciones     de los ordenadores    .

![imagen](img/Historia_microprocesadores9.png)

![imagen](img/Historia_microprocesadores10.jpg)



 La velocidad de un microprocesador se mide en mega hertzios \(MHz\) o giga hertzios \(1 GHz = 1.000 MHz\). Debido a la extrema dificultad de fabricar componentes electrónicos que funcionen a las inmensas velocidades de MHz habituales hoy en día, todos los microprocesadores modernos tienen 2 velocidades:

![imagen](img/Historia_microprocesadores11.png)

VELOCIDAD INTERNA:

 La velocidad a la que funciona el microprocesador internamente \(1.8, 2.1, 2.3... GHz\).

![imagen](img/Historia_microprocesadores12.png)

VELOCIDAD EXTERNA O DEL BUS:

 La velocidad a la que se comunican el micro y la placa base, típicamente a 1033, 2066…     MHz.

![imagen](img/Historia_microprocesadores13.jpg)

2. PARTES BÁSICAS DE UN MICROPROCESADOR

![imagen](img/Historia_microprocesadores14.png)

2.1   <span style="color:#5A83E0"> UC \(Unidad de Control\)   :

Organiza el funcionamiento de la CPU, decidiendo

qué se hace \(y quién\) en cada momento.

2.2   <span style="color:#5A83E0"> ALU \(Unidad Aritmético\-Lógica\)   <span style="color:#5A83E0"> _ _   :

Realiza las operaciones que convierten los datos de

entrada en resultados.

2.3   El Coprocesador Matemático   :

o, más correctamente, la FPU \(Unidad de coma Flotante\). Parte del microprocesador especializada cálculos matemáticos complejos.

### 2.4. Registros:

Posiciones de memoria interna que almacenan temporal y momentáneamente los datos que pasan por la CPU, estados, direcciones…  mientras  se necesitan.

### 2.5. La Memoria Cache

Una memoria intermedia ultrarrápida que sirve al microprocesador para tener a mano ciertos datos que previsiblemente serán utilizados en las siguientes operaciones sin tener que acudir a la memoria RAM, reduciendo el tiempo de espera.

Es lo que se conoce como caché de primer nivel; es decir, la que está más cerca del microprocesador, tanto que está encapsulada junto a él, también llamada caché interna.

![imagen](img/Historia_microprocesadores15.jpg)

## 2. PARTES BÁSICAS DE UN MICROPROCESADOR

![imagen](img/Historia_microprocesadores16.png)

Bus de Direcciones:

Transporta las direcciones de los datos manejados por la CPU

![imagen](img/Historia_microprocesadores17.png)

Bus de Datos Externos:

Transporta hacia y desde el exterior de la PCU \(cache L2, chipset, RAM…\).  También se le denomina bus frontal o bus del sistema.

![imagen](img/Historia_microprocesadores18.png)

Bus de Datos Internos:

Transporta los datos dentro de la CPU, es decir entre registros, cache L1, etc.

![imagen](img/Historia_microprocesadores19.png)

Marca la frecuencia del funcionamiento del microprocesador y los distintos buses del sistema.

![imagen](img/Historia_microprocesadores20.jpg)

3. PARTES ELEMENTALES  DE UN MICROPROCESADOR

![imagen](img/Historia_microprocesadores21.png)

![imagen](img/Historia_microprocesadores22.jpg)

![imagen](img/Historia_microprocesadores23.png)

ESQUEMA DE LOS MICROPROCESADORES

![imagen](img/Historia_microprocesadores24.png)

![imagen](img/Historia_microprocesadores25.jpg)

ESQUEMA DE LA UNIDAD ARITMÉTICO – LÓGICA \(UAL\)

![imagen](img/Historia_microprocesadores26.png)

![imagen](img/Historia_microprocesadores27.jpg)

![imagen](img/Historia_microprocesadores28.png)

ESQUEMA DE LA UNIDAD ARITMÉTICO – LÓGICA \(UAL\)

![imagen](img/Historia_microprocesadores29.png)

* _Componentes de la ALU_
  * Registros de entrada \(A, B\):
    * Almacenan los operandos \(datos de entrada\).
  * Circuito operacional:
    * Componentes electrónicos que realizan las operaciones.
  * Registro acumulador \(R\):
    * Almacena el resultado de las operaciones.
  * Registros de estado \(D\):
    * “Flags” que recogen cómo termina la operación.
      * Cero, negativo, acarreo, desbordamiento, paridad, etc...
  * Selector de operaciones \(F\):
    * Microinstrucciones procedentes de la Unidad de Control.

ESQUEMA DE LA UNIDAD DE CONTROL  \(UC\)

![imagen](img/Historia_microprocesadores30.png)

![imagen](img/Historia_microprocesadores31.png)

![imagen](img/Historia_microprocesadores32.png)

![imagen](img/Historia_microprocesadores33.png)

UNIDAD DE CONTROL  \(UC\)

* _Componentes de la UC_
  * Contador de programa
    * Contiene la dirección de memoria de la siguiente instrucción.
  * Registro de instrucciones
    * Contiene la instrucción que se está ejecutando.
  * Decodificador
    * Interpreta la instrucción en curso, para poder ejecutarla.
  * Reloj
    * Genera impulsos eléctricos que sincronizan y marcan la velocidad a la que trabaja la CPU.
  * Secuenciador
    * Genera las microinstrucciones para la ejecución paso a paso de la instrucción interpretada por el decodificador.

![imagen](img/Historia_microprocesadores34.jpg)

![imagen](img/Historia_microprocesadores35.png)

UNIDAD DE CONTROL  \(UC\)

  * <span style="color:#002060"> _Interpreta_   <span style="color:#002060"> las instrucciones almacenadas en la memoria y   <span style="color:#002060"> _genera_   <span style="color:#002060"> las   <span style="color:#002060"> _señales de control_   <span style="color:#002060"> necesarias para ejecutarlas.
  * <span style="color:#002060">Activa o desactiva los componentes del microprocesador en función de:
    * <span style="color:#002060">La   <span style="color:#002060"> _instrucción_   <span style="color:#002060"> que se esté ejecutando.
    * <span style="color:#002060">La   <span style="color:#002060"> _fase_   <span style="color:#002060"> de dicha instrucción que se esté ejecutando.
  * <span style="color:#002060">Existen dos tipos de unidades de control:
    * <span style="color:#002060">Cableadas \(máquinas sencillas\).
    * <span style="color:#002060">Microprogramadas  <span style="color:#002060"> \(máquinas complejas\).

![imagen](img/Historia_microprocesadores36.png)

![imagen](img/Historia_microprocesadores37.png)

![imagen](img/Historia_microprocesadores38.jpg)

![imagen](img/Historia_microprocesadores39.png)

EJECUCIÓN DE UNA INSTRUCCIÓN

![imagen](img/Historia_microprocesadores40.png)

  * Se recibe la instrucción desde la UC.
  * Se comprueba el estado de la ALU.
  * Se cargan los operandos.
  * Se realiza la operación.
  * Se guarda el resultado en el acumulador.
  * Se guarda el estado de la ALU al final.

![imagen](img/Historia_microprocesadores41.png)

  * Búsqueda de la instrucción \( fetch \).
  * Decodificación de la instrucción \( decode \) y carga de operandos \( load \).
  * Ejecución de las operaciones \( execute \).
  * Escritura de resultados \( store \).

![imagen](img/Historia_microprocesadores42.png)

![imagen](img/Historia_microprocesadores43.jpg)

4. TIPOS DE DISEÑO DE LOS MICROPROCESADORES

Computación con una colección de instrucciones reducida\): se basan en la idea de que la mayoría de las instrucciones para realizar procesos en el computador son relativamente simples por lo que se minimiza el número de instrucciones y su complejidad a la hora de diseñar la CPU. Estos procesadores se suelen emplear en aplicaciones industriales y profesionales por su gran rendimiento y fiabilidad. Compañías    Compaq  , Motorola y   PowerPC

Computación con una colección de instrucciones compleja\): al contrario, tienen una gran cantidad de instrucciones y por tanto son muy rápidos procesando código complejo. Se trata de extender el conjunto de instrucciones de la CPU para que trabaje más eficientemente con tratamiento de imágenes y aplicaciones en 3D. Compañías   Cirix   y AMD

![imagen](img/Historia_microprocesadores44.png)

\-Ejecutar más instrucciones por ciclo.

\-Ejecutar las instrucciones en orden distinto del original para que las interdependencias entre operaciones sucesivas no afecten al rendimiento del procesador.

\-Contribuir a acelerar el rendimiento global del sistema, además de la velocidad de la

CPU.

![imagen](img/Historia_microprocesadores45.jpg)

## 5. DISEÑO DE LOS MICROPROCESADORES – Aumento de prestaciones

INEFICIENCIA =>   La mayoría de los componentes estaban ociosos más del 90% del tiempo

 Replicación de componentes internos de la CPU.

 Conexiones pensadas para permitir el trabajo en paralelo de TODOS ellos.

![imagen](img/Historia_microprocesadores46.png)

\-La   _arquitectura_   del ordenador ha aportado más al rendimiento que la miniaturización.

\-La   _refrigeración_   se ha convertido en algo crucial.

![imagen](img/Historia_microprocesadores47.jpg)

5. DISEÑO DE LOS MICROPROCESADORES – Aumento de prestaciones

PIPELINE \(SEGMENTACIÓN\)

Se divide cada instrucción en varias fases.

Cada componente de la CPU puede estar ocupado por una fase distinta de una instrucción distinta.

  Se pretende usar todos los componentes de la CPU, el 100% del tiempo.

![imagen](img/Historia_microprocesadores48.png)

![imagen](img/Historia_microprocesadores49.jpg)

5. DISEÑO DE LOS MICROPROCESADORES – Aumento de prestaciones

HYPER\-THREADING \(HT   Technology  \)

![imagen](img/Historia_microprocesadores50.png)

  * Se simula, de cara a los programas, como si el PC tuviera dos CPU’s, en lugar de una solo.
  * Lo inventó Intel y mejora el rendimiento un 30%.
  * Permite procesar en paralelo, sobre una misma CPU, la ejecución de varios programas “multihilo”.
  * Invisible para el SO y los programas. Solo se requiere “multiprocesamiento simétrico” \(SMP\).

![imagen](img/Historia_microprocesadores51.jpg)

5. DISEÑO DE LOS MICROPROCESADORES – Aumento de prestaciones

HYPER\-  Transport   \(HT\) o   Lightning   Data   Transport   \(LDT\)

  * Tecnología de comunicación bidireccional que ofrece gran ancho de banda.
  * Comunicación entre chips de un circuito integrado.
  * Sustituto del FSB .
  * Pretende reducir número de buses y facilitar multiprocesamiento.
  * Proporciona conexiones auto\-negociadas.
  * Utiliza líneas de 32 bits.
  * Usado por AMD en procesadores y chipsets.

![imagen](img/Historia_microprocesadores52.png)

![imagen](img/Historia_microprocesadores53.jpg)

5. DISEÑO DE LOS MICROPROCESADORES – Aumento de prestaciones

Intel   QuickPath     Inteconnect   \(QPI\)

  * Desarrollado por Intel para competir con HyperTransport.
  * Reemplaza FSB en procesadores \(p.ej, Core i7\) y chipsets \(X58\).

![imagen](img/Historia_microprocesadores54.png)

![imagen](img/Historia_microprocesadores55.png)

![imagen](img/Historia_microprocesadores56.jpg)

## 6. EVOLUCIÓN DE LOS MICROPROCESADORES

 1. Microprocesadores de Intel más antiguos:

![imagen](img/Historia_microprocesadores57.png)

![imagen](img/Historia_microprocesadores58.jpg)

![imagen](img/Historia_microprocesadores59.png)

 1972: Intel 8008

 1974: Intel 8080

 1971: Intel 4004

![imagen](img/Historia_microprocesadores60.jpg)

![imagen](img/Historia_microprocesadores61.jpg)

 1978: Intel 8086

 1979: Intel 8088

![imagen](img/Historia_microprocesadores62.gif)

![imagen](img/Historia_microprocesadores63.gif)

![imagen](img/Historia_microprocesadores64.jpg)

 2. Microprocesadores antiguos de otros fabricantes:

![imagen](img/Historia_microprocesadores65.png)

![imagen](img/Historia_microprocesadores66.png)

 1975:     Signetics     2650

![imagen](img/Historia_microprocesadores67.png)

![imagen](img/Historia_microprocesadores68.png)

![imagen](img/Historia_microprocesadores69.png)

 1975: Motorola 6800

 1978: Motorola 68000

![imagen](img/Historia_microprocesadores70.jpg)

 3. Siguiente generación de Intel:

![imagen](img/Historia_microprocesadores71.jpg)

![imagen](img/Historia_microprocesadores72.jpg)

![imagen](img/Historia_microprocesadores73.jpg)

 1982: Intel 80286

 1989: Intel 80486

 1985: Intel 80386

![imagen](img/Historia_microprocesadores74.jpg)

![imagen](img/Historia_microprocesadores75.jpg)

![imagen](img/Historia_microprocesadores76.png)

1997: Intel Pentium II

 1993: Intel Pentium

1995: Intel Pentium Pro

![imagen](img/Historia_microprocesadores77.jpg)

 4. Un nuevo competidor en el mercado, AMD:

![imagen](img/Historia_microprocesadores78.png)

![imagen](img/Historia_microprocesadores79.png)

![imagen](img/Historia_microprocesadores80.png)

![imagen](img/Historia_microprocesadores81.png)

![imagen](img/Historia_microprocesadores82.png)

![imagen](img/Historia_microprocesadores83.png)

![imagen](img/Historia_microprocesadores84.jpg)

5. Microprocesadores modernos \- 1999

![imagen](img/Historia_microprocesadores85.png)

VELOCIDAD DEL CPU DESDE 266\-550 MHZ

CACHE L1 DE 64 KB

2.2. A 2.4 VOLTIOS

TIENE 9.3 MILLONES DE TRANSISTORES

SOCKET 7 O SÚPER SOCKET 7 .

Intel Pentium III

![imagen](img/Historia_microprocesadores86.png)

Velocidad de bus a 266   MHz.

Cache L1 128 KB

Cache L2 512 KB

Socket de 370   pins  .

![imagen](img/Historia_microprocesadores87.png)

5. Microprocesadores modernos \- 2000

![imagen](img/Historia_microprocesadores88.jpg)

![imagen](img/Historia_microprocesadores89.png)

ANCHO DE BANDA 2.1 GB/SEG.

CACHE L1 128 KB, 64KB DATOS Y

 64KB INSTRUCCIONES.

CACHE L2 256 KB

BUS FRONTAL DE 266 MHZ

SOCKET 462 PINS.

BUS DE 400 MHZ

ANCHO DE BANDA DE 3.2 GB/SEG

SOCKET 432 PNS.

CACHE L1 DE 8 KB

CACHE L2 DE 512 KB ,

![imagen](img/Historia_microprocesadores90.png)

5. Microprocesadores modernos \- 2003

![imagen](img/Historia_microprocesadores91.png)

![imagen](img/Historia_microprocesadores92.jpg)

CPU   900 MHz

Velocidad   de FSB 400 MT/s

CPU   800 MHz

Velocidad   de Bus 200 MHZ

Cache L1 128KB

Cache L2 64 KB

Socket 370 pins.

![imagen](img/Historia_microprocesadores93.png)

5. Microprocesadores modernos \- 2005

![imagen](img/Historia_microprocesadores94.png)

![imagen](img/Historia_microprocesadores95.png)

2 CPUs \(Pentium 4\) a   2,66\-3,6 GHz

Velocidad   de FSB 533\-800 MHz

Variantes   con   HyperThreading

CPU   1,0\-3,2 GHz

Velocidad     HyperTransport     800\-1000 MT/s

![imagen](img/Historia_microprocesadores96.png)

5. Microprocesadores modernos \- 2006

![imagen](img/Historia_microprocesadores97.png)

![imagen](img/Historia_microprocesadores98.png)

![imagen](img/Historia_microprocesadores99.png)

AMD   Athlon   64 FX

Intel Core 2 Duo

2 CPUs a 1  ,8\-3,3 GHz

Velocidad   de FSB 533\-1600 MT/s

64 bits

CPU   2,4\-3,0 GHz

Bus de   sistema   a 2 GHz

64 bits

![imagen](img/Historia_microprocesadores100.png)

5. Microprocesadores modernos \- 2007

![imagen](img/Historia_microprocesadores101.png)

![imagen](img/Historia_microprocesadores102.png)

![imagen](img/Historia_microprocesadores103.png)

Intel Core 2 Quad

4 CPUs a 2  ,3\-3,0 GHz

Velocidad   de FSB 1066\-1333 MT/s

4 CPUs   2,4\-2,6 GHz

Bus de   sistema   a 2 GHz

![imagen](img/Historia_microprocesadores104.jpg)

5. Los microprocesadores más modernos de Intel

![imagen](img/Historia_microprocesadores105.png)

![imagen](img/Historia_microprocesadores106.jpg)

![imagen](img/Historia_microprocesadores107.jpg)

![imagen](img/Historia_microprocesadores108.jpg)

   2 ó 4 núcleos

 Hasta 3,60 GHz con Turbo   Boost

   HyperThreading

 Velocidad bus DMI de 2,5 GT/s

   2 ó 4 núcleos

   HyperThreading

 GPU integrada

   4 núcleos

 Velocidad de CPU: 2,66 GHz a 3,33 GHz

 Velocidad QPI: 4,8\-6,4 GT/s

![imagen](img/Historia_microprocesadores109.png)

- 1971:  Intel 4004  \(primer microprocesador comercial\)
- 1972:  Intel 8008
- 1974:  Intel 8080
- 1975: Signetics 2650, MOS 6502,  Motorola 6800
- 1976:  Zilog   Z80
- 1978:  Intel 8086 ,  Motorola 68000
- 1979:  Intel 8088
- 1982:  Intel 80286
- 1985:  Intel 80386 ,  AMD Am386
- 1987:  Motorola 68030
- 1989:  Intel 80486 , AMD Am486

![imagen](img/Historia_microprocesadores110.png)

- 1993:  Intel Pentium ,  AMD K5
- 1995: Intel Pentium Pro
- 1997:  Intel Pentium II ,  AMD K6
- 1999:  Intel Pentium III
- 2000:  Intel Pentium 4 ,  AMD   Athlon   XP

2003: PowerPC G5, Intel Pentium M

2005: Intel Extreme Edition con  hyper\-threading ,  Intel   Core              Duo ,  AMD   Athlon   64 ,  AMD   Athlon   64 X2 ,

2006:  Intel   Core   2   Duo , Intel Core 2 Extreme, AMD Athlon FX

2007:  Intel   Core   2   Quad ,  AMD   Quad     Core , AMD Quad FX

2008\-…:  Intel   Core   i3,   Intel   Core   i5, Intel   Core   i7,                 AMD Athlon II, AMD Phenom II, AMD Turion II,…

![imagen](img/Historia_microprocesadores111.jpg)

## 7.CARACTERÍSTICAS TÉCNICAS DE ALGUNOS MICROS

Pentium   Classic  :

![imagen](img/Historia_microprocesadores112.png)

Está optimizado para aplicaciones de 16 bits.  Dispone de 8Kb de caché de instrucciones \+ 8Kb de caché de datos.  Utiliza el zócalo de tipo 5 \(socket 5\) o el de los MMX \(tipo 7\). También es conocido por su nombre clave P54C.  Está formado por 3,3 millones de transistores

![imagen](img/Historia_microprocesadores113.gif)

| Especificaciones de la gama Pentium |            |            |         |       |               |        |
| :---------------------------------: | :--------: | :--------: | :-----: | :---: | :-----------: | :----: |
|             Procesador              | Frecuencia | Tecnología | Voltaje |  Bus  | Multiplicador | Socket |
|                 P60                 |   60Mhz.   |   0,8 µ    |   5v    | 60Mhz |       -       |   4    |
|                 P66                 |   66Mhz    |   0,8 µ    |   5v    | 66Mhz |       -       |   4    |
|                 P75                 |   75Mhz    |   0,6 µ    |  3,52v  | 50Mhz |      1,5      | 5 / 7  |
|                 P90                 |   90Mhz    |   0,6 µ    |  3,52v  | 60Mhz |      1,5      | 5 / 7  |
|                P100                 |   100Mhz   |   0,6 µ    |  3,52v  | 66Mhz |      1,5      | 5 / 7  |
|                P120                 |   120Mhz   |   0,35 µ   |  3,52v  | 60Mhz |       2       | 5 / 7  |
|                P133                 |   133Mhz   |   0,35 µ   |  3,52v  | 66Mhz |       2       | 5 / 7  |
|                P150                 |   150Mhz   |   0,35 µ   |  3,52v  | 60Mhz |      2,5      |   7    |
|                P166                 |   166Mhz   |   0,35 µ   |  3,52v  | 66Mhz |      2,5      |   7    |
|                P200                 |   200Mhz   |   0,35 µ   |  3,52v  | 66Mhz |       3       |   7    |

![imagen](img/Historia_microprocesadores114.jpg)

![imagen](img/Historia_microprocesadores115.png)

La memoria de segundo nivel trabaja a la misma velocidad que la CPU.  Utilizan el zócalo super7 a 100   Mhz.  64 KB   de caché L1 \(32 para datos y 32 para instrucciones\)  256 KB   de caché L2.  Fabricados con 21,3 millones de transistores y tecnología de 0,25 micras.  Soporte para AGP.

| Especificaciones de la gama K6-III |        |               |              |        |         |              |                  |
| :--------------------------------: | :----: | :-----------: | :----------: | :----: | :-----: | :----------: | :--------------: |
|             Procesador             | Freq.  | Voltaje Core | Voltaje I/O |  Bus   | Multip. | Temp.Máxima | Potencia Máxima |
|             K6-III/400             | 400Mhz |      2,4      |     3,3      | 100Mhz |   2,5   |     65º      |      26,8 W      |
|             K6-III/450             | 450Mhz |      2,4      |     3,3      | 100Mhz |    3    |     65º      |     29,50 W      |

