# snake game

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import score_board
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)


snake = Snake()
food = Food()
score_board = score_board()

writer = Turtle()
writer.penup()
writer.hideturtle()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # collision with food
    if snake.head.distance(food) < 35:
        food.give_food()
        snake.extend_tail()
        score_board.increase_score()

    # collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score_board.write_game_over()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            score_board.write_game_over()


screen.exitonclick()
