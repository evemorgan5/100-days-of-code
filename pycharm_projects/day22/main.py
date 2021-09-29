from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

#Create and move a paddle - using the same class to create each one
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # refresh screen every 0.1 sec, now moves at more reasonable rate
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        # width of ball is 20
        ball.bounce_y()

    #Detect collision with paddle
    # past paddle and distance within paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()
        scoreboard.r_point()

    if (ball.distance(l_paddle) < 50 and ball.xcor() > -320):
        # print("made contact with paddle")
        ball.bounce_x()
        scoreboard.l_point()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.return_centre()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.return_centre()
        scoreboard.r_point()

screen.exitonclick()
