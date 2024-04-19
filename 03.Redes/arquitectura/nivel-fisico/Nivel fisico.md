# Funciones y servicios del nivel físico

## Transmisión de datos

Definición

Conceptos básicos

- Emisor
- Receptor
- Medio
- Codificación del canal
- Mensaje

## Clasificación de sistemas de transmisión

### Dirección

Los sistemas de transmisión se clasifican según la dirección de la comunicación en:

- **Simplex**: Esta dirección de comunicación permite la transmisión de datos en una sola dirección. Esto significa que los datos sólo se pueden transmitir en una dirección, no se pueden recibir.

- **Half-duplex**: Esta dirección de comunicación permite la transmisión de datos en ambas direcciones, pero no al mismo tiempo. Esto significa que los datos sólo se pueden transmitir en una dirección a la vez.

- **Full-duplex**: Esta dirección de comunicación permite la transmisión de datos en ambas direcciones al mismo tiempo. Esto significa que los datos se pueden transmitir y recibir simultáneamente.

### Soporte

Los sistemas de transmisión se clasifican según el soporte de la comunicación en:

- **A 2 hilos**: Esta clasificación de sistemas de transmisión utiliza dos hilos de comunicación para transmitir datos.

- **A 4 hilos**: Esta clasificación de sistemas de transmisión utiliza cuatro hilos de comunicación para transmitir datos.

- **A 4 hilos equivalentes**: Esta clasificación de sistemas de transmisión utiliza cuatro hilos equivalentes para transmitir datos. Estos hilos son equivalentes en cuanto a velocidad de transmisión, lo que permite una transmisión simultánea en ambas direcciones.

### Técnica

Los sistemas de transmisión se clasifican según la técnica de transmisión en:

- **Sistemas analógicos**: Esta clasificación de sistemas de transmisión utiliza señales analógicas para transmitir datos.

- **Sistemas digitales**: Esta clasificación de sistemas de transmisión utiliza señales digitales para transmitir datos.

## Tipos de medios

Existen diferentes tipos de medios de transmisión que se utilizan en redes informáticas. Estos medios se dividen en dos grandes grupos: los guiados y los no guiados.

### Los medios guiados

Los medios guiados son aquellos que utilizan cables para transmitir información. El tipo de cable utilizado depende de la frecuencia de la señal y de la distancia a recorrer. Entre los medios guiados más comunes se encuentran:

- **Par trenzado**: Utilizado para transmisiones a corta y media distancia. Existen tres tipos de par trenzado: UTP (Unshielded Twisted Pair), STP (Shielded Twisted Pair) y FTP (Foiled Twisted Pair).

- **Coaxial**: Utilizado para transmisiones a larga distancia. El cable coaxial utilizado más común es el BNC (Bayonet Neill-Concelman).

- **Fibra óptica**: Utilizado para transmisiones a larga distancia. Existen dos tipos: monomodo y multimodo.

### Los medios no guiados

Los medios no guiados son aquellos que no utilizan cables para transmitir información. Entre los medios no guiados más comunes se encuentran:

- **Microondas**: Utilizado para transmisiones a larga distancia.

- **Satélite**: Utilizado para transmisiones a muy larga distancia.

- **Infrarrojos**: Utilizado para transmisiones a corta distancia.

## Tipos de señales

### Transmisión analógica

- Nodos locales y nodos de tránsito
- Degradación
  - Retardo
  - Atenuación
  - Perturbaciones

### Transmisión digital

- Conversores ADC y DAC
- Codificadores y decodificadores
- Moduladores
- Nodos de tránsito: enrutamiento y regeneración

## Adaptación al medio

### Técnicas de codificación

Las **técnicas de codificación** son una forma de representar los datos digitales usando señales eléctricas o ópticas.

Una de las técnicas más comunes es la de **NRZ** (Non-Return to Zero), que codifica los bits de los datos en señales de niveles de voltaje diferentes. Otra técnica común es la codificación **Bipolar**, que usa señales de voltaje positivo y negativo para representar los bits de los datos. Por último, la codificación **Manchester** usa una señal binaria que alterna entre altos y bajos niveles de voltaje para representar los bits de los datos.

### Técnicas de modulación

La **modulación** es el proceso de transformar una señal de información, como un mensaje de audio o datos, para su transmisión a través de un canal de comunicación.

La señal de información se conoce como señal **portadora**, mientras que la señal modulada se conoce como señal **modulada**.

