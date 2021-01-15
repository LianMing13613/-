# IoT Proposal 智慧澆水系統

## 概述
智慧澆水系統會持續偵測並記錄盆栽土壤濕度，在土壤過乾時，自動逕行澆水。  

## 功能

時間設定:透過手機設定智慧盆栽系統開啟時段  
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

## 步驟
### 一 Arduino開發版接線
接上RFLINK-UART無線序列傳輸模組![image](https://github.com/LianMing13613/-/tree/main/picture/RFlink.jpg)  
接上土壤濕度感測器  
![image](https://github.com/LianMing13613/-/tree/main/picture/土壤濕度.jpg)  
接上DHT-22  
![image](https://github.com/LianMing13613/-/tree/main/picture/DHT22.jpg)  
接上繼電器  
![image](https://github.com/LianMing13613/-/tree/main/picture/繼電器.jpg)  
### 二 Raspberry pi 3 接線  
![image](https://github.com/LianMing13613/-/tree/main/picture/RFlink.jpg)  
