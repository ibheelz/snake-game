import time
from food import Food
from snake import Snake
from score import Score
from turtle import Screen

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake Game")
screen.setup(width = 600, height = 600)

game_is_on = True

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_update()

screen.exitonclick()