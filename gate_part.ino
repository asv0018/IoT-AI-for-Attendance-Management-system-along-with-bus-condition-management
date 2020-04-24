#include <Servo.h> 
Servo gate;

void setup(){
  Serial.begin(9600);
  gate.attach(9);
}
void loop(){
  if (Serial.available()>0){
    Serial.println("bus is entering the campus!");
    if(Serial.readString()){
       Serial.println("bus entered inside");
       turnGateOn();
       delay(5000);
       turnGateOff();
    }
  }
}
void turnGateOn(){
 for (int pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 90 degrees
    Serial.println(pos);
    gate.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position is 15*(90-0)=1350 ms
  }
}
void turnGateOff(){
  for (int pos = 90; pos >= 0; pos -= 1) { // goes from 90 degrees to 0 degrees
    gate.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                     // waits 15ms for the servo to reach the position is 15*(90-0)=1350 ms
  }
}
