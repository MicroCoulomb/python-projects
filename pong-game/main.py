from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

PLAYER1 = (350, 0)
PLAYER2 = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle(PLAYER1)
paddle2 = Paddle(PLAYER2)

screen.listen()
#player 1 controls
screen.onkey(fun=paddle1.move_up, key="Up")
screen.onkey(fun=paddle1.move_down, key="Down")

#player 2 controls
screen.onkey(fun=paddle2.move_up, key="w")
screen.onkey(fun=paddle2.move_down, key="s")

scoreboard = ScoreBoard()
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.p2_score()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.p1_score()

screen.exitonclick()