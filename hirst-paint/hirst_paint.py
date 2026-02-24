# import colorgram
#
# colors = colorgram.extract('sample.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

my_colors = [(233, 166, 61), (46, 112, 157), (113, 151, 202), (12, 15, 43), (17, 128, 96), (215, 122, 162),
             (170, 44, 88), (153, 18, 53), (224, 200, 114), (1, 176, 141), (155, 165, 38), (223, 77, 105),
             (227, 86, 43), (41, 165, 208), (119, 172, 115), (214, 64, 33), (120, 104, 159), (62, 14, 34), (43, 53, 96),
             (18, 94, 70), (227, 169, 188), (15, 54, 43), (14, 84, 101), (50, 13, 6), (130, 30, 22), (161, 208, 196)]

import turtle as t
import random
trese = t.Turtle()
trese.hideturtle()
screen = t.Screen()
screen.setup(width=600, height=600)
t.colormode(255)

trese.penup()
trese.speed("fastest")

def run_horizontal(ypos):
    trese.setpos(-225, ypos)
    for _ in range(10):
        one_color = random.choice(my_colors)
        trese.dot(20, one_color)
        trese.forward(50)

y_pos = -225
for _ in range(10):
    run_horizontal(y_pos)
    y_pos += 50



screen.exitonclick()