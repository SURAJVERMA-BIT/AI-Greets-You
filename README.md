# AI Assistant

This project is an AI assistant that provides the current time, date, weather, motivational quotes, fun facts, and news headlines. The assistant uses text-to-speech (TTS) to greet the user and deliver the information.

## Features

- **Current Time and Date**: Get the current time and date in a readable format.
- **Weather**: Fetch the current weather for a specified city.
- **Motivational Quotes**: Receive a random motivational quote.
- **Fun Facts**: Learn a random fun fact.
- **News Headlines**: Hear the latest news headlines from India.

## Installation

1. **Clone the Repository**
   git clone https://github.com/SURAJVERMA-BIT/AI-Greets-You.git
   cd AI-Greets-You

2. **Install Dependencies**
Make sure you have Python installed, then install the required packages:
pip install pyttsx3 requests
3. **Set Up API Keys**

- **OpenWeatherMap API Key**: Sign up at OpenWeatherMap and get your API key.
- **NewsAPI Key**: Sign up at NewsAPI and get your API key.
Replace the placeholders in the script with your API keys:

OPENWEATHERMAP_API_KEY = 'your_openweathermap_api_key'
NEWSAPI_KEY = 'your_newsapi_key'
4. **Run the Script**

python ai_assistant.py

## Usage
When you run the script, the AI assistant will greet you and provide the following:

- The current time and date.
- The current weather for the specified city.
- A motivational quote.
- A fun fact.
- A random news headline from India.

## Customization
- Change the City: Update the city variable in the script to get weather information for a different location.
- Add More Quotes/Facts: You can add more motivational quotes and fun facts by updating the lists in the get_motivational_quote() and get_fun_fact() functions.
## Dependencies
- pyttsx3: A text-to-speech conversion library in Python.
- requests: A simple HTTP library for Python.
Install them using:

pip install pyttsx3 requests
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Feel free to submit issues, fork the repository, and send pull requests. Contributions are always welcome.

## Contact
For any questions or suggestions, feel free to reach out to {sv9052788@gmail.com}