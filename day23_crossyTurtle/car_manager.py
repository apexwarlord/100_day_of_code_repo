from turtle import Turtle
import random

COLORS = ["red", "orange", "sky blue", "green", "blue", "purple", "hot pink", "lime", "brown", "black"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2.5
LAUNCH_FACTOR = 7

class CarManager:
    def __init__(self):
        self.car_fleet = []
        self.active_fleet = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.launch_factor = LAUNCH_FACTOR

    def create_car(self):
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=0.8, stretch_len=2)
        new_car.setheading(180)
        return new_car

    def generate_fleet(self):
        for i in range(0, 26):
            for _ in range(3):
                car = self.create_car()
                car.goto(310, -240+i*20)
                self.car_fleet.append(car)

    def launch_cars(self):
        if self.launch_factor >= random.randint(1, 40):
            self.active_fleet.append(self.car_fleet.pop(random.randint(0, len(self.car_fleet)-1)))

    def drive_cars(self):
        for car in self.active_fleet:
            if car.xcor() < -310:
                car.setx(310)
                self.car_fleet.append(self.active_fleet.pop(self.active_fleet.index(car)))

            else:
                car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        self.launch_factor += 1
