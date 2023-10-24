from weather_data import get_weather_data
from data_processing import create_csv

if __name__ == "__main__":
    city = "Novosibirsk"
    weather_data = get_weather_data(city)
    create_csv(weather_data, "weather_data.csv")