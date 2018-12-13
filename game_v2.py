import math
import turtle

window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.bgpic("images/background.png")
window.screensize(1200, 800)
# window.tracer(n=2)

BASE_X, BASE_Y = 0, -300


def calc_heading(x1, y1, x2, y2):
    dx = x2 - x1
    length = (dx ** 2 + (y2-y1) ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    return alpha


def fire_missile(x, y):
    missile = turtle.Turtle()
    missile.hideturtle()
    missile.speed(0)
    missile.color('white')
    missile.penup()
    missile.setpos(x=BASE_X, y=BASE_Y)
    missile.pendown()
    heading = calc_heading(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)
    missile.setheading(heading)
    missile.showturtle()
    # missile.forward(500)
    # missile.shape('circle')
    # missile.shapesize(2)
    # missile.shapesize(3)
    # missile.shapesize(4)
    # missile.shapesize(5)
    # missile.clear()
    # missile.hideturtle()
    our_missiles.append(missile)
    our_missiles_target.append([x, y])


window.onclick(fire_missile)

our_missiles = []
our_missiles_target = []

while True:
    window.update()

    for num, missile in enumerate(our_missiles):
        missile.forward(4)
        target = our_missiles_target[num]
        if missile.distance(x=target[0], y=target[1]) < 20:
            missile.shape('circle')
            missile.shapesize(2)
            missile.shapesize(3)
            missile.shapesize(4)
            missile.shapesize(5)