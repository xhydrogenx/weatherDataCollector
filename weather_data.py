import json

import requests


def get_weather_data(city):
    # создаем ендпоинт и список параметров для запроса
    baseurl = "https://api.weatherapi.com/v1/history.json"
    params = {"key": "d92e9a08d06d486984343743232410",
              "q": f"{city}",
              "dt": "2023-09-01",
              "end_dt": "2023-09-30"
              }
    try:
        # делаю запрос
        response = requests.get(baseurl, params=params)
        # проверка запроса на успех
        response.raise_for_status()
        # запись в переменную
        weatherdata = response.json()
        # пустой списоr для измененных данных
        newweatherdata = []

        # проходимся по forecastday и в каждом обьекте выбираем только город, день и среднесуточную температуру
        for forecastday in weatherdata["forecast"]["forecastday"]:
            # создание нового словаря в цикле
            simple_data = {
                "day": forecastday["date"],
                "avg_temp_c": forecastday["day"]["avgtemp_c"]
            }
            # записываю в пустой список словарь из simple_data для каждого объекта в forecastday
            newweatherdata.append(simple_data)
        # колхозим новый объект
        finalweather = {
            "location": {
                "city": weatherdata["location"]["name"]
            },
            "weather": newweatherdata
        }

        # создаю json
        with open('finalweather.json', 'w') as json_file:
            json.dump(finalweather, json_file, indent="  ", separators=(',', ':'))



    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    return None  # Возвращаем None в случае ошибки


get_weather_data("Novosibirsk")
