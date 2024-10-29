import turtle
screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer_state=screen.textinput(title="Guess the state",prompt="What's the another state name")
print(answer_state)

# import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.title("U.S States Game")
# image = "blank_states_img.gif"

# # Add the image as a shape
# screen.addshape(image)
# turtle.shape(image)

# # Get user input
# answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?")

# # Print user input for verification
# if answer_state:
#     print(answer_state)
# else:
#     print("No input provided.")
