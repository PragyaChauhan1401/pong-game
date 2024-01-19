from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
score = Scoreboard()
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
s = 6
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 60 and ball.xcor() > 340 or ball.distance(l_paddle) < 60 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()
