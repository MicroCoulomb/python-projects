from turtle import Turtle, Screen

trese = Turtle()
screen = Screen()

def move_forwards():
    trese.forward(10)

screen.listen()
screen.onkey(fun=move_forwards, key="space")
screen.exitonclick()