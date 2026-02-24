from turtle import Screen, Turtle

pen = Turtle()
screen = Screen()
pen.speed("fastest")

def move_forwards():
    pen.forward(10)

def move_backwards():
    pen.backward(10)

def turn_cw():
    pen.right(10)

def turn_ccw():
    pen.left(10)

def clear_screen():
    pen.home()
    pen.clear()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_cw, key="d")
screen.onkey(fun=turn_ccw, key="a")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()