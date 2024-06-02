import requests
import pandas as pd
import time
import os

API_KEY = 'Replace with your OpenWeatherMap API key'  
CITY = 'London'
latitude = 52.6309
longitude = 1.2974
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API_KEY}'
# URL = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={API_KEY}'


def fetch_weather_data():
    response = requests.get(URL)
    data = response.json()
    
    weather_data = {
        'Timestamp': pd.Timestamp.now(),
        'Temperature': data['main']['temp'],
        'Humidity': data['main']['humidity'],
        'Pressure': data['main']['pressure'],
        'Weather': data['weather'][0]['description'],
        'Wind Speed': data['wind']['speed']
    }
    
    df = pd.DataFrame([weather_data])
    
    # Save to CSV
    file_path = os.path.join('..', 'data', 'weather_data.csv')
    write_header = not os.path.isfile(file_path)
    df.to_csv(file_path, mode='a', header=write_header, index=False)

if __name__ == '__main__':
    while True:
        fetch_weather_data()
        print("Weather data fetched and saved.")
        # Wait for 1 hour before next update
        time.sleep(60)
