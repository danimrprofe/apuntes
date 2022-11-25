# Problema

- Si el sensor de infrarrojos detecta un coche, enciende el led rojo y apaga el led verde y baja la barrera
- Si el sensor no detecta un coche, se apaga el led rojo y apaga el led verde.

# Algoritmo

Solo una vez:

1. Decir donde están conectados los **led** y configurar como salida
2. Decir donde está conectado el **sensor IR** y configurar como entrada
3. Decir donde está conectado el **motor** y programar como salida

Repetir siempre:

1. Mirar el valor del sensor de IR
2. Si el sensor detecta un valor alto
   1. Enciende el rojo y apaga el verde
   2. Baja la barrera con el servo
3. Si el sensor detecta un valor bajo
   1. Apaga el rojo y enciende el verde
   1. Baja la barrera con el servo

# Código

```c
// variables y  includes

#include <Servo.h>

int pinSensor = A1;
int pinRojo = 12;
int pinVerde = 11;
int valorSensorIR = 0;


void setup()
{

  Serial.begin(9600);


  //Habilitamos como salida

  pinMode(pinRojo, OUTPUT);
  pinMode(pinVerde, OUTPUT);
}

void loop()
{
  valorSensorIR = digitalRead(pinSensor);
  Serial.println(valorSensorIR);

  if (valorSensorIR == HIGH)
  {
    digitalWrite(pinRojo, LOW);
    digitalWrite(pinVerde, HIGH);
  }
  else
  {
    digitalWrite(pinRojo, HIGH);
    digitalWrite(pinVerde, LOW);
  }   
}
```