#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

import json
import requests
import sys

APPID = 'put your key here!'

# Compute location based from cmd args
if len(sys.argv) < 2:
    print('Usage: weather-data.py city_name 2_letter_country_code')
    sys.exit()

location = ''.join(sys.argv[1:])

URL = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, APPID)
response = requests.get(URL)
response.raise_for_status()

#print(response)

weather_data = json.loads(response)
# Print weather descriptions
w = weather_data['list']

print('Current weather in {}:'.format(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])