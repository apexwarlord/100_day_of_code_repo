from turtle import Screen
import time

from scoreboard import Scoreboard, build_border
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=640, height=665)
screen.bgcolor("black")

screen.title("SNAKE GAME")
screen.tracer(0)
build_border()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.07)

    snake.move()

    if snake.head.distance(food) <= 15:
        print('Nom nom nom...')
        food.refresh()
        scoreboard.update_score()
        snake.extend_snake()
        snake.extend_snake()

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 19:
            # game_is_on = False
            # time.sleep(2)
            scoreboard.reset_score()
            scoreboard.score = -1
            scoreboard.update_score()
            snake.reset()

    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        # game_is_on = False
        # time.sleep(3)
        scoreboard.reset_score()
        scoreboard.score = -1
        scoreboard.update_score()
        snake.reset()

# scoreboard.game_over()

screen.exitonclick()

# # create a snake body
# snake = []
# for i in range(0,3):
#     new_body = t.Turtle(shape='square')
#     new_body.color('white')
#     new_body.penup()
#     new_body.setx(-20*i)
#     snake.append(new_body)

# for segment in range(len(snake) - 1, 0, -1):
#     new_x, new_y = snake[segment-1].xcor(), snake[segment-1].ycor()
#     snake[segment].goto(new_x, new_y)
# snake[0].forward(20)
