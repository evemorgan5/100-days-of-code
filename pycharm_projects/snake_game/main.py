from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0, 100)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# Up is 90 N, down is 270 S, right is 0, left is 180
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # refresh screen every 0.1 sec
    snake.move()

#Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#Detect collision with wall - game over
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print(snake.head.xcor(), snake.head.xcor(), snake.head.ycor(), snake.head.ycor())
        game_is_on = False
        scoreboard.game_over()


#Detect collision with own tail - game over
    #         if head collides with any segment in the tail:
    #            trigger game over sequence
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()


