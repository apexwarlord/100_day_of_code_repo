from turtle import Turtle

STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]


class Snake(object):
    def __init__(self, direction=0):
        self.direction = direction
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_COORDINATES:
            self.snake_body.append(self.add_segment(position))

    def add_segment(self, xy_cor):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(xy_cor)
        return segment

    def extend_snake(self):
        self.snake_body.append(self.add_segment(self.snake_body[-1].position()))

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x, new_y = self.snake_body[segment - 1].xcor(), self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(20)
        self.direction = self.head.heading()

    def up(self):
        if self.direction != 270:
            self.head.setheading(90)

    def down(self):
        if self.direction != 90:
            self.head.setheading(270)

    def left(self):
        if self.direction != 0:
            self.head.setheading(180)

    def right(self):
        if self.direction != 180:
            self.head.setheading(0)

    def reset(self):
        for segment in self.snake_body[3:]:
            segment.goto(800, 800)
            self.snake_body.pop(self.snake_body.index(segment))
        for i in range(0, 3):
            self.snake_body[i].goto(STARTING_COORDINATES[i])
        self.head.setheading(0)


# screen = t.Screen()
# screen.setup(600, 600)
# screen.bgcolor('black')
#
# johnny = Snake()
# johnny.move(0)
# screen.exitonclick()
