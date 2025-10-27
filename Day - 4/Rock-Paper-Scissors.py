import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

print("Welcome to ROCK, PAPER, SCISSORS")
print("what do you choose? 0 for rock, 1 for paper, 2 for scissors")
user_choice = int(input("Enter your choice: "))
user = print(game[user_choice])
computer_choice = random.randint(0, 2)
print(f"Computer Choose:")
print(game[computer_choice])

if user_choice == computer_choice:
    print("TIE")
elif user_choice == 0 and computer_choice == 1:
    print("Computer Win")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
elif user_choice == 1 and computer_choice == 2:
    print("Computer Win")
elif user_choice == 1 and computer_choice == 0:
    print("You Win")
elif user_choice == 2 and computer_choice == 1:
    print("You Wins")
elif user_choice == 2 and computer_choice == 0:
    print("Computer Wins")
else:
    print("Invalids number")
