from question_model import Question
from data import quiz_categories
from quiz_brain import QuizBrain
from art import logo
import random

print(logo)
print("🎉 Welcome to the Ultimate Quiz Challenge! 🎉")
print("\n📚 Choose your quiz category:")

for key, category in quiz_categories.items():
    print(f"{key}. {category['name']}")

while True:
    choice = input("\n🔢 Enter your choice (1-5): ")
    if choice in quiz_categories:
        selected_category = quiz_categories[choice]
        print(f"\n✨ You selected: {selected_category['name']} ✨")
        print("🎯 Get ready for 10 random questions!\n")
        break
    else:
        print("❌ Invalid choice! Please enter 1-5.")

question_bank = []
selected_questions = random.sample(selected_category['data'], 10)

for question in selected_questions:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("🎆 You've completed the quiz! 🎆")
print(f"🏆 Your final score was: {quiz.score}/{quiz.question_number}")

if quiz.score >= 8:
    print("🎉 Excellent! You're a quiz master! 🎉")
elif quiz.score >= 6:
    print("😊 Great job! Well done! 😊")
elif quiz.score >= 4:
    print("😐 Not bad! Keep practicing! 😐")
else:
    print("😔 Better luck next time! 😔")