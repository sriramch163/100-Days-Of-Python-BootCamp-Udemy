import random 


def random_waiter(waiters):
    """Select a random waiter from the list of waiters."""
    return random.choice(waiters)




def random_quote():
    quotes = [
        "Good food takes time, please be patient!",
        "Cooking is an art — perfection in progress!",
        "Your dish is being crafted with love ❤️",
        "Smells delicious already!",
        "Happiness is homemade!",
        "Sizzling magic in progress 🔥"
    ]
    return random.choice(quotes)