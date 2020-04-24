#include <ArduinoJson.h>
void setup(){
Serial.begin(9600);
}
void loop() {
StaticJsonBuffer<200> jsonBuffer;
JsonObject& rpi = jsonBuffer.createObject();
rpi["tem"]=fetchEngineTemperature();
rpi["fuel"]=checkFuel();
rpi.printTo(Serial);
Serial.println();
delay(2000);
}
int fetchEngineTemperature(){
 unsigned int value =analogRead(A1);
  value=(value*500)/1023;
  return value;
}
String checkFuel(){
  int value=analogRead(A0);
  if (value>5){
    return "HIGH";
  }
  if ((value<=5)&&(value>3)){
    return "MED";
  }
  if(value<3){
    return "LOW";
  }
}
