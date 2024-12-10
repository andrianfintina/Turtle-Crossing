from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
HIGHT = 1
WEIGHT = 2
START_X = 320


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.shapesize(HIGHT, WEIGHT)
        self.set_position(self)
    
    def car_move(self):
        self.forward(MOVE_INCREMENT)
    
    def set_position(self, car):
        car.setx(START_X)
        car.sety(random.randint(-280, 280))

    
    

