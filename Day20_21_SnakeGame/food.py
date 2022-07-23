import random
from turtle import Turtle

from scipy import rand
from wordcloud import random_color_func


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)
