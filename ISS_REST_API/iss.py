import requests
import json
from conf import API_key, username

def query():
    res = requests.get('http://api.open-notify.org/iss-now.json')
    res = res.json()
    lat = res['iss_position']['latitude']
    lng = res['iss_position']['longitude']
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={API_key}&units=metric')
    weather = weather.json()
    temp = float(weather['main']['temp'])
    temp = round(temp, 1)
    try:
        res = requests.get(f'http://api.geonames.org/countrySubdivisionJSON?lat={lat}&lng={lng}&username={username}')
        res = res.json()
        location = res['countryName']
    except:
        res = requests.get(f'http://api.geonames.org/oceanJSON?lat={lat}&lng={lng}&username={username}')
        res = res.json()
        location = res['ocean']['name']

    json_form = json.dumps({'location':location,
                            'temp':temp})
    str_form = f'ISS is over {location} and the temperature is {temp} °C'
    res_dict = {'json': json_form, 'text': str_form}
    return res_dict