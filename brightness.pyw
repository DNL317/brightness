
import screen_brightness_control as sbc
import datetime
from datetime import timezone
import json
import requests
import sys
from suntime import Sun
import time

def brightness():

    print("brightness running")
    send_url = "http://api.ipstack.com/check?access_key=68d6a43e7f37d2152f9bb7dc199b87ef"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']

    sun = Sun(latitude, longitude)

    today_sr = sun.get_sunrise_time()
    today_ss = sun.get_sunset_time()

    print(today_sr)
    print(today_ss)


    current_time = datetime.datetime.now(timezone.utc)
    while True:
        if today_ss > current_time > today_sr and sbc.get_brightness() != 100:
            sbc.fade_brightness(100, increment=3)
        elif current_time > today_ss and sbc.get_brightness() != 0:
            sbc.fade_brightness(0, increment=3)
            sys.exit()

# this part not working as intended. still debugging    
for i in range(25):
    print(f"{i}")
    try:
        brightness()
    except:
        time.sleep(10)
        continue
