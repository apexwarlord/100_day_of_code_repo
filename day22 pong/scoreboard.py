from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(position)

    def update_score(self, alignment, score=1):
        self.clear()
        self.score += score
        self.write(f"{self.score}", align=alignment, font=("Courier", 84, "bold"))
