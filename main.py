from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_stick = Paddle((350, 0))
l_stick = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_stick.go_up, "Up")
screen.onkey(r_stick.go_down, "Down")
screen.onkey(l_stick.go_up, "w")
screen.onkey(l_stick.go_down, "s")

game = True
l_player = 0
r_player = 0

while game:
    time.sleep(ball.increase_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_stick) < 50 and ball.xcor() > 320 or ball.distance(l_stick) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_pos()
    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_pos()

screen.exitonclick()
