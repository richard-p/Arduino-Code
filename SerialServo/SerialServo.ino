#include <Servo.h>

Servo myservo;
int SERVO = 3;
char data;

void setup() {
  Serial.begin(9600);
  myservo.attach(SERVO);
}

void loop() {
  while (Serial.available() > 0){ //While there is a serial connection
   data = Serial.read();
   
   
   if (data == 'l'){ //Left position
     myservo.write(0);
     delay(15);
   }
   
   else if (data == 'r'){ //Right position
     myservo.write(170);
     delay(15);
   }
   
   else if (data == 'c'){ //Center position
     myservo.write(83);
     delay(15);
   }
   
   
  }

}
