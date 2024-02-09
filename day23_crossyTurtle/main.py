import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

traffic = CarManager()
traffic.generate_fleet()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=player.go_up)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    traffic.launch_cars()
    traffic.drive_cars()
    screen.update()

    for car in traffic.active_fleet:
        if car.ycor()-22 < player.ycor() < car.ycor()+13 and player.distance(car) <= 23:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish():
        scoreboard.score += 1
        scoreboard.print_score()
        traffic.increase_speed()
        screen.update()
        time.sleep(3)
        player.go_to_start()


screen.update()

screen.exitonclick()