import time
from turtle import Screen
from snake import Snake

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()


screen.listen()
screen.onkey(snake.up, "Up")  # up - это метод класса "Snace" (def up(self):), "Up" - это активная клавиша
screen.onkey(snake.down, "Down")  # down - это метод класса "Snace" /-/, "Down" - это активная клавиша
screen.onkey(snake.left, "Left") # left - это метод класса "Snace" /-/, "Left" - это активная клавиша
screen.onkey(snake.right, "Right") # right - это метод класса "Snace" /-/, "Right" - это активная клавиша


game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)

	snake.move()

screen.exitonclick()


