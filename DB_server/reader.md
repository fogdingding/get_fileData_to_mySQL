# 如何使用

0. 進入資料夾
```
cd DB_server
```
1. 確保有python3
```
    python3 --version
```
2. 確保有pip3
```
    pip3 --version
```
3. 透過pip3來進行安裝(flask, pymysql)
```
    pip -r requirements.txt
```
4. 執行指令
```
    python3 app.py
```
5. 打開瀏覽器輸入
```
    127.0.0.1:5000/2019/07/20
```
```
    GET
    localhost:5000/year/month/day
```
6. 您就會看到資料了

# 補充說明

0. 資料型態
```
[
    {
        "Id": 626696,
        "DataTime": "2019-07-21 00:01:00",
        "OutdoorSunshine": 0.0,
        "IndoorSunshine": 24.4,
        "OutdoorTemperature": 0.0,
        "IndoorTemperature": 0.0,
        "Rainwater": 24.4,
        "RelativeHumidity": 99.0,
        "OutdoorWindSpeed": 0.4
    }, 
    {
        "Id": 626697,
        "DataTime": "2019-07-21 00:02:00",
        "OutdoorSunshine": 0.0,
        "IndoorSunshine": 24.4,
        "OutdoorTemperature": 0.0,
        "IndoorTemperature": 0.0,
        "Rainwater": 24.4,
        "RelativeHumidity": 99.0,
        "OutdoorWindSpeed": 0.4
    }
]
```
1. 需要連線至公司VPN喔！