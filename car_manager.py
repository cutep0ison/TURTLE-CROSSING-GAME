from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.segment = []

    def genarate(self):
        random_number = random.randint(1, 6)
        if random_number == 6:
            new_segment = Turtle("square")
            new_segment.shapesize(stretch_wid=1, stretch_len=2)
            new_segment.color(random.choice(COLORS))
            new_segment.penup()
            new_segment.goto(x=230, y=random.randint(-200, 200))
            new_segment.setheading(180)
            self.segment.append(new_segment)

    def move(self):
        for turtle in self.segment:
            turtle.forward(MOVE_INCREMENT)







