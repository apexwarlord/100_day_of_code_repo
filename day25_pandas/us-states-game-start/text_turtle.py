from turtle import Turtle


class TextTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.speed('fastest')

    def write_text(self, text, xcor, ycor):
        self.goto(xcor, ycor)
        self.write(text, align="center", font=("arial", 12, "bold"))
