'''Используя сервис OpenWeatherMap, 
   в коде реализована программа, которая показывает
   погоду, влажность и давление в указанном городе "city_name".'''

import requests
import json

print("TASK 1")

def weather_repo(city_name, api_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
    
    if response.status_code != 200:
        print("An error happened")
        return None

    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    return weather, temperature, humidity, pressure

def main():
    city_name = 'Naypyidaw'
    api_key = 'b99f47a70a2917d12795aa7c91431a16'
    
    weather_info = weather_repo(city_name, api_key)
    if weather_info:
        weather, temperature, humidity, pressure = weather_info
        print(f'Город: {city_name}')
        print(f'Погода: {weather},\n Температура: {temperature} Келвин(K),\n Влажность: {humidity} %,\n Давление: {pressure} hPa')
        print('_'* 50)
    else:
        print("Error happened during processing")

if __name__ == "__main__":
    main()

'''Код формирует запрос (по api веб-сайта) с параметрами и получает ответ в формате .json.
Исследует данные, которые можно получить с помощью api
Создает структурированный вывод информации'''

print("TASK 2")

def character_info(name):
    url = f'https://rickandmortyapi.com/api/character/?name={name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()

    else:
        print(f'failed with status code {response.status_code}')
        return None

def main():
    character_name = "Nick"
    request_result = character_info(character_name)

    for character in request_result['results']:
        print(json.dumps({
            "Name": character['name'],
            "Gender": character['gender'],
            "Status": character['status'],
            "Location": character['location']['name'],
            "Species": character['species'],
            "Type": character['type'] if character['type'] else 'N/A'
        }, indent=4))

if __name__ == '__main__':
    main()   
   





