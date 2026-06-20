import random

def get_random_quote(quotes):
    return random.choice(quotes) if quotes else ""
