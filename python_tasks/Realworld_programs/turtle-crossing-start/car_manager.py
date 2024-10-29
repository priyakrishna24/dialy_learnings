from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 30


class CarManager(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.move_distance=STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance == 1:
            new_car=Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)  
            new_car.penup()
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.move_speed=0.9

            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.move_distance)
            if car.xcor()<-320:
                car.hideturtle()
                self.all_cars.remove(car)
    
    def increase_carspeed(self):
        self.move_speed+=MOVE_INCREMENT
    
# from turtle import Turtle
# import random 

# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10

# class CarManager:
#     def __init__(self):
#         self.all_cars = []
#         self.move_distance = STARTING_MOVE_DISTANCE
    
#     def create_car(self):
#         random_chance = random.randint(1, 6)  # Adjust range for car creation frequency
#         if random_chance == 1:
#             new_car = Turtle("square")
#             new_car.color(random.choice(COLORS))
#             new_car.shapesize(stretch_wid=1, stretch_len=2)  
#             new_car.penup()
#             random_y = random.randint(-250, 250)
#             new_car.goto(300, random_y)
#             self.all_cars.append(new_car)

#     def move_car(self):
#         cars_to_remove = []
#         for car in self.all_cars:
#             car.backward(self.move_distance)
#             if car.xcor() < -320:
#                 cars_to_remove.append(car)  # Mark for removal

#         # Remove cars that have gone off-screen
#         for car in cars_to_remove:
#             car.hideturtle()  # Hide the turtle
#             self.all_cars.remove(car)  # Remove from list
