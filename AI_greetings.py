import pyttsx3
from datetime import datetime
import random
import requests  # For future enhancement if APIs are added

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

def get_motivational_quote():
    """Return a random motivational quote."""
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt"
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
    """Return a random news headline."""
    news = [
        "In today's news, scientists have made a groundbreaking discovery in renewable energy.",
        "Tech stocks are on the rise as companies report higher than expected earnings.",
        "A new study shows that daily exercise can significantly improve mental health.",
        "In sports, the local team won their championship game in a thrilling overtime victory.",
        "The city is planning to expand public transportation options to reduce traffic congestion."
    ]
    return random.choice(news)

def main():
    """main function to run AI greeting."""
    try:
        current_time = get_current_time()
        current_date = get_current_date()
        quote = get_motivational_quote()
        fun_fact = get_fun_fact()
        news = get_news()

        greeting = (
            f"Hello sir. The current time is {current_time} on {current_date}. "
            f"The weather is clear with a high of 25 degrees Celsius."
            f",so.  Here's your motivational quote for the day: {quote}. "
            f"And now, a fun fact which you may not know is : {fun_fact}. "
            f"In today's news: {news}. "
            f"Is there anything else I could assist you with sir ?"
        )

        speak(greeting)
    except Exception as e:
        speak("I may have encountered an error while processing your request. Please try again later sir.")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
