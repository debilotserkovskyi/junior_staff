from turtle import Turtle
from random import randint


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('yellow')
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = randint(-200, 200)
        random_y = randint(-200, 200)
        self.goto(random_x, random_y)
        