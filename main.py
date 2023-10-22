import turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

def quit():
    with open("highscore.txt") as file:
        prev_high_score = int(file.read())

    if (score.high_score > prev_high_score):
        with open ("highscore.txt", "w") as file:
            file.write(str(score.high_score))
    
    turtle.bye()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(quit, "q")

while True:
    snake.move()
    screen.update()
    time.sleep(0.2)

    # Check if snake touched food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.reposition() 
        score.increase_score()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 
        or snake.head.ycor() > 280 or snake.head.ycor() < -380):
        score.reset()
        snake.reset()
        

    # check if touches tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()




screen.exitonclick()