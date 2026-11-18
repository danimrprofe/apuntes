// variables y  includes

#include <Servo.h>

// Configuramos PINES para leer los valores del LDR
// Los conectaremos a los pines analógicos A1 a A3

int pinP1Sensor = A1;
int pinP2Sensor = A2;
int pinP3Sensor = A3;

int valorSensorP1 = 0;
int valorSensorP2 = 0;
int valorSensorP3 = 0;

// Configuramos los PINES para cada LED
// Los conectaremos a los pines 7 a 12

int pinP1Rojo = 12;
int pinP1Verde = 11;
int pinP2Rojo = 10;
int pinP2Verde = 9;
int pinP3Rojo = 8;
int pinP3Verde = 7;

// Los umbrales los colocaremos en el valor en el que queramos
// Detectar el cambio de luz
// Si a tope de luz el LDR me da 100 y con poca luz 50,
// podria poner un valor de 75

int UmbralLuzP1 = 60;
int UmbralLuzP2 = 40;
int UmbralLuzP3 = 100;

// Estados true or false de los 3 parkings

boolean P1_ocupado;
boolean P2_ocupado;
boolean P3_ocupado;

// Grados del servo para las dos posiciones (abierto y cerrado)

int posicionAbierto = 90; // variable to store the servo position
int posicionCerrado = 0;

Servo miservo; // create servo object to control a servo

// setup part

void setup()
{

  Serial.begin(9600);
  miservo.attach(13); // Le asignamos el PIN
  pinMode(pinP1Rojo, OUTPUT);
  pinMode(pinP1Verde, OUTPUT);
  pinMode(pinP2Rojo, OUTPUT);
  pinMode(pinP2Verde, OUTPUT);
  pinMode(pinP2Rojo, OUTPUT);
  pinMode(pinP2Verde, OUTPUT);
}

// loop part

void loop()
{

  delay(200);

  valorSensorP1 = analogRead(pinP1Sensor);
  valorSensorP2 = analogRead(pinP2Sensor);
  valorSensorP3 = analogRead(pinP3Sensor);

  Serial.println(valorSensorP1);
  Serial.println(valorSensorP2);
  Serial.println(valorSensorP3);

  if (valorSensorP1 > UmbralLuzP1)
  {
    digitalWrite(pinP1Rojo, LOW);
    digitalWrite(pinP1Verde, HIGH);
    P1_ocupado = false;
  }
  else
  {
    digitalWrite(pinP1Rojo, HIGH);
    digitalWrite(pinP1Verde, LOW);
    P1_ocupado = true;
  }
  if (valorSensorP2 > UmbralLuzP2)
  {
    digitalWrite(pinP2Rojo, LOW);
    digitalWrite(pinP2Verde, HIGH);
    P2_ocupado = false;
  }
  else
  {
    digitalWrite(pinP2Rojo, HIGH);
    digitalWrite(pinP2Verde, LOW);
    P2_ocupado = true;
  }
  if (valorSensorP3 > UmbralLuzP3)
  {
    digitalWrite(pinP3Rojo, LOW);
    digitalWrite(pinP3Verde, HIGH);
    P3_ocupado = false;
  }
  else
  {
    digitalWrite(pinP3Rojo, HIGH);
    digitalWrite(pinP3Verde, LOW);
    P3_ocupado = true;
  }

  // Si las 3 plazas están ocupadas (valores true) cierra la barrera
  // Si al menos una no lo está, abre la barrera

  if (P1_ocupado && P2_ocupado && P3_ocupado)
  {
    miservo.write(posicionCerrado); // tell servo to go to position in variable 'pos
  }
  else
  {
    miservo.write(posicionAbierto); // tell servo to go to position in variable 'pos'
  }
}
