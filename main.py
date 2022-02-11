import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from pygame import mixer

WINNING_SCORE = 5
screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.onkey(player.move_up, "w")
screen.onkey(player.move_right, "d")
screen.onkey(player.move_left, "a")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(score.move_speed)
    screen.update()

    car.genarate()
    car.move()

    for seg in car.segment:
        if seg.distance(player) < 20:
            mixer.init()
            mixer.music.load("57B2HU8-game-failed-05.mp3")
            mixer.music.play()
            game_is_on = False
            score.gameover()

    if player.ycor() >= 230:
        mixer.init()
        mixer.music.load("achievement unlock.mp3")
        mixer.music.play()
        score.level()
        player.refresh()

    if score.score == WINNING_SCORE:
        mixer.init()
        mixer.music.load("TB7L64W-winning.mp3")
        mixer.music.play()
        game_is_on = False
        score.win()

screen.exitonclick()
