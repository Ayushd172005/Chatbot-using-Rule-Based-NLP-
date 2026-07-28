import re
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

print("🤖 Chatbot: Hello! Type 'bye' to exit.")

rules = {
    r"hi|hello|hey": "Hello! How can I help you today?",
    r"how are you": "I'm doing great! How about you?",
    r"your name": "I am a rule-based chatbot built using Python.",
    r"help": "Sure! You can ask me about greetings, time, date, or basic info.",
    r"time": "I don't have a watch, but it's always a good time to learn!",
    r"date": "I can't track dates, but today is a great day to code!",
    r"thank you|thanks": "You're welcome! 😊",
    r"bye|exit|quit": "Goodbye! Have a nice day 👋"
}

def tokenize_text(text):
    """
    Tokenizes input sentence into words
    """
    tokens = word_tokenize(text.lower())
    return tokens

def generate_response(user_input):
    """
    Matches user input with regex rules
    """
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    return "Sorry, I didn't understand that. Can you rephrase?"

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("🤖 Chatbot:", rules[r"bye|exit|quit"])
        break

    tokens = tokenize_text(user_input)
    response = generate_response(user_input)

    print("🤖 Chatbot:", response)
