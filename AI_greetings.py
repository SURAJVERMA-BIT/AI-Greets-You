import pyttsx3
from datetime import datetime
import random
import requests

# Replace with your own API keys
OPENWEATHERMAP_API_KEY = 'c718f893cc502544c6bfd13e191ee80f'
NEWSAPI_KEY = '8b39c74f6fde4287a6dcf5f4adf4779a'

def speak(message):
    """Speak a given message using the TTS engine."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    engine.say(message)
    engine.runAndWait()

def get_current_time():
    """Get the current time in a readable format."""
    now = datetime.now()
    return now.strftime("%I:%M %p")

def get_current_date():
    """Get the current date in a readable format."""
    now = datetime.now()
    return now.strftime("%A, %B %d, %Y")

def get_weather(city):
    """Fetch the current weather for a given city."""
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(weather_url)
    data = response.json()

    if data.get("cod") != 200:
        return "Sorry, I couldn't retrieve the weather information."
    
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    return f"The current weather in {city} is {weather} with a temperature of {temperature}°C."

def get_motivational_quote():
    """Return a random motivational quote."""
    quotes = [
        "The only way to do great work is to love what you do. -said by Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. - said by Albert Schweitzer",
        "Don't watch the clock; do what it does. Keep going. - said by Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - said by Eleanor Roosevelt",
        "Believe you can and you're halfway there. - said by Theodore Roosevelt"
    ]
    return random.choice(quotes)

def get_fun_fact():
    """Return a random fun fact."""
    facts = [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
        "Bananas are berries, but strawberries aren't.",
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
        "A day on Venus is longer than a year on Venus.",
        "Humans share 50% of their DNA with bananas."
    ]
    return random.choice(facts)

def get_news():
    """Fetch the latest news headlines for India."""
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWSAPI_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok":
        return "Sorry, I couldn't retrieve the news."

    articles = data["articles"]
    if not articles:
        return "Sorry, I couldn't find any news articles."

    top_article = random.choice(articles)  # Pick a random article to read
    headline = top_article["title"]
    return f"In today's news: {headline}"

def main():
    """Main function to run AI greeting."""
    try:
        current_time = get_current_time()
        current_date = get_current_date()
        quote = get_motivational_quote()
        fun_fact = get_fun_fact()
        city = "Mungher, Bihar, India"
        weather = get_weather(city)
        news = get_news()

        greeting = (
            f"Hello sir. The current time is {current_time} on {current_date}. "
            f"{weather} "
            f"Here's your motivational quote for the day: {quote}. "
            f"And now, a fun fact: {fun_fact}. "
            f"{news} "
            f"Is there anything else I could assist you with today, sir?"
        )

        speak(greeting)
    except Exception as e:
        speak("I may have encountered an error while processing your request. Please try again later, sir.")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
