from turtle import Turtle

STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10.0
FINISH_LINE_Y = 230


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-230)
        self.setheading(90)

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor()+MOVE_DISTANCE)

    def move_right(self):
        self.goto(x=self.xcor() + MOVE_DISTANCE, y=self.ycor())

    def move_left(self):
        self.goto(x=self.xcor() - MOVE_DISTANCE, y=self.ycor())

    def refresh(self):
        self.goto(x=0, y=-230)


