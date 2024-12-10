from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POSITION)
        self.shape('turtle')
    
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def at_the_edge(self):
        if self.ycor() == FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)

