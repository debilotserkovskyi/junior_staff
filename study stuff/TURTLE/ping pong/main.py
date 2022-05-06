import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
# TODO 1 create a screen -- done

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

# TODO 2 create and move a paddle -- done
# TODO 3 create another paddle -- done
# TODO 4 create a ball and make in move -- done

my_paddle = Paddle((350, 0))
another_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
score.line()

screen.listen()
screen.onkeypress(my_paddle.up, 'Up')
screen.onkeypress(my_paddle.down, 'Down')
screen.onkey(another_paddle.up, 'a')
screen.onkey(another_paddle.down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.speed_move)
    # TODO 5 detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # TODO 6 Detect collision with paddle
    if ball.xcor() > 330 and ball.distance(my_paddle) < 50 or \
            ball.xcor() < -330 and ball.distance(another_paddle) < 50:
        ball.bounce_paddle()
    
    # TODO 7 detect when paddle misses
    if ball.xcor() > 400:
        ball.restart()
        score.increase_right()
    
    if ball.xcor() < -400:
        ball.restart()
        score.increase_left()
    
    # TODO 8 keep score
    if score.score_r == 5 or score.score_r == 5:
        game_is_on = False

screen.exitonclick()
