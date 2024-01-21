import weather
import os
from dotenv import load_dotenv
import json

load_dotenv()


def main():
    
    # Used in the forecast function.
    lat = float()
    lon = float()

    # Taking user input 
    user_input = input("Please enter the city name: ")

    # Retrieving OpenWeatherMap API key from environment variables
    api_key = os.getenv("API_KEY")

    # Base URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Base URL for OpenWeatherMap Forecast API
    forecast_url = "http://api.openweathermap.org/data/2.5/forecast"

    # Calling the weatherData function from the weather file.
    data = weather.weatherData(base_url, user_input, api_key)

    # This can get the weather forecast for next five days.

    # Check respone data
    if data is not None:
        
        with open('weather.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
        # print(f"weather data for {user_input} is {data}")

        # Getting the data for forecast URL
        lat += data["coord"]["lat"]
        lon += data["coord"]["lon"]

    # Calling the forecast function from the weather file.
    forecast_data = weather.forecast(api_key, forecast_url, lat, lon,user_input)

    if forecast_data != None:
        with open('forecast.json', 'w') as json_file:
            json.dump(forecast_data, json_file, indent=2)
        # print(f"weather Forecast for {user_input} is {forecast_data}")


if __name__ == "__main__":
    main()
