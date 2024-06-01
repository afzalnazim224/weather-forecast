import requests
import csv
from datetime import datetime, timedelta

def fetch_weather_forecast(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data["list"]

def write_to_csv(forecast_data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Temperature (°C)', 'Humidity (%)', 'Weather']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for forecast in forecast_data:
            date = datetime.fromtimestamp(forecast["dt"]).strftime('%Y-%m-%d')
            temperature = forecast["main"]["temp"]
            humidity = forecast["main"]["humidity"]
            weather = forecast["weather"][0]["description"]
            writer.writerow({'Date': date, 'Temperature (°C)': temperature, 'Humidity (%)': humidity, 'Weather': weather})

def main():
    api_key = '86690017307a1dab1d834fd6853c8cf2'
    city = 'London'  # Replace with your city
    output_file = 'weather_forecast.csv'
    forecast_data = fetch_weather_forecast(api_key, city)
    write_to_csv(forecast_data, output_file)

if __name__ == "__main__":
    main()