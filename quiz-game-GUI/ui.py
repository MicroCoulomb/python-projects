from tkinter import *
from quiz_brain import QuizBrain

BG_COLOR = "#9E3B3B"
Q_BG = "#FFEAD3"
Q_FONT = ("Arial", 12, "italic")

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=BG_COLOR)

        self.quiz = quiz

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="#FFEAD3", bg=BG_COLOR, font=("Courier", 10))
        self.score_label.grid(row=0, column=1, sticky='e')

        self.canvas = Canvas(width=300, height=250, bg=Q_BG)
        self.qtext = self.canvas.create_text(150, 125, width=260,
                                             text="Sample Question", fill=BG_COLOR, font=Q_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.cross_image = PhotoImage(file="cross.png")
        self.cross_button = Button(image=self.cross_image, bg=BG_COLOR, highlightthickness=0, relief="flat", command=self.false_press)
        self.cross_button.grid(row=2, column=0)

        self.check_image = PhotoImage(file="check.png")
        self.check_button = Button(image=self.check_image, bg=BG_COLOR, highlightthickness=0, relief="flat", command=self.true_press)
        self.check_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=Q_BG)
        if self.quiz.still_has_question():
            question_data = self.quiz.next_question()
            # self.answer = question_data["Answer"]
            self.canvas.itemconfig(self.qtext, text=question_data)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.qtext, text=f"Quiz Done.\nYour final score is {self.quiz.score}/10", font=("Courier", 14, "bold"), justify="center")
            self.cross_button.config(state="disabled")
            self.check_button.config(state="disabled")


    def true_press(self):
        self.give_feedback(self.quiz.check_answer(u_answer="True"))

    def false_press(self):
        self.give_feedback(self.quiz.check_answer(u_answer="False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)