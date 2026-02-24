from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class TurtleCrosser(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -280:
            self.backward(MOVE_DISTANCE)

    def at_finish_line(self):
        return self.ycor() >= FINISH_LINE

    def reset_position(self):
        self.goto(STARTING_POSITION)