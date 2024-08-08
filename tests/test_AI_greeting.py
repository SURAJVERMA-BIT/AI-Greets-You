import unittest
from AI_greetings import get_current_time, get_current_date, get_motivational_quote, get_fun_fact, get_news

class TestAIGreetings(unittest.TestCase):

    def test_get_current_time(self):
        self.assertIsInstance(get_current_time(), str)

    def test_get_current_date(self):
        self.assertIsInstance(get_current_date(), str)

    def test_get_motivational_quote(self):
        self.assertIn(get_motivational_quote(), [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
            "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "Believe you can and you're halfway there. - Theodore Roosevelt"
        ])

    def test_get_fun_fact(self):
        self.assertIn(get_fun_fact(), [
            "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
            "Bananas are berries, but strawberries aren't.",
            "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
            "A day on Venus is longer than a year on Venus.",
            "Humans share 50% of their DNA with bananas."
        ])

    def test_get_news(self):
        self.assertIn(get_news(), [
            "In today's news, scientists have made a groundbreaking discovery in renewable energy.",
            "Tech stocks are on the rise as companies report higher than expected earnings.",
            "A new study shows that daily exercise can significantly improve mental health.",
            "In sports, the local team won their championship game in a thrilling overtime victory.",
            "The city is planning to expand public transportation options to reduce traffic congestion."
        ])

if __name__ == "__main__":
    unittest.main()
