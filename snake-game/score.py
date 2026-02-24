from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
with open("data.txt", mode="r") as file:
    HIGH_SCORE = int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.highscore = HIGH_SCORE
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score} High Score : {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset (self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = -1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)