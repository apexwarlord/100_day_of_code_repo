# import colorgram
#
# colors = colorgram.extract('hirst_painting.png', 40)
# colorlist = []
# for color in colors:
#     colorlist.append((color.rgb.r, color.rgb.g, color.rgb.b))

import turtle as t
import random

background = (241, 236, 244)
colors =[(2, 13, 30), (47, 26, 18), (216, 128, 110), (21, 103, 156), (241, 210, 81), (163, 67, 47), (213, 87, 69), (155, 11, 29), (163, 160, 50), (96, 6, 18), (156, 63, 100), (204, 75, 105), (14, 61, 32), (34, 136, 72), (174, 135, 160), (18, 87, 51), (31, 170, 213), (7, 62, 141), (91, 203, 177), (147, 226, 215), (36, 207, 199), (112, 167, 190), (112, 48, 39), (219, 179, 214), (106, 218, 228), (82, 135, 176), (34, 84, 89), (222, 177, 169), (183, 191, 203), (67, 67, 53)]

timmy = t.Turtle()
timmy.speed("fastest")
screen = t.Screen()
screen.screensize(250, 700)

t.colormode(255)

timmy.pu()
timmy.width(25)
timmy.color('black')
screen.bgcolor(background)
timmy.hideturtle()

lmarg = [-225, -475]
while lmarg[1] < 500:
    timmy.goto(lmarg[0], lmarg[1])
    while timmy.pos()[0] < 250:
        randcolor = random.choice(colors)
        randomint = random.randint(0, 3)*5-1
        softcolor = (randcolor[0]+randomint, randcolor[1]+randomint, randcolor[2]+randomint)
        timmy.color(softcolor)
        timmy.down()
        timmy.forward(0.25)
        timmy.up()
        timmy.forward(49.75)
    lmarg[1] += 50









screen.exitonclick()
