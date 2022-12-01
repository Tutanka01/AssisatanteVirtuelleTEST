from calendar import c
from turtle import st
import requests
from pprint import pprint
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=secret_monreuf&units=metric'.format("ville !")
res = requests.get(url)
data = res.json()

# wind_speed = data['wind']['speed']
# describe = data['weather'][0]['description']
# feels_like_temp = int(data['main']['feels_like'])
# humidity = data['main']['humidity']
# cloudy = data['clouds']['all']  #Le donne en pourcentage de couverture nuageuse

def temperature():
    temp = data['main']['temp']
    temp = str(temp)
    return temp
def vent():
    wind_speed = data['wind']['speed']
    wind_speed = str(wind_speed)
    return wind_speed
def temp_resentie():
    feels_like_temp = int(data['main']['feels_like'])
    feels_like_temp = str(feels_like_temp)
    return feels_like_temp
def humidite():
    humidity = data['main']['humidity']
    humidity = str(humidity)
    return humidity
def nuages():
    cloudy = data['clouds']['all']
    cloudy = str(cloudy)
    return cloudy
def description():
    describe = data['weather'][0]['description']
    return describe
