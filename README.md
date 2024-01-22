# Weather-Forecast

To run the code, follow the steps below:

1. **Create a Virtual Environment:**
    a. Install virtualenv:
       pip install virtualenv

    b. Create a virtual environment named `virtualEnv`:
       python -m venv virtualEnv

    c. Activate the virtual environment:
       virtualEnv\Scripts\activate
       

2. **Add OpenWeatherMap API Key:**
    - Create a file named `.env` in the project directory.
    - Add your OpenWeatherMap API key to the `.env` file:

      api_key = `your_api_key`
      
      Use this api key
      `api_key = '49be92bf0230b1709b927ad1e9157e62'`

3. **Install Required Libraries:**
   
    pip install -r requirements.txt
    
4. **Run the Code:**
    a. Execute the following command:
       python main.py
       
    b. Enter the city name as prompted and press enter.

5. **Retrieve Weather Data:**
   - The code will make an API call to OpenWeatherMap and provide you with the current weather data and a 5-day weather forecast.
   - The weather information is then stored in a JSON file for further reference.

Make sure to replace `your_api_key` in the `.env` file with your actual OpenWeatherMap API key. Additionally, activate the virtual environment before running the code.

    
