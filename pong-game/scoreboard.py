from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.update_score()

    def p1_score(self):
        self.player1_score += 1
        self.update_score()

    def p2_score(self):
        self.player2_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 260)
        self.write(f"{self.player1_score}", align=ALIGN, font=FONT)
        self.goto(-100, 260)
        self.write(f"{self.player2_score}", align=ALIGN, font=FONT)