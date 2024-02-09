import turtle as t
import random

directions = [0, 90, 180, 270, ]


def direction():
    return random.choice(directions)


def get_color():
    return tuple(random.randint(0, 255) for _ in range(3))


timmy = t.Turtle()
timmy.shape("turtle")
t.colormode(255)
screen = t.Screen()

# timmy.pu()
# timmy.setx(-50)
# timmy.sety(200)
# timmy.pd()

# sides = 12

# for _ in range(10):
#     timmy.color(colors.pop(colors.index(random.choice(colors))))
#     timmy.begin_fill()
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(360/sides)
#     timmy.end_fill()
#     sides -= 1

timmy.width(2)
timmy.speed('fastest')

turn = 4

for _ in range(int(360/turn)):
    timmy.color(get_color())
    # timmy.seth(direction())
    timmy.circle(120)
    timmy.left(4)
    # timmy.forward(20)

screen.exitonclick()
