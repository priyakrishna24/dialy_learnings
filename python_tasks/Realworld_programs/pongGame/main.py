from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Creating a screen
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

# paddle=Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(5,1)
# paddle.penup()
# paddle.goto(340,0)

# def go_up():
#     y_new=paddle.ycor()+20
#     paddle.goto(paddle.xcor(),y_new)
# def go_down():
#     y_new=paddle.ycor()-20
#     paddle.goto(paddle.xcor(),y_new)

screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
     
    #Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detect collision with paddle
    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.bounce_x()

    #Detect R Paddle Misses
    if ball.xcor()>380:
        scoreboard.increase_left_score()
        ball.reset_position()
    
    #Detect L Paddle Misses
    if ball.xcor()<-380:
        scoreboard.increase_right_score()
        ball.reset_position()

screen.exitonclick()