from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.Level=1
        self.update_Level()
    
    def update_Level(self):
        self.clear()
        self.goto(-230,270)
        self.write(f"Level : {self.Level}",align="center",font=FONT)
    
    def increase_level(self):
        self.Level+=1
        self.update_Level()

    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.write(f"GAME OVER",align="center",font=FONT)
