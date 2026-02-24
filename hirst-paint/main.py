from turtle import Turtle, Screen, colormode

trese = Turtle()
trese.shape("classic")
trese.color("maroon")

# draw a line and turn
# for _ in range(4):
#     trese.forward(100)
#     trese.right(90)

# draw a dashed line
# for _ in range(15):
#     trese.forward(10)
#     trese.penup()
#     trese.forward(10)
#     trese.pendown()

#draw different polygons with different colors
from random import randint, choice
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        trese.forward(100)
        trese.right(angle)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

colormode(255)
# for sides in range(3,11):
#     trese.color(random_color())
#     draw_shape(sides)

# random walk
# directions = [0,90,180,270]
# trese.pensize(10)
trese.speed("fastest")
#
# for _ in range(250):
#     rand_color = random_color()
#     # trese.pencolor(rand_color)
#     trese.color(rand_color)
#     trese.forward(15)
#     trese.setheading(choice(directions))

# spirograph
n_circles = 100
angle = 360 / n_circles
for _ in range(n_circles):
    trese.color(random_color())
    trese.circle(100)
    curr_heading = trese.heading()
    trese.setheading(curr_heading + angle)









screen = Screen()
screen.exitonclick()