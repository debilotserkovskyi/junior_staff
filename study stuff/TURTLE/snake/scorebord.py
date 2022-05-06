from turtle import Turtle
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('orange')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write(arg=f'Score: {self.score}', align='center', font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'GAME OVER', align='center', font=FONT)

    
    # def undate(self)
    #     :
        
        
        