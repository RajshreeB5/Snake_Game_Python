from turtle import Turtle,Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()



    snake.move()










screen.exitonclick()