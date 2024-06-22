from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong_game")
screen.tracer(0)

left_paddle = Paddle((-360, 0))
right_paddle = Paddle((360, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.velocity)
    ball.move()

    # detecting the collision with the top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting paddle with the ball 
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 330 or
            ball.distance(left_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
# bounce backing of ball after the detection and updating the scorecard  
    if ball.xcor() > 380:
        ball.bounce_back()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.bounce_back()
        scoreboard.right_point()


screen.exitonclick()
