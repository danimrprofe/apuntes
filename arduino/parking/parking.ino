//variables and includes

#include <Servo.h>
int pinP1Sensor = A1;
int pinP2Sensor = A2;
int pinP3Sensor = A3;
int pinP1Red = 12;
int pinP1Green = 11;
int pinP2Red = 10;
int pinP2Green = 9;
int pinP3Red = 8;
int pinP3Green = 7;
int P1SensorValue = 0;
int P2SensorValue = 0;
int P3SensorValue = 0;
int pos = 0;    // variable to store the servo position
Servo myservo;  // create servo object to control a servo

// setup part

void setup() {

  Serial.begin(9600);
  myservo.attach(13);  // Le asignamos el PIN
  pinMode(pinP1Red, OUTPUT);
  pinMode(pinP1Green, OUTPUT);
  
}

// loop part

void loop() {
    
  P1SensorValue = analogRead (pinP1Sensor);
  P2SensorValue = analogRead (pinP2Sensor);
  P3SensorValue = analogRead (pinP3Sensor);

  Serial.println(P1SensorValue);
  Serial.println(P2SensorValue);
  Serial.println(P3SensorValue);

  if (P1SensorValue > 60){
    digitalWrite(pinP1Red, LOW);
    digitalWrite(pinP1Green, HIGH);
  } 
  else{
    digitalWrite(pinP1Red, HIGH);
    digitalWrite(pinP1Green, LOW);
  }
    if (P2SensorValue > 60){
    digitalWrite(pinP2Red, HIGH);
    digitalWrite(pinP2Green, LOW);
  }  
    else{
    digitalWrite(pinP2Red, LOW);
    digitalWrite(pinP2Green, HIGH);
  }
    if (P3SensorValue > 60){
    digitalWrite(pinP3Red, LOW);
    digitalWrite(pinP3Green, HIGH);
  }
    else{
    digitalWrite(pinP3Red, HIGH);
    digitalWrite(pinP3Green, LOW);
  }  
  /*
  if (P1SensorValue > 60 && P2SensorValue > 60 && P3SensorValue > 60){

      myservo.write(0);              // tell servo to go to position in variable 'pos
    }
  
  else{

      myservo.write(90);              // tell servo to go to position in variable 'pos'
    }
  */
  


}
