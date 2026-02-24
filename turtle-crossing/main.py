from turtle import Screen
import time
from turtle_cross import TurtleCrosser
from car_manager import CarManager
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

crosser = TurtleCrosser()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=crosser.move_up, key="Up")
screen.onkey(fun=crosser.move_down, key="Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.move_car()
    car_manager.create_car()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(crosser) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if crosser.at_finish_line():
        crosser.reset_position()
        car_manager.increase_speed()
        scoreboard.update_score()



screen.exitonclick()