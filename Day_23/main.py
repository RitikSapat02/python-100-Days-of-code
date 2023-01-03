from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)              #turned off the tracer

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while(game_is_on):             #whatever code in while loop will be run after every 0.1 sec
    time.sleep(0.1)           # update screen every 0.1 seconds
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.score_increment()

   

screen.exitonclick()

