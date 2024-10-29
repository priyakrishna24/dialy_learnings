import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Turtle Event Listener")
t = turtle.Turtle()

# Define functions to move the turtle
def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

# Set up key bindings
screen.listen()  # Activate the screen to listen for events
screen.onkey(move_forward, "Up")    # Bind the Up arrow key to move_forward
screen.onkey(move_backward, "Down")  # Bind the Down arrow key to move_backward
screen.onkey(turn_left, "Left")      # Bind the Left arrow key to turn_left
screen.onkey(turn_right, "Right")    # Bind the Right arrow key to turn_right

# Keep the window open
screen.mainloop()
