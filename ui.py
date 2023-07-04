import tkinter as tk
from quiz_brain import QuizBrain

BG_COLOR = "#3B7097"
CARD_COLOR = "#75BDE0"
TEXT_COLOR = "#F6E2BC"


class UI:

    def __init__(self, quizBrain: QuizBrain):  # imports QuizBrain class to use its functions
        self.window = tk.Tk()
        self.quiz = quizBrain
        self.window.title("True or False Quiz!")
        self.window.config(bg=BG_COLOR, height=600, width=350, padx=20, pady=20)

        self.card = tk.Canvas(width=300, height=250, highlightthickness=0, bg=CARD_COLOR)
        self.question = self.card.create_text(150, 125, text="", font=("Arial", 20, "italic"), fill="white", width=250)
        self.card.grid(columnspan=2, column=0, row=1, pady=40)

        self.score = tk.Label(text="Score: 0")
        self.score.grid(row=0, column=1)
        self.score.config(bg=BG_COLOR, fg="white")

        true_image = tk.PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=true_image, command=self.check_true)
        self.true_button.grid(row=2, column=0)
        self.true_button.config(height=97, width=100, highlightthickness=0, highlightcolor=BG_COLOR, padx=10, pady=10)

        false_image = tk.PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=false_image, command=self.check_false)
        self.false_button.grid(row=2, column=1)
        self.false_button.config(height=97, width=100, highlightthickness=0, highlightcolor=BG_COLOR, padx=10, pady=10)
        self.get_q()

        self.window.mainloop()

    def get_q(self):
        self.card.config(bg=CARD_COLOR)
        if self.quiz.q_number <= 9:
            question_text = self.quiz.next_q()
            self.card.itemconfig(self.question, text=question_text)
        else:
            self.card.itemconfig(self.question, text=f"Quiz is over! Your score is {self.quiz.score}.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def check_true(self):
        correct = self.quiz.check(user_answer="True", cor_answer=self.quiz.next_q_answer())
        if correct:
            self.score.config(text=f"Score: {self.quiz.score}")
        self.color_feedback(correct)

    def check_false(self):
        correct = self.quiz.check(user_answer="False", cor_answer=self.quiz.next_q_answer())
        if correct:
            self.score.config(text=f"Score: {self.quiz.score}")
        self.color_feedback(correct)

    def color_feedback(self, correct: bool):
        if correct:
            self.card.config(bg="green")
        else:
            self.card.config(bg="red")
        self.window.after(1000, self.get_q)
