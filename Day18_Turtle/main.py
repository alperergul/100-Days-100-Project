import turtle as t
import random
from matplotlib.pyplot import title


# *************************************************
# ************LECTURE NOTES************************
# *************************************************
# from scipy import rand

# t.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color


# timy_the_turtle = t.Turtle()
# timy_the_turtle.dot()
# timy_the_turtle.speed('fastest')


# def draw_spirograph(size_of_gap):

#     for i in range(int(360 / size_of_gap)):
#         timy_the_turtle.color(random_color())
#         timy_the_turtle.circle(100)
#         timy_the_turtle.setheading(timy_the_turtle.heading() + size_of_gap)


# draw_spirograph(4)


# screen = t.Screen()
# screen.exitonclick()

# *************************************************
# ************CREATE COLORS************************
# *************************************************
# import colorgram

# rgb_colors = []

# # Extract 6 colors from an image.
# colors = colorgram.extract('data.jpg', 30)

# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb_colors.append((r, g, b))

color_list = [(26, 108, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (226, 237, 229), (223, 137, 176), (143, 108, 57), (102, 197, 219), (205, 166, 30), (21, 57, 132), (214, 74, 91), (238, 89, 49),
              (119, 192, 140), (142, 208, 227), (4, 185, 176), (106, 108, 198), (138, 29, 72), (5, 161, 86), (98, 51, 36), (23, 156, 209), (229, 167, 185), (173, 185, 222), (29, 90, 95), (233, 172, 162), (155, 212, 190), (88, 46, 33), (244, 207, 5)]


# *************************************************
# ************CREATE TURTLE PROJECT****************
# *************************************************

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
