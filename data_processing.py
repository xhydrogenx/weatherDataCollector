import csv
import weather_data  # Импортируйте модуль, в котором определена функция get_weather_data

# Вызов функции get_weather_data для получения данных
weatherdata = weather_data.get_weather_data("Novosibirsk")  # Замените "YourCity" на название вашего города

def create_csv(weatherdata):
    weatheroutput = "weather_data.csv"  # Создаем имя файла внутри функции
    try:
        with open(weatheroutput, 'w', newline='') as weather_csv:
            csv_writer = csv.writer(weather_csv)
            if weatherdata:
                header = weatherdata[0].keys()
                csv_writer.writerow(header)

                for entry in weatherdata:
                    csv_writer.writerow(entry.values())
                print(f"Данные записаны в csv: {weatheroutput}")
            else:
                print(f"Данные не записаны")

    except Exception as ex:
        print(f'Произошла ошибка: {str(ex)}')

# Теперь передайте weatherdata в функцию create_csv
create_csv(weatherdata)
