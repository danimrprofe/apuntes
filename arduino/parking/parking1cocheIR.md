```c
// variables y  includes

#include <Servo.h>

// Configuramos PINES para leer los valores del LDR
// Los conectaremos a los pines analógicos A1 a A3

int pinP1Sensor = A1;

// Configuramos los PINES para cada LED
// Los conectaremos a los pines 7 a 12

int pinP1Rojo = 12;
int pinP1Verde = 11;

int valorSensorP1 = 0;

// Grados del servo para las dos posiciones (abierto y cerrado)

int posicionAbierto = 0; // variable to store the servo position
int posicionCerrado = 90;

Servo miservo; // create servo object to control a servo

void setup()
{

  Serial.begin(9600);
  miservo.attach(13); // Le asignamos el PIN

  //Habilitamos como salida

  pinMode(pinP1Rojo, OUTPUT);
  pinMode(pinP1Verde, OUTPUT);

}

// loop part

void loop()
{

  delay(200);

  valorSensorP1 = digitalRead(pinP1Sensor);
  Serial.println(valorSensorP1);

  if (valorSensorP1 == HIGH)
  {
    digitalWrite(pinP1Rojo, LOW);
    digitalWrite(pinP1Verde, HIGH);
  }
  else
  {
    digitalWrite(pinP1Rojo, HIGH);
    digitalWrite(pinP1Verde, LOW);
  }
 
  if (parkingLleno == false)
  {
     miservo.write(posicionCerrado); // tell servo to go to position in variable 
  }
  else
  {
     miservo.write(posicionAbierto); // tell servo to go to position in variable 'pos'
    }
  
}
```