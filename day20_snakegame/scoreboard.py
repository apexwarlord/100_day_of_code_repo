from turtle import Turtle

ALLIGNMENT = 'left'
FONT = ('Ariel', 24, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(shape='turtle')
        self.penup()
        self.highscore = 0
        self.get_high_score()
        self.hideturtle()
        self.score = -1
        self.color("lime")
        self.update_score()

    def get_high_score(self):
        try:
            with open("data.txt", 'r') as highscore_data:
                try:
                    highscore = int(str(highscore_data.read()))
                except ValueError as err:
                    print(err)
                    highscore = 0
        except FileNotFoundError as err:
            print(err)
            highscore = 0
        self.highscore = highscore

    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(-135, 300)
        self.write(f'SCORE:  {self.score}      HIGHSCORE: {self.highscore}', move=True, align=ALLIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            file = open('data.txt', 'w')
            file.write(f'{self.score}')
            file.close()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER', align='center', font=('courier', 50, 'bold'))


def build_border():
    border = Turtle()
    border.hideturtle()
    border.goto(-290, -290)
    border.color('white')
    border.goto(-290, 290)
    border.goto(290, 290)
    border.goto(290, -290)
    border.goto(-290, -290)
