import turtle as t


def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_left():
    timmy.left(15)

def turn_right():
    timmy.right(15)

def go_home():
    timmy.clear()
    timmy.up()
    timmy.home()
    timmy.down()



timmy = t.Turtle()
timmy.width(2)
screen = t.Screen()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(go_home, "space")


screen.exitonclick()