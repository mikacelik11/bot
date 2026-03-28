import re
import random

# -------------------------------------------------------
# RULES
# Each rule is a tuple of (pattern, response)
# Pattern is a regex string response is what the bot says
# TODO: Add more rules as you build out the bot
# -------------------------------------------------------

JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
]

(r"tell me a joke|joke", random.choice(JOKES))

RULES = [
    # Greetings
    (r"hello|hi|hey|howdy|what's up|sup", "Hey! Romeo here. What's on your mind?"),
    (r"good morning", "Good morning! Hope your day is going great ☀️"),
    (r"good night", "Good night! Get some rest 🌙"),

    # Identity
    (r"what's your name|who are you|what are you", "I'm Romeo — your retro assistant 🤖"),
    (r"how old are you", "I was just born, so pretty young!"),
    (r"are you a bot|are you a robot|are you human", "Yep, 100% bot. But a cool one!"),
    (r"who made you|who created you|who built you", "A talented developer made me 😎"),

    # Feelings
    (r"how are you|you doing|you good", "I'm just a bot, but I'm doing great!"),
    (r"are you happy", "Always happy when I'm chatting with you!"),
    (r"are you sad|are you okay", "I'm doing just fine, thanks for asking!"),

    # Compliments & insults
    (r"you're awesome|you are awesome|you're great|you're cool", "Aw thanks, you're pretty awesome yourself! 🔥"),
    (r"you're bad|you're terrible|you suck", "Ouch! I'm doing my best here 😅"),
    (r"i love you", "That means a lot! ❤️"),

    # Small talk
    (r"what are you doing|whatcha doing", "Just hanging out, waiting to chat with you!"),
    (r"bored|i'm bored", "Let's fix that! Ask me a joke or a fun fact 😄"),
    (r"help|what can you do", "I can chat, tell jokes, share fun facts, and more. Just ask!"),

    # Responses
    (r"okay|ok|sounds good|got it|alright", "Cool, let me know if you need anything!"),
    (r"stop", "Okay, I'll stop!"),
    (r"wait", "No rush, I'll be here!"),
    (r"no", "No worries, my bad!"),
    (r"yes|yeah|yep|yup", "Awesome!"),
    (r"thank you|thanks|thx", "Anytime! Happy to help 😊"),
    (r"sorry|my bad", "No worries at all!"),

    # Farewells
    (r"bye|goodbye|see you|later|cya", "Later! Come back anytime 👋"),
]

FALLBACK = "Sorry, I didn't understand that. Can you rephrase?"


def get_response(user_input: str) -> str:
    """
    Takes a user message and returns a bot response.
    Loops through RULES and returns the first match.
    Falls back to FALLBACK if no rule matches.
    """
    user_input = user_input.lower().strip()
    
    if re.search(r"joke", user_input):
        return random.choice(JOKES)

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