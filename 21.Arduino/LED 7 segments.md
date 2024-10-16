
## 7 segments (1 dígito)

Un **seven segments** es un dispositivo de visualización formado por siete diodos LED dispuestos en forma de número 8.

Se utilizan para mostrar números, letras y caracteres especiales. Se usan en una variedad de dispositivos electrónicos, como relojes digitales, calculadoras, contadores, temporizadores, etc.

![imagen](img/2022-12-05-16-21-35.png)

## Combinaciones

Estas son las combinaciones que podemos hacer para mostrar los distintos números:

![imagen](img/2022-12-12-18-32-50.png)

## Componentes necesarios

| cantidad | componente                                     |
| -------- | ---------------------------------------------- |
| 1        | placa``Arduino``                               |
| 1        | protoboard                                     |
| 1        | circuito integrado 74HC595                     |
| 1        | Pantalla 7 segments                            |
| 8        | resistencias de 220 ohm                        |
| 1        | M-M cables (cables de puente de macho a macho) |

## Display de siete segmentos

Abajo está el diagrama de pines de siete segmentos

![imagen](media/image130.jpeg)

Los números del 0 al 9 se representan en un display de siete segmentos mediante la activación de segmentos individuales. Cada LED, en caso de recibit un 1, se ilumina. Combinando todos los LED podemos hacer todos los números

| dp  | a	b	c	d	e	f	g   |
| --- | --------------- |
| 0   | 0	1	1	1	1	1	1	0 |
| 1   | 0	0	1	1	0	0	0	0 |
| 2   | 0	1	1	0	1	1	0	1 |
| 3   | 0	1	1	1	1	0	0	1 |
| 4   | 0	0	1	1	0	0	1	1 |
| 5   | 0	1	0	1	1	0	1	1 |
| 6   | 0	1	0	1	1	1	1	1 |
| 7   | 0	1	1	1	0	0	0	0 |
| 8   | 0	1	1	1	1	1	1	1 |
| 9   | 0	1	1	1	1	0	1	1 |

# Registro de desplazamiento

Vamos a utilizar un **circuito integrado** para simplificar el control del seven segments, en concreto se trata de un registro de desplazamiento **74HC595** para controlar la visualización de un seven segments.

![alt text](image-5.png)

El 74HC595 es un registro de desplazamiento de 8 bits que se utiliza comúnmente para controlar múltiples dispositivos, como un display de siete segmentos. Permite la conexión de varios dispositivos en cadena, simplificando la conexión a microcontroladores u otros circuitos de control. El registro de desplazamiento toma datos de entrada serie y los desplaza a través de sus salidas de forma paralela, lo que lo hace ideal para controlar múltiples segmentos de un display de siete segmentos de manera eficiente y con menos pines de control.

## Conexión

![imagen](media/image131.jpeg)

## Diagrama de cableado

![imagen](media/image132.jpeg)

La siguiente tabla muestra la tabla de correspondencias pantalla de siete segmentos 74HC595 pin

## Paso uno: conexión 74HC595

En primer lugar, el cableado está conectado a la alimentación y tierra:

- VCC (pin 16) y Señor (pin 10) conectado a 5V
- GND (pin 8) y OE (pin 13) a tierra

## Paso uno: conexión 74HC595

Pin conexión DS, ST_CP y SH_CP:

- DS (pin 14) conectado al pin de tablero UNO R3 2 (la cifra por debajo de la línea amarilla)
- ST_CP (pin 12, perno de pestillo) conectado al pin de tablero UNO R3 3 (línea azul de la figura abajo)
- SH_CP (pin 11, pin de reloj) conectado al pin de tablero UNO R3 4 (figura debajo de la línea blanca)

## Paso 2: conectar el display de siete segmentos

El display de siete segmentos 3, 8 pin a UNO R3 Junta GND (este ejemplo utiliza el cátodo común, si se utiliza el ánodo común, por favor conecte el 3, 8 pines para tablero UNO R3 + 5V)

Según la tabla anterior, conecte el 74HC595 Q0 ~ Q7 a siete segmentos pantalla pin correspondiente (A ~ G y DP) y luego cada pie en una resistencia de 220 ohmios en serie.

## Código

![imagen](media/image133.jpeg)

```c

int tDelay = 100;
int latchPin = 11;      // (11) ST_CP [RCK] on 74HC595
int clockPin = 9;      // (9) SH_CP [SCK] on 74HC595
int dataPin = 12;     // (12) DS [S1] on 74HC595

byte leds = 0;

void updateShiftRegister()
{
   digitalWrite(latchPin, LOW);
   shiftOut(dataPin, clockPin, LSBFIRST, leds);
   digitalWrite(latchPin, HIGH);
}

void setup()
{
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
}

void loop()
{
  leds = 0;
  updateShiftRegister();
  delay(tDelay);
  for (int i = 0; i < 8; i++)
  {
    bitSet(leds, i);
    updateShiftRegister();
    delay(tDelay);
  }
}
```