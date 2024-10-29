from turtle import Turtle, Screen

# Create a turtle object
timmy_turtle = Turtle()

# Set the length of each dash
dash_length = 10

# Draw a dashed line
for _ in range(15):  # Number of dashes in the line
    timmy_turtle.forward(dash_length)  # Draw the dash
    timmy_turtle.penup()  # Lift the pen to not draw the gap
    timmy_turtle.forward(dash_length)  # Move forward to create the gap
    timmy_turtle.pendown()  # Put the pen down to start drawing the next dash

# Keep the turtle window open until clicked
screen = Screen()
screen.exitonclick()
