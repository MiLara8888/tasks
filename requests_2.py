import requests
import time

text = 'http://api.openweathermap.org/data/2.5/weather'
params = {'q': input(), 'appid': '',
          'units': 'metric', 'lang': 'ru'}
res = requests.get(text, params=params)
res = res.json()

if res['cod'] == '404':
    print('Пожалуйста введите город')
elif res['cod'] == 200:
    temp = 'Сейчас - {}℃'.format(int(res['main']['temp']))
    feels_like = 'Ощущается как - {}℃'.format(int(res['main']['feels_like']))
    temp_min = 'Минимальная температура в городе - {}℃'.format(int(res['main']['temp_min']))
    temp_max = 'Максимальная температура в городе - {}℃'.format(int(res['main']['temp_max']))
    wind = 'Скорость ветра {}м/c'.format(round(float(res['wind']['speed'])), 1)
    weather = 'На улице - {}'.format(res['weather'][0]['description'])
    sunrise = 'Восход солнца - {}'.format(time.strftime('%X', time.localtime(res['sys']['sunrise'])))
    sunset = 'Заход солнца - {}'.format(time.strftime('%X', time.localtime(res['sys']['sunset'])))
    print(weather)
    print(temp)
    print(feels_like)
    print(temp_min)
    print(temp_max)
    print(wind)
    print(sunset)
    print(sunrise)
