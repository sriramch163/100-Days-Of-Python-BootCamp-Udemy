import random
from game_data import data
from art import logo, vs

print(logo)

def format_data(anime):
    """Takes the anime data and returns the printable format"""
    anime_name = anime["name"]
    anime_description = anime["description"]
    anime_origin = anime["origin"]
    return f"🌟 {anime_name} — {anime_description} 🌀 (from {anime_origin})"

def check_answer(guess, a_power_level, b_power_level):
    """Take the user guess and the power levels and returns if they have more or not"""
    if a_power_level > b_power_level:
        return guess == "a"
    else:
        return guess == "b"

score = 0
anime_b = random.choice(data)

end_game = True
while end_game:

    anime_a = anime_b
    anime_b = random.choice(data)

    if anime_b == anime_a:
        anime_b = random.choice(data)

    print("⚔️  Battle Arena ⚔️")
    print(f"\n👊 Compare A : {format_data(anime_a)}")
    
    print(vs)
    print(f"🔥 Against B : {format_data(anime_b)}\n")
    

    guess = input("💭 Who has more power? Type 'A' or 'B' ➤   ").lower()

    print("\n" * 20)
    print(logo)

    a_power_level = anime_a["power_level"]
    b_power_level = anime_b["power_level"]

    is_correct = check_answer(guess, a_power_level, b_power_level)

    if is_correct:
        score += 1
        print(f"✅ Correct! ✨ Current Score: {score}\n")
        print("💪 You sense your anime spirit growing stronger!\n")

    else:
        print("\n" * 10)
        print(f"💥 Wrong choice! 😭 Final Score: {score}\n")
        print(f"🔹 {anime_a['name']} had Power {a_power_level}")
        print(f"🔹 {anime_b['name']} had Power {b_power_level}\n")
        print("🎴 Game Over — Your anime journey ends here!\n")
        end_game = False
