import re

# -------------------------------------------------------
# RULES
# Each rule is a tuple of (pattern, response)
# Pattern is a regex string response is what the bot says
# TODO: Add more rules as you build out the bot
# -------------------------------------------------------
RULES = [
    (r"hello|hi|hey", "Hey there! How can I help you?"),
    (r"how are you", "I'm just a bot, but I'm doing great!"),
    (r"bye|goodbye", "Goodbye! Have a great day!"),
    (r"stop", "Okay, I will stop!")
    (r"what's your name?", "My name is Romeo")
    (r"wait", "Okay")
    # TODO: Add your own rules here
    # (r"your pattern", "your response"),
]

FALLBACK = "Sorry, I didn't understand that. Can you rephrase?"


def get_response(user_input: str) -> str:
    """
    Takes a user message and returns a bot response.
    Loops through RULES and returns the first match.
    Falls back to FALLBACK if no rule matches.
    """
    user_input = user_input.lower().strip()

    for pattern, response in RULES:
        if re.search(pattern, user_input):
            return response

    # TODO: Optionally add context-aware logic here later
    return FALLBACK


# Quick test — run `python bot.py` to verify your rules work
if __name__ == "__main__":
    print("Bot test mode. Type 'quit' to exit.\n")
    while True:
        msg = input("You: ")
        if msg.lower() == "quit":
            break
        print(f"Bot: {get_response(msg)}\n")