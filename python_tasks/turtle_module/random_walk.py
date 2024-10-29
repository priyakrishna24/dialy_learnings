import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colour=(r,g,b)
    return random_colour

angle=[90,180]

tim.pensize(10)
tim.speed(10)
for _ in range(100):
    tim.color(random_colour())
    tim.forward(30)
    tim.right(random.choice(angle))


screen = Screen()
screen.exitonclick()