# import turtle
# my_turtle=turtle.Turtle()
# my_turtle.forward(10)
# my_turtle.left(90)
# my_turtle.forward(100)

# turtle.exitonclick()

from turtle import Turtle,Screen

timmy_turtle=Turtle()

timmy_turtle.shape("turtle")
timmy_turtle.color("green")

# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)


length=100
width=100

for i in range(2):
    
    timmy_turtle.forward(length)
    timmy_turtle.right(90)
    timmy_turtle.forward(width)
    timmy_turtle.right(90)




screen=Screen()
screen.exitonclick()