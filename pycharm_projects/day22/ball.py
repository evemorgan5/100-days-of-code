from turtle import Turtle

# Create ball and make it move constantly across the screen

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        # square is historically accurate
        self.penup()
        self.goto(0, 0)
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # if hits paddle make it bounce
    def bounce_x(self):
        self.x_move *= -1

    # if hits the wall make it bounce
    def bounce_y(self):
        self.y_move *= -1

    def return_centre(self):
        self.goto(0, 0)
        self.bounce_x()
