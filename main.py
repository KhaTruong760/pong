from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
score = Score()

ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")



screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_on = True
while game_on :
    score.update()
    time.sleep(ball.move_speed)
    screen.update()
    ball.direction()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380 :
        ball.reset()
        score.l_point()
    if ball.xcor() < -380 :
        ball.reset()
        score.r_point()





screen.exitonclick()