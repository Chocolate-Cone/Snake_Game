from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
Play_game = True
while Play_game:
    screen.update()
    time.sleep(0.5)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        Play_game = False
        scoreboard.game_over()

    for seg in snake.all_snakes:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            Play_game = False
            scoreboard.game_over()
screen.exitonclick()
