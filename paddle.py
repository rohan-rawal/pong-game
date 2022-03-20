from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.pos = position
        self.shape("square")
        self.create_paddle()

    def create_paddle(self):
        self.color("white")
        self.penup()
        self.goto(self.pos)
        self.resizemode("user")
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    
