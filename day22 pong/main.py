from time import sleep
from turtle import Screen
from turtle import Turtle

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

'''create and initialize screen'''
screen = Screen()
screen.setup(width=840, height=600)
screen.title("Pong Game")
screen.bgcolor('black')
screen.tracer(0)

''' create objects'''
ball = Ball()
l_score = Scoreboard((-90, 215))
r_score = Scoreboard((90, 215))
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
l_score.update_score('left', 0)
r_score.update_score('right', 0)

'''set game key listening'''
screen.listen()
screen.onkeypress(key='w', fun=l_paddle.up)
screen.onkeypress(key='s', fun=l_paddle.down)
screen.onkeypress(key='Up', fun=r_paddle.up)
screen.onkeypress(key='Down', fun=r_paddle.down)

screen.update()
sleep(1)
game_is_on = True

while game_is_on:
    ball.match_init()
    screen.update()
    sleep(1)
    while -370 <= ball.xcor() <= 370:
        ball.move(r_paddle, l_paddle)
        screen.update()
        sleep(0.03)
    if ball.ycor() > 0:
        r_score.update_score('right')
        if ball.serve == -1:
            ball.change_serve()
    else:
        l_score.update_score('left')
        if ball.serve == 1:
            ball.change_serve()
    l_paddle.goto(-350, 0)
    r_paddle.goto(350, 0)
    screen.update()
    sleep(1.5)

screen.exitonclick()