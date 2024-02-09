from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.score = 0

        self.question = "sample question text"
        self.answer = None

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.score}", font=('courier', 12, 'bold',), bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0, borderwidth=0)
        self.question_text = self.canvas.create_text(150, 125, text=f"{self.question}", fill=THEME_COLOR,
                                                     font=('arial', 20, 'bold italic'), width=285)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        trueimg = PhotoImage(file="images/true.png")
        falseimg = PhotoImage(file="images/false.png")
        self.trueb = Button(image=trueimg, highlightthickness=0, borderwidth=0, command=self.answer_true)
        self.falseb = Button(image=falseimg, highlightthickness=0, borderwidth=0, command=self.answer_false)
        self.trueb.grid(row=2, column=0)
        self.falseb.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if not self.quiz.still_has_questions():
            self.trueb["state"] = DISABLED
            self.falseb["state"] = DISABLED
            self.canvas.itemconfig(self.question_text, text=f"You've finish the quiz with a final score of...\n\n    ~~ {self.score} / 10 ~~")
        else:
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
            self.trueb["state"] = NORMAL
            self.falseb["state"] = NORMAL

    def answer_false(self):
        self.check_answer(False)

    def answer_true(self):
        self.check_answer(True)

    def check_answer(self, asr: bool):
        self.trueb["state"] = DISABLED
        self.falseb["state"] = DISABLED
        if asr == self.quiz.check_answer():
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)