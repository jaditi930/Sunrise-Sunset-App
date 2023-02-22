import json
import requests
from geopy.geocoders import Nominatim
from datetime import datetime
import pandas

appid= 'a6962678a5cba51e8db12b46bc87a867'

def convert_unix_time(time):
    datetime_obj = datetime.fromtimestamp(time)
    return f"{datetime_obj.hour}:{datetime_obj.minute}:{datetime_obj.second}"

def get_lat_and_long(zipcode):
    try:
    # get latitude and longitude from zipcode 
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(zipcode)
        latitude = location.latitude
        longitude = location.longitude
        output=get_data_and_format(latitude,longitude) 
    except:
        output={}
    return output

def get_data_and_format(latitude,longitude):
    # call api and convert data into python object
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={appid}"
    r = requests.get(api)
    content = r.content
    data = json.loads(content)

    # store required data in new dict
    output = {}
    if r.status_code == 200:
        output["status"] = 'ok'
        output["rise"] = convert_unix_time(data['sys']['sunrise'])
        output["set"] = convert_unix_time(data['sys']['sunset'])
        output["riseunix"] = data['sys']['sunrise']
        output["setunix"] = data['sys']['sunset']
    else:
        output["status"] = 'not ok'
        output["rise"] = 'None'
        output["set"] = 'None'
        output["riseunix"] = 'None'
        output["setunix"] = 'None'
    return output
