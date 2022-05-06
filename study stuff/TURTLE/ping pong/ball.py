from turtle import Turtle
from random import randint
ANGLE = 0


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize()
        self.shape('circle')
        self.color('white')
        self.speed_move = 0.1
        # self.setpos(0, 0)
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_wall(self):
        self.y_move *= -1
        
    def bounce_paddle(self):
        self.x_move *= -1
        self.speed_move *= 0.9
        
    def restart(self):
        self.home()
        # self.y_move *= -1
        self.x_move *= - 1
        self.speed_move = 0.1
        