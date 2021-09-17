import turtle as t
import random

tim = t.Turtle()
# object^   blueprint,Class, from module^
t.colormode(255)
# changed colormode

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# function returns random color
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_ = (r, g, b)
    return color_


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed(10)

for _ in range(100):
    tim.color(random_color())
    # tim.color(random.choice(colours))
    # color from the list

    tim.forward(30)
    tim.setheading(random.choice(directions))


