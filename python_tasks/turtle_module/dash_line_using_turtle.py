from turtle import Turtle,Screen 
my_turtle=Turtle()

my_turtle.shape("turtle")
for _ in range(10):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
    


screen=Screen()
screen.exitonclick()