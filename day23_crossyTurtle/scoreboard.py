from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Courier', 50, 'bold'))