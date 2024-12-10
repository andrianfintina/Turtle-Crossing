import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

plaier = Player()
car = CarManager()

screen.listen()
screen.onkeypress(plaier.move_forward, 'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    plaier.at_the_edge()
    car.car_move()
    screen.update()

