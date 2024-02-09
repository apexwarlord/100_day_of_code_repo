import turtle
import turtle as t
import random

colors = ['r', 'o', 'y', 'g', 'b', 'i', 'v',]
colorstext = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet',]

turtles = [red, orange, yellow, green, blue, indigo, violet] = [t.Turtle() for _ in range(len(colors))]
ref = t.Turtle()

screen = t.Screen()
screen.setup(width=500, height=400)


def race():
    winner = []
    while len(winner) == 0:
        for racing_turtle in turtles:
            racing_turtle.forward(random.randint(2, 8) * 2)
        for racing_turtle in turtles:
            if racing_turtle.xcor() >= 215:
                winner.append(racing_turtle)
    return winner

user_bet = ''
while not user_bet or user_bet[0] not in colors:
    user_bet = screen.textinput('Bet on a turtle!', 'Which turtle would you like to bet on? Enter a color from ROYGBIV: ').lower()
user_bet = colors.index(user_bet[0])

ref.hideturtle()
ref.up()
ref.speed('fastest')
ref.setx(215)
ref.sety(170)
ref.down()

top_height = 125
for turtle in turtles:
    turtle.shape('turtle')
    turtle.color(colorstext[turtles.index(turtle)])
    turtle.penup()
    turtle.goto(-240, top_height)
    top_height -= 35

ref.right(90)
ref.forward(340)

winner_list = race()

if turtles[user_bet] in winner_list:
    print('You won!')
else:
    print('You lost!')


screen.exitonclick()