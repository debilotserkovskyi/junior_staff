from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_l, self.score_r = 0, 0
        self.color('orange')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.line()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"{self.score_l}       {self.score_r}",
                   font=('Arial', 40, 'normal'),
                   align='center')
        
    def increase_left(self):
        self.score_l += 1
        self.update_score()
        
    def increase_right(self):
        self.score_r += 1
        self.update_score()
        
    def line(self):
        dash = Turtle()
        dash.color('white')
        dash.goto(0, -25)
        dash.circle(50)
        dash.goto(0, 300)
        dash.goto(0, -300)
            