#include <Stepper.h>

const int stepsPerRevolution = 200; // número de pasos por revolución de tu motor
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11); // Pines del motor

void setup() {
  Serial.begin(9600);
  myStepper.setSpeed(60); //velocidad de giro de tu motor
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 's') {
      Serial.println("Girando 90 grados...");
      myStepper.step(200);
      delay(120000); 
      Serial.println("Girando -90 grados...");
      myStepper.step(-200);
    }
  }
}