Esta última se caracteriza por tener una frecuencia, un ancho de banda y una amplitud que pueden ser controladas para modificar la señal original.

#### Modulaciones Analógicas

Las modulaciones analógicas son la forma más común de codificar señales para su transmisión a través de canales de comunicación. Estas incluyen Amplitud Modulada (AM), Frecuencia Modulada (FM) y Fase Modulada (PM).

**AM**

La amplitud modulada (AM) es el tipo más común de modulación analógica. En este método, la amplitud de la señal se modifica para codificar la información de audio. Se caracteriza por una alta relación señal-ruido, pero un ancho de banda limitado.

**FM**

La frecuencia modulada (FM) es una forma avanzada de modulación analógica. En este método, la frecuencia de la señal se modifica para codificar la información de audio. Se caracteriza por un ancho de banda mayor que el de la AM, una mayor relación señal-ruido y una mejor calidad de sonido.

**PM**

La fase modulada (PM) es una forma avanzada de modulación analógica. En este método, la fase de la señal se modifica para codificar la información de audio. Se caracteriza por un ancho de banda mayor que el de la AM y una mejor calidad de sonido.

#### Modulaciones Digitales

Las modulaciones digitales se utilizan para codificar señales digitales para su transmisión a través de canales de comunicación. Estas incluyen Amplitud Síncrona (ASK), Frecuencia Síncrona (FSK) y Fase Síncrona (PSK).

**ASK**

La amplitud síncrona (ASK) es una forma de modulación digital. En este método, la amplitud de la señal se modifica para codificar la información digital. Se caracteriza por un ancho de banda limitado y una alta relación señal-ruido.

**FSK**

La frecuencia síncrona (FSK) es una forma de modulación digital. En este método, la frecuencia de la señal se modifica para codificar la información digital. Se caracteriza por un ancho de banda mayor que el de la AM y una relación señal-ruido aceptable.

**PSK**

La fase síncrona (PSK) es una forma de modulación digital. En este método, la fase de la señal se modifica para codificar la información digital. Se caracteriza por un ancho de banda mayor que el de la AM y una relación señal-ruido aceptable.

## Perturbaciones

### Transmisión analógica

#### Distorsión

La distorsión es la modificación de la señal original por el sistema de transmisión (lineal o no lineal). Esta distorsión se debe principalmente a la variación de los parámetros en el circuito, como el voltaje o la impedancia. La distorsión se manifiesta como una variación en el contorno de la señal y se mide como el porcentaje de variación de la señal original.

#### Interferencia

La interferencia es una de las principales causas de ruido en un sistema de transmisión. Se produce cuando la señal de transmisión se ve interferida por una fuente externa (como otro sistema de transmisión cercano). Esto se debe a que, al pasar a través de la línea, la señal se ve afectada por los cambios en la impedancia, el voltaje o la temperatura.

#### Ruido

El ruido se refiere a las perturbaciones aleatorias (internas o externas) que afectan la señal de transmisión. Estas perturbaciones pueden ser provocadas por una amplia variedad de factores como la temperatura, el voltaje, etc. El ruido es una de las principales causas de degradación de la señal de transmisión.

#### Diafonía

La diafonía se produce cuando la señal de transmisión es afectada por una señal externa, ya sea un sistema cercano o el sistema mismo. Esto se debe a que la señal externa se mezcla con la señal original, produciendo una interferencia que afecta a la calidad de la señal.

#### SNR

SNR (Signal-to-Noise Ratio) es una medida de la relación entre la señal y el ruido en un sistema de transmisión. Esta relación se mide como una proporción entre la señal y el ruido, donde un valor más alto indica una mejor calidad de la señal de transmisión.

### Transmisión digital

#### Probabilidad de error

La probabilidad de error es una medida de la fiabilidad de un sistema de transmisión digital. Esta medida se refiere a la probabilidad de que la señal de transmisión se vea afectada por un error de bit o una distorsión de la señal.

#### Regeneración de la señal

La regeneración de la señal se refiere al proceso por el cual la señal se recupera entre intervalos. Esto se logra mediante la eliminación del ruido y la distorsión de la señal original.

#### Interferencia intersimbólica

La interferencia intersimbólica es una de las principales causas de degradación de la señal de transmisión digital. Esta interferencia se produce cuando los bits de una señal digital se mezclan con los bits de otra señal, lo que produce una interferencia entre las señales. Esto afecta la calidad de la señal de transmisión.
