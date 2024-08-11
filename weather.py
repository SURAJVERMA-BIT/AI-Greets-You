import requests
OPENWEATHERMAP_API_KEY = 'c718f893cc502544c6bfd13e191ee80f'
city = "Munger, Bihar, India"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"

def get_weather(city):
    """Fetch the current weather for a given city."""
    response = requests.get(weather_url)
    data = response.json()

    if data.get("cod") != 200:
        return "Sorry, I couldn't retrieve the weather information."
    
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    return f"The current weather in {city} is {weather} with a temperature of {temperature}°C."

# Example usage
print(get_weather(city))
