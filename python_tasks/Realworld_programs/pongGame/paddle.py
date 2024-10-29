from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor()<250:
            y_new=self.ycor()+20
            self.goto(self.xcor(),y_new)
    def go_down(self):
        if self.ycor()>-240:
            y_new=self.ycor()-20
            self.goto(self.xcor(),y_new)

