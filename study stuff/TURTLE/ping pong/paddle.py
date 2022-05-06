from turtle import Turtle

DOWN = 270
UP = 90
POSITION = [(300, 0), (300, 20), (300, 40)]


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.paddle_create(position)
    
    def paddle_create(self, position):
        self.penup()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setpos(position)

    def up(self):
        self.goto(self.xcor(),  self.ycor() + 20)
    
    def down(self):
        self.goto(self.xcor(),  self.ycor() - 20)
        
    
        