# get_fileData_to_mySQL
# 如何使用

0. 進入資料夾
```
cd get_fileData_to_mySQL
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
    pip3 -r install requirements.txt
```
4. 執行指令
```
    python3 main.py ./main.csv
```

# 補充說明

0. 資料欄位(詳情請看main.csv)
```
    (資料表)db_table,test
    (資料欄位)db_column,DataTime,OutdoorSunshine,IndoorSunshine,OutdoorTemperature,IndoorTemperature,Rainwater,RelativeHumidity,OutdoorWindSpeed
    (需要impoert的文件副檔名)file_tag,csv
    (資料夾放的路徑)data_dir,/Users/dingding/Documents/get_fileData_to_mySQL/data
    (刪除資料內特殊文字)deletes,0x, 20.818:30
```