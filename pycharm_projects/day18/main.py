# from turtle import Turtle, Screen
# # module^        class^  Screen class
# # import turtle module and get hold of the turtle class (Turtle)
# timmy_the_turtle = Turtle()
# ^ new turtle object    ^ from Turtle class
# # when from turtle: import Turtle, tim = Turtle()

# else if import module have to call class Turtle
#: import turtle, timmy_the_turtle = turtle.Turtle()



# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("orange")
#
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#
#






#
#
#
# screen = Screen()
# screen.exitonclick()



# from turtle import *
#  ^ import everything in file from module
# try and avoid using

import turtle as t
# give it an alias name
tim = t.Turtle()

for _ in range(15):
    tim.forward (10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



