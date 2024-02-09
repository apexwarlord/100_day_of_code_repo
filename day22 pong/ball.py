from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, serve=1):
        super().__init__('circle')
        self.serve = serve
        self.xvelocity = 10 * self.serve
        self.yvelocity = 0
        self.width(7)
        self.draw_court()
        self.reset()

    def draw_court(self):
        self.goto(0, -306.5)
        self.color('white')
        self.setheading(90)
        for _ in range(25):
            self.forward(10.5)
            self.up()
            self.forward(17)
            self.down()
        self.up()

    def reset(self):
        self.goto(0, 0)

    def change_serve(self):
        if self.serve == 1:
            self.serve = -1
        else:
            self.serve = 1

    def match_init(self):
        self.xvelocity = 7 * self.serve
        self.yvelocity = random.choice([-12, -9, 9, 12])
        self.goto(0, random.randint(-150, 150))

    def move(self, right_paddle, left_paddle):
        self.goto(self.xcor() + self.xvelocity, self.ycor() + self.yvelocity)
        if abs(self.ycor()) > 280:
            self.yvelocity = -self.yvelocity
        if 338 > self.xcor() > 333 and self.distance(right_paddle) < 52:
            self.xvelocity = -self.xvelocity
        if -338 < self.xcor() < -333 and self.distance(left_paddle) < 52:
            self.xvelocity = -self.xvelocity
