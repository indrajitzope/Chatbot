import random
import re

# Predefined responses for the chatbot
responses = {
    "greeting": ["Hi there!", "Hello!", "Hey!", "Hi, how can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!", "Anytime!"],
    "default": ["I'm sorry, I didn't understand that.", "Could you rephrase that?", "I'm not sure I understand."],
}

# Keywords to match user input
patterns = {
    "greeting": r"\b(hi|hello|hey|howdy)\b",
    "goodbye": r"\b(bye|goodbye|see you|exit|quit)\b",
    "thanks": r"\b(thank you|thanks|much appreciated)\b",
}

def get_response(user_input):
    """
    Get a response based on user input.
    :param user_input: User's input string.
    :return: Response string from the chatbot.
    """
    for intent, pattern in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses[intent])
    return random.choice(responses["default"])

def main():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        if re.search(r"\b(exit|quit)\b", user_input, re.IGNORECASE):
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
