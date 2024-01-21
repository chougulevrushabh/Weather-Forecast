import requests


def weatherData(base_url, city_name, api_key):
    if city_name != "" and api_key != "":
        url = f"{base_url}?q={city_name}&APPID={api_key}&units=metric"
        print(f"weather url is : {url}")

        try:
            # Make the API call
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                response.raise_for_status()

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}")

        except Exception as e:
            # Handle any other exceptions
            print(f"An unexpected error occurred: {e}")

    else:
        print("Please enter both correct City name and API Key")


def forecast(api_key, forecast_url, lat, lon,city_name):
    print(city_name,"---")
    if  city_name != "" and api_key != "" :
        url = f"{forecast_url}?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        print(f"Forecast url is : {url}")

        try:
            # Make the API call
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                response.raise_for_status()

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}")
    else:
        print("Please enter both correct City name and API Key")