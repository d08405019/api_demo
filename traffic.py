from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
from requests import request
from pprint import pprint
import json
import math

app_id = 'FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF'
app_key = 'FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF'

class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'gzip'
        }


if __name__ == '__main__':
    a = Auth(app_id, app_key)
    response = request('get', 'https://ptx.transportdata.tw/MOTC/v3/Bus/Station/City/Tainan?$format=JSON', headers= a.get_auth_header())
    data = json.loads(response.text)
    my_lat = 24.035441
    my_lon = 121.499922
    min_result = 9999
    result_name = '台北'
    for station in data['Stations']:
        lat = station['StationPosition']['PositionLat']
        lon = station['StationPosition']['PositionLon']
        result = math.sqrt((my_lat-lat)*(my_lat-lat)+(my_lon-lon)*(my_lon-lon))
        # print(str(result))
        if min_result > result:
            min_result = result
            result_name = station['StationName']['Zh_tw']


    pprint(response.content)