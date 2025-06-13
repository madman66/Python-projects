import turtle
from turtle import Turtle,Screen
from random import choice

from sympy import false

timmy = Turtle()
screen = Screen()
color_list = [(245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
y = 0

turtle.colormode(255)
timmy.shape("turtle")

timmy.penup() # Lift the pen to avoid drawing while moving
timmy.goto(0 , 0) # Move to the bottom center
timmy.pendown() # Put the pen down to start drawing

for i in range(10):

    for j in range(10):
        color_1 = choice(color_list)
        timmy.fillcolor(color_1)
        timmy.begin_fill()
        timmy.circle(20)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

    y+=50
    timmy.penup()
    timmy.goto(0, y)
    timmy.pendown()

timmy.hideturtle()
screen.exitonclick()

