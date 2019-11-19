from flask import Flask
import pymysql
import json
import datetime

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d-%H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def get_date_data(year,month,day):
    connection = pymysql.connect(host='172.16.3.3',
                                port=3306,
                                user='greenhouser',
                                password='greenhouser_test',
                                db='green_house',
                                cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(''' SELECT * FROM `test` 
    WHERE `DataTime` > '{}-{}-{} 00:00:00'
    AND `DataTime` <= '{}-{}-{} 23:59:00'; '''.format(year,month,day,year,month,day))
    data = cursor.fetchall()
    return data


app = Flask(__name__)

@app.route("/<year>/<month>/<day>", methods=['GET'])
def hello(year,month,day):
    data = get_date_data(year,month,day)
    return json.dumps(data,cls=DateEncoder,ensure_ascii=False).encode('utf8')

if __name__ == "__main__":
    app.run()