import turtle
import random
import math

window = turtle.Screen()
window.setup(1300, 900)
window.bgpic("images/background.png")
window.screensize(1200,800)

BASE_X, BASE_Y = 0, -350

def calc_heading(x1, y1, x2, y2):
    dx = x2 - x1
    length = (dx ** 2 + (y2-y1) ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    return alpha

def fire_missile(x, y):
    missile = turtle.Turtle()
    missile.color("white")
    missile.penup()
    missile.setpos(x = BASE_X, y= BASE_Y)
    heading = calc_heading(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)
    missile.pendown()
    missile.setheading(heading)
    missile.forward(500)
    missile.shape("circle")
    missile.shapesize(1)
    missile.shapesize(4)
    missile.shapesize(6)
    missile.shapesize(8)
    missile.shapesize(10)
    missile.clear()
    missile.hideturtle()

window.onclick(fire_missile)

window.mainloop()