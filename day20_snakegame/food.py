import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('hot pink')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-13, 14)*20-10, random.randint(-13, 14)*20-10)