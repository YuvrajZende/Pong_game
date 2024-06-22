from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.y_axis = 10
        self.x_axis = 10
        self.velocity = 0.1

    def move(self):
        x_axis = self.xcor() + self.x_axis
        y_axis = self.ycor() + self.y_axis
        self.goto(x_axis, y_axis)

    def bounce_y(self):
        self.y_axis *= -1

    def bounce_x(self):
        self.x_axis *= -1
        self.velocity *= 0.9

    def bounce_back(self):
        self.goto(0, 0)
        self.x_axis *= -1
        self.velocity = .1

