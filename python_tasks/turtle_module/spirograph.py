import turtle as t
from turtle import Screen
import random


t.speed(20)
tilt_angle=5
size_of_gap=5
t.colormode(255)

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colour=(r,g,b)
    return random_colour

for _ in range(int(360/size_of_gap)):
    t.color(random_colour())
    t.circle(50)
    t.right(tilt_angle)


screen = Screen()
screen.exitonclick()