import json
import requests

weatherapi_baseurl = "https://api.weatherapi.com/v1"


def get_weather_data(city: str) -> None:
    # создаем ендпоинт и список параметров для запроса

    params = {
        "key": "d92e9a08d06d486984343743232410",
        "q": city,
        "dt": "2023-09-01",
        "end_dt": "2023-09-30"
    }

    # делаю запрос
    response = requests.get(f"{weatherapi_baseurl}/history.json", params=params)
    # проверка запроса на успех
    response.raise_for_status()
    # запись в переменную
    weatherdata = response.json()
    # пустой список для измененных данных
    final_weather = {
        "location": {
            "city": weatherdata["location"]["name"]
        },
        "weather": []
    }

    # проходимся по forecast_day и в каждом объекте выбираем только город, день и среднесуточную температуру
    for forecast_day in weatherdata["forecast"]["forecastday"]:
        # создание нового словаря в цикле
        simple_data = {
            "day": forecast_day["date"],
            "avg_temp_c": forecast_day["day"]["avgtemp_c"]
        }
        # записываю в пустой список словарь из simple_data для каждого объекта в forecast_day
        final_weather["weather"].append(simple_data)

    # создаю json
    with open('finalweather.json', 'w') as json_file:
        json.dump(final_weather, json_file, indent="  ", separators=(',', ':'))


if __name__ == "__main__":
    get_weather_data("Novosibirsk")
