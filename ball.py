from turtle import Turtle
import random
import time
ANGLE = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x = 10
        self.y = 10
        self.increase_speed = 0.1

    def move(self):
        nx = self.xcor() + self.x
        ny = self.ycor() + self.y
        self.goto(nx, ny)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.increase_speed *= .9

    def reset_pos(self):
        self.goto(0, 0)
        self.increase_speed = .1
        self.bounce_x()
        time.sleep(.5)
