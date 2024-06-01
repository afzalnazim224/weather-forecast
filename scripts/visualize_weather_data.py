import os
import pandas as pd
import matplotlib.pyplot as plt

def visualize_weather_data():
    # Load CSV into DataFrame
    file_path = os.path.join('..', '', 'weather_forecast.csv')
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])

    # Plot Temperature Over Time
    plt.figure(figsize=(10, 5))
    plt.plot(df['Timestamp'], df['Temperature'], label='Temperature')
    plt.title('Temperature Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (K)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot Humidity Over Time
    plt.figure(figsize=(10, 5))
    plt.plot(df['Timestamp'], df['Humidity'], label='Humidity', color='orange')
    plt.title('Humidity Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Humidity (%)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    visualize_weather_data()
