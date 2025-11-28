from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#27374D"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain, player_name, category_name):
        self.quiz = quiz_brain
        self.name = player_name
        self.category = category_name

        # ===== Window ===== #
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=25, pady=25, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(text=f"Score: 0", fg="white",
                                 bg=THEME_COLOR, font=("Segoe UI", 13, "bold"))
        self.score_label.grid(row=0, column=1)

        # Question canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280,
            text="Loading...", fill=THEME_COLOR, font=("Segoe UI", 16, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        # ---- TRUE / FALSE BUTTONS ---- #
        try:
            true_img = PhotoImage(file="true.png")
            false_img = PhotoImage(file="false.png")

            self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
            self.true_btn.image = true_img

            self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
            self.false_btn.image = false_img

        except:
            self.true_btn = Button(text="TRUE", width=12, bg="green",
                                   fg="white", font=("Segoe UI", 12, "bold"),
                                   command=self.true_pressed)
            self.false_btn = Button(text="FALSE", width=12, bg="red",
                                    fg="white", font=("Segoe UI", 12, "bold"),
                                    command=self.false_pressed)

        self.true_btn.grid(row=2, column=0, pady=10)
        self.false_btn.grid(row=2, column=1, pady=10)

        self.get_next_question()
        self.window.mainloop()

    # =========================
    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")

        else:
            final = f"🎉 Quiz Over 🎉\n\n{self.name}, you scored {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_text, text=final)

            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

            messagebox.showinfo(
                "Quiz Completed",
                f"{self.name}, your Score is {self.quiz.score}/{self.quiz.question_number}"
            )

    # =========================
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, correct):
        self.canvas.config(bg="lightgreen" if correct else "red")
        self.window.after(600, self.get_next_question)
