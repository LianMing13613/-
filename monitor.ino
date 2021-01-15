#include <DHT.h>
#include <DHT_U.h>

#define DHTTYPE DHT22
#define WRELAY_PIN 6
#define DHT_PIN 22
#define MOISTURE_PIN A0 

DHT dht(DHT_PIN, DHTTYPE);
void setup() {
  // put your setup code here, to run once:
  pinMode(CRELAY_PIN,OUTPUT);
  pinMode(WRELAY_PIN,OUTPUT);
  pinMode(MOISTURE_PIN, INPUT);
  dht.begin();
}

String readCommand(){
  String recv = "";
  String a;
  while(Serial.available())
  {
    a = Serial.readString();
    recv = recv + a;
    Serial.print(a);
  }
}

void loop() {
  float temp = dht.readTemperature();
  float humi = dht.readHumidity();
  float mois = analogRead(MOISTURE_PIN);
  String cmd = readCommand();

  if(cmd.indexOf('a')>=0)
  {
    digitalWrite(6, HIGH);
    Serial.print("Power on the Water!");
  }
  else if(cmd.indexOf('b')>=0)
  {
    digitalWrite(6, LOW);
    Serial.print("Power off the Water~");
  }

  Serial.print("[T:" + String(temp) + ":0,");
  Serial.print("H:" + String(humi) + ":0,");
  Serial.print("W:" + String(mois) + ":0," + "]");
}
