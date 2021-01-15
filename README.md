# IoT Proposal 智慧澆水系統

## 概述
智慧澆水系統會持續偵測並記錄盆栽土壤濕度，在土壤過乾時，自動進行行澆水。  

## 功能
 
自動澆水:利用土壤濕度感測器監測濕度，於濕度不足時開啟抽水幫浦澆水。  
自動降溫:利用DHT-22監測環境溫溼度，在溫度過高時，啟動噴霧降溫機。  
手動操作:透過手機手動開啟抽水幫浦、降溫機進行澆水降溫。  
環境監控:記錄環境溫溼度、土壤濕度等資料。    
  
## 工具
一個 raspiberry pi 3  
一個 Arduino MEGA2560開發板  
一個 DHT-22溫溼度模組  
一個 RFLINK-UART無線序列傳輸模組(1對1)  
一個 繼電器  
一個 土壤濕度感測器  
一個 延長線(中繼延長線)  
一個 水管  
一個 海綿(代替盆栽)

## 示意圖
![image](https://github.com/LianMing13613/-/blob/main/picture/示意圖.png)  
![image](https://github.com/LianMing13613/-/blob/main/picture/示意圖2.png)  

## 步驟
### 一 Arduino開發版接線
1.接上RFLINK-UART無線序列傳輸模組，rx端須接到開發版的tx，tx端則接到開發版的rx端(pin:rx0,tx0)
![image](https://github.com/LianMing13613/-/blob/main/picture/RFlink.jpg)
2.接上土壤濕度感測器(PIN:A0, Mode:IN)
![image](https://github.com/LianMing13613/-/blob/main/picture/土壤濕度.jpg)  
3.接上DHT-22(PIN:22, Mode:IN)  
![image](https://github.com/LianMing13613/-/blob/main/picture/DHT22.jpg)  
4.接上繼電器(PIN:6, Mode:OUT)  
![image](https://github.com/LianMing13613/-/blob/main/picture/繼電器.jpg)  
5.剪斷中繼線一條線路，並連接繼電器，可參考網站  
http://lioujj.blogspot.com/2015/09/arduino.html  
http://a-chien.blogspot.com/2016/07/arduino_7.html  
![image](https://github.com/LianMing13613/-/blob/main/picture/中繼線+繼電器.jpg)  
### 二 Raspberry pi 3 接線
接上RFLINK-UART無線序列傳輸模組，接線如開發版

## 程式設定
### 一 Arduino
1.至Arduino官方網站下載Arduino IDE:  
https://www.arduino.cc/en/software
2.欲使用DHT22，需先下載DHT sensor library與Adafruit Unified Sensor的.zip檔，並加入library  
DHT sensor library: https://www.arduinolibraries.info/libraries/dht-sensor-library  
Adafruit Unified Sensor: https://www.arduinolibraries.info/libraries/adafruit-unified-sensor  
3.依據實際接線於IDE中設定需控制的pin與pinMode:  
```
#define DHTTYPE DHT22
#define WRELAY_PIN 6
#define DHT_PIN 22
#define MOISTURE_PIN A0 

#include <DHT.h>
#include <DHT_U.h>
DHT dht(DHT_PIN, DHTTYPE);
void setup() {
  pinMode(WRELAY_PIN,OUTPUT);
  pinMode(MOISTURE_PIN, INPUT);
  dht.begin();
}
```
4.定義讀取Raspberry pi指令之序列化函式  
```
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
```
5.將測得之土壤濕度與空氣溫溼度傳至Raspberry pi  
```
  float temp = dht.readTemperature();
  float humi = dht.readHumidity();
  float mois = analogRead(MOISTURE_PIN);
  Serial.print("[T:" + String(temp) + ":0,");
  Serial.print("H:" + String(humi) + ":0,");
  Serial.print("W:" + String(mois) + ":0," + "]");
```
6.讀取Raspberry pi指令，開啟或關閉繼電器(抽水馬達):  
```
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
```
### 二 Raspiberry pi 3
1.安裝opencv，參考網站:  
https://www.pyimagesearch.com/2019/04/08/openvino-opencv-and-movidius-ncs-on-the-raspberry-pi/  

2.使用Python獲取Arduino回傳訊息，必須安裝pySerial套件   
```
$ pip3 install pyserial
```
3.Python程式連結至Arduino，並讀取回傳內容  
```
ser = serial.Serial('/dev/ttyAMA0', 9600)
if ser.inWaiting:
    recv = ser.read(ser.inWaiting).decode('utf-8')
```

