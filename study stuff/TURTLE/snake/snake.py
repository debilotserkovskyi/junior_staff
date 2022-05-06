from turtle import Turtle
MOVING = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.head.color('blue')
    
    def create_snake(self):
        for position in range(0, 3):
            self.add_segment(position)
    
    def add_segment(self, position):
        shift = 0
        lil_tim = Turtle(shape="square")
        lil_tim.color("yellow")
        lil_tim.penup()
        lil_tim.setpos(0 - shift, 0)
        shift += 20
        self.body.append(lil_tim)
    
    def extend(self):
        self.add_segment(self.body[-1].position())
    
    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg - 1].xcor()
            new_y = self.body[seg - 1].ycor()
            self.body[seg].goto(new_x, new_y)
        self.head.forward(MOVING)
    
    def up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != UP:
            return self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != LEFT:
            return self.head.setheading(0)
    