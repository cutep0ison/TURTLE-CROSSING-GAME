from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.score = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-180, 220)
        self.write(f"Level= {self.score}", False, "center", font=('Courier', 20, 'normal'))

    def level(self):
        self.move_speed *= 0.5
        self.clear()
        self.score += 1
        self.write(f"Level= {self.score}", False, "center", font=('Courier', 20, 'normal'))

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=('Courier', 30, 'bold'))

    def win(self):
        self.goto(0, 0)
        self.write("Winner", False, "center", font=('Courier', 30, 'bold'))
