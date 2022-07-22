import turtle as t
import random
from matplotlib.pyplot import title


from scipy import rand

t.colormode(255)

direction = [0, 90, 180, 270]


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color


timy_the_turtle = t.Turtle()
timy_the_turtle.dot()
timy_the_turtle.speed(20)


# for i in range(360):
#     timy_the_turtle.color(random_color())
#     timy_the_turtle.forward(30)
#     timy_the_turtle.left(random.choice(direction))


timy_the_turtle.circle(100)

for i in range(360):
    timy_the_turtle.circle(100)
    timy_the_turtle.left(10)


screen = t.Screen()
screen.exitonclick()
