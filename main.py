import sys
import os
import csv
import pymysql


def list_to_csv(FileName,FileList):
    for row_index, list in enumerate(FileList):
        for column_index, string in enumerate(list):
            FileList[row_index][column_index] = FileList[row_index][column_index]
    with open(FileName, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(FileList)


def csv_to_list(fileName):
    data = []
    with open(fileName, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            tmp = (', '.join(row)).replace(' ','').replace('%','').split(',')
            data.append(tmp)
    return data


# 把列出資料夾的程式碼寫成一個函式
def show_folder_content(folder_path,isWindows=False,isDesignation=False,Designation=[]):
    data = []
    # 判別是否是資料夾
    if os.path.isdir(folder_path):
        print(folder_path + '讀取資料夾內容')
    else:
        print("error,{} is not dir".format(folder_path))
        return "error,folder_path is not dir"
    
    # 設定路徑的分隔符號
    IdentificationSymbol = '/'
    if isWindows:
        IdentificationSymbol = '\\'
    
    # 開始裝填檔案路徑名稱
    folder_content = os.listdir(folder_path)
    for item in folder_content:
        if os.path.isdir(folder_path + IdentificationSymbol + item):

            # 呼叫自己處理這個子資料夾
            tmp_data = show_folder_content(folder_path + IdentificationSymbol + item)
            for line in tmp_data:
                data.append(line)
        elif os.path.isfile(folder_path + IdentificationSymbol + item):
            tmp_file_path = folder_path + IdentificationSymbol + item
            if isDesignation:
                for line in Designation:
                    if( item.find(line) != -1):
                        data.append(tmp_file_path)
            else:
                data.append(tmp_file_path)
        else:
            print('無法辨識： ' + folder_path + IdentificationSymbol + item)
    return data 

def get_onFilePathOfdate(file_path):
    tmp = file_path.split('/')
    tmp = tmp[-1].split('.')
    return tmp[0]

def update_TimeofList(date,index,origin_list,deletes):
    data = []
    for line in origin_list:
        for column in line:
            for delete in deletes:
                if (column.find(delete) != -1):
                    origin_list.remove(line)
    for line in origin_list:
        line[index] = '{} {}'.format(date,line[index])
        data.append(tuple(line))
    return data

    

# 驗證參數指令數目
if (len(sys.argv) != 2):
    print("error, parameter. it's like```python3 main.py <main_setting_filePath>```")
    sys.exit()

# 驗證設定檔案路徑是否正確
main_setting_path = sys.argv[1]
if (not os.path.isfile(main_setting_path)):
    print("error, {} is a dir or not a ture path".format(main_setting_path))
    sys.exit()
if (main_setting_path.find(".csv") == -1):
    print("error, {} is not a csv file")
    sys.exit()

# 
main_setting = csv_to_list(main_setting_path)
obj_title = [
    'db_table',
    'db_column',
    'file_tag',
    'data_dir',
    'deletes',
]
obj_setting = {}
if (len(main_setting) != len(obj_title)):
    print("error, main_setting amd obj_title are len not match")
    sys.exit()

for index,line in enumerate(main_setting):
    obj_setting[obj_title[index]] = line[1:]


data_list = show_folder_content(obj_setting['data_dir'][0],False,True,obj_setting['file_tag'])


connection = pymysql.connect(host='172.16.3.3',
                             port=3306,
                             user='greenhouser',
                             password='greenhouser_test',
                             db='green_house',)


executemany_string = 'INSERT INTO `{}` ({}) VALUES ({})'
executemany_string = executemany_string.format(obj_setting['db_table'][0],'{}','{}')
max_len = len(obj_setting['db_column'])-1

for index,value in enumerate(obj_setting['db_column']):
    if index == max_len:
        executemany_string = executemany_string.format(value,'%s')
    else:
        executemany_string = executemany_string.format(('{},{}'.format(value,{})),('{},{}'.format('%s','{}')))

for data_file_path in data_list:
    executemany_list = None
    tmp_csv_data_list = csv_to_list(data_file_path)
    tmp_csv_date = get_onFilePathOfdate(data_file_path)
    executemany_list = update_TimeofList(tmp_csv_date,0,tmp_csv_data_list,obj_setting['deletes'])

    cursor = connection.cursor()
    effect_row = cursor.executemany(executemany_string,executemany_list)
    try:
        connection.commit()
    except:
        print("error,connection.commit")
    else:
        print('insert done {}'.format(data_file_path))

# data_file_path = '/Users/dingding/Documents/get_fileData_to_mySQL/data/2018-10-08.csv'
# tmp_csv_data_list = csv_to_list(data_file_path)
# tmp_csv_date = get_onFilePathOfdate(data_file_path)
# executemany_list = update_TimeofList(tmp_csv_date,0,tmp_csv_data_list)
# cursor = connection.cursor()
# effect_row = cursor.executemany(executemany_string,executemany_list)
# connection.commit()