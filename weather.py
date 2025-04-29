import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(data):
    if data.get("cod") != 200:
        print("City not found or error fetching data.")
        return
    city = data['name']
    temp = data['main']['temp']
    weather = data['weather'][0]['description']
    humidity = data['main']['humidity']
    print(f"\nWeather in {city}:")
    print(f"Temperature : {temp}°C")
    print(f"Condition : {weather}")
    print(f"Humidity : {humidity}%")

if __name__ == "__main__":
    print("=== Weather App ===")
    api_key = input("Enter your OpenWeatherMap API Key: ")
    city = input("Enter city name: ")
    data = get_weather(city, api_key)
    display_weather(data)