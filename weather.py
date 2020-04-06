import json
import requests
city_name=input("which city report do you want:")
apikey="40d439259718ef3f486d5ccb188390f5"
link="http://api.openweathermap.org/data/2.5/weather?"
complete_link=link + "q=" + city_name + "&appid=" + apikey
response=requests.get(complete_link).json()
print(f'The weather condition of {city_name} is {response["weather"][0]["description"]}.')
y=response["main"]["temp"]

temp_in_centigrade=(y-32)*5/9
print(f'The current temperature of {city_name} is {temp_in_centigrade}')

