# from turtle import Turtle,Screen
# timmy_turtle=Turtle()

# timmy_turtle.shape("turtle")
# timmy_turtle.color("green")

# for i in range(2):
    
#     timmy_turtle.forward(100)
#     timmy_turtle.right(120)
#     timmy_turtle.forward(100)
#     timmy_turtle.right(120)

# for i in range(2):
    
#     timmy_turtle.forward(100)
#     timmy_turtle.right(90)
#     timmy_turtle.forward(100)
#     timmy_turtle.right(90)





# screen=Screen()
# screen.exitonclick()



from turtle import Turtle, Screen
import random
# Create a turtle object
timmy_turtle = Turtle()

timmy_turtle.shape("turtle")

#timmy_turtle.color("green")
colors=["green","red","blue","black","brown","purple"]
def color_change():
    timmy_turtle.color(random.choice(colors))


#timmy_turtle.speed(10)  
num_repetitions =3
while(num_repetitions<10):
    color_change()
    angle = 360 / num_repetitions  
    line_length = 100

    # Drawing the pattern
    for _ in range(num_repetitions):
        timmy_turtle.forward(line_length)  
        timmy_turtle.right(angle)   
    num_repetitions+=1       

screen = Screen()
screen.exitonclick()
