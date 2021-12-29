import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creating player
player = Player()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# Screen listen
screen.listen()
screen.onkey(player.move, "Up")
# Car manager
car_manager = CarManager()
# scoreboard:
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()

    # Detecting collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detecting Finish line
    if player.reach_finish_line():
        print("you go to next level ")
        player.reset()
        car_manager.increase_speed()
        scoreboard.level_up()

screen.exitonclick()