from art import logo
print(logo)
import random
import time

EASY_LEVEL_TURNS = 10
MEDIUM_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess. Returns remaining turns."""
    if user_guess > actual_answer:
        print("😈 Too high! Try again...")
        print("")
        return turns - 1
    elif user_guess < actual_answer:
        print("🫣 Too low! Keep trying...")
        print("")
        return turns - 1
    else:
        print(f"🎉 Correct! The answer was {actual_answer}! You win! 🥳")
        return None  # End game


def set_difficulty():
    level = input("Choose a difficulty — Type 'easy' or 'medium' or'hard': ").lower()
    if level == "easy":
        print("🧘 Easy mode activated! You get 10 attempts.")
        return EASY_LEVEL_TURNS
    elif level == "medium":
        print("⚔️ Medium mode activated! You get 7 attempts.")
        return MEDIUM_LEVEL_TURNS
    elif level == "hard":
        print("🔥 Hard mode activated! Only 5 attempts!")
        return HARD_LEVEL_TURNS
    else:
        print("⚠️ Invalid choice! Defaulting to easy mode.")
        return EASY_LEVEL_TURNS


def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100... 🤔")
    time.sleep(1)
    print("Done ✅")
    print("🔢 Let's see if you can guess it!")
    number = random.randint(1, 100)
    # print(f"(DEBUG: The number is {number})")  # Uncomment for testing

    turns = set_difficulty()
    guess = 0

    while guess != number:
        print(f"\n💭 You have {turns} attempt(s) remaining...")
        print("")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, number, turns)

        if turns is None:
            break  # Player guessed correctly

        if turns == 0:
            print(f"💀 Game over! You've run out of guesses. The number was {number}.")
            print("😨 Better luck next time!")
            break
        elif turns <= 2:
            print("⚠️ Be careful! Only a few turns left... 😬")
        else:
            print("🔁 Guess again!")


# Run the game
number_guessing_game()
