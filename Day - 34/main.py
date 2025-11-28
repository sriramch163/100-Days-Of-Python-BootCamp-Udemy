from tkinter import *
from tkinter import ttk
from question_model import Question
from data import quiz_categories
from quiz_brain import QuizBrain
from ui import QuizInterface
from art import logo
import random

player_name = ""


def start_quiz():
    global player_name
    selected = category_choice.get()
    player_name = name_input.get()

    if not selected:
        status_label.config(text="⚠ Please select a category!", fg="red")
        return
    if player_name.strip() == "":
        status_label.config(text="⚠ Please enter your name!", fg="red")
        return

    questions = random.sample(quiz_categories[selected]["data"], 10)
    question_bank = [Question(q["text"], q["answer"]) for q in questions]

    selection_window.destroy()
    QuizInterface(QuizBrain(question_bank), player_name, quiz_categories[selected]["name"])


selection_window = Tk()
selection_window.title("QUIZ GAME")
selection_window.config(padx=45, pady=35, bg="#0F0F0F")

Label(selection_window, text=logo, fg="#00F5FF", bg="#0F0F0F",
      font=("Courier New", 20, "bold"), justify="center").pack(pady=5)

Label(selection_window, text="Enter Your Name", font=("Segoe UI", 16, "bold"),
      bg="#0F0F0F", fg="white").pack(pady=(15, 4))

name_input = Entry(selection_window, font=("Segoe UI", 14), width=20)
name_input.pack(pady=5)

Label(selection_window, text="Select Quiz Category", font=("Segoe UI", 18, "bold"),
      bg="#0F0F0F", fg="white").pack(pady=(18, 6))

category_choice = StringVar()

style = ttk.Style()
style.configure("Custom.TRadiobutton",
                font=("Segoe UI", 14),
                background="#0F0F0F",
                foreground="white")

frame = Frame(selection_window, bg="#0F0F0F")
frame.pack()

for key, data in quiz_categories.items():
    ttk.Radiobutton(frame, text=data["name"].strip(), variable=category_choice,
                    value=key, style="Custom.TRadiobutton").pack(anchor="w", pady=4)

status_label = Label(selection_window, text="", bg="#0F0F0F", fg="yellow",
                     font=("Segoe UI", 12))
status_label.pack()

Button(selection_window, text=" Start Quiz ▶ ", font=("Segoe UI", 15, "bold"),
       bg="#00FF6A", fg="black", padx=12, pady=6, command=start_quiz)\
    .pack(pady=25)

selection_window.mainloop()
