from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup() # So it does not draw
        self.shapesize(0.5, 0.5) # Make the circle smaller
        self.color("red") # Set colour to red
        self.speed(0) # Set speed to fastest 
        self.reposition()

    def reposition(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)   # Go to random position