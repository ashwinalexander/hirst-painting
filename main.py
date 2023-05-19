# import turtle
import random
from turtle import Turtle, Screen
# import colorgram
# Extract  colors from a Hirst painting
# colors = colorgram.extract('image.jpg', 30)
# final_colors = []
# for color in colors:
#     final_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
# print(final_colors)

leo = Turtle()
screen = Screen()
screen.colormode(255)
hirst_colors = [(232, 254, 243), (253, 234, 245), (43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56), (216, 114, 171), (16, 127, 144), (85, 248, 252), (188, 39, 109), (23, 5, 107), (8, 209, 215), (99, 8, 50), (231, 163, 205), (204, 119, 35), (112, 6, 4)]

leo.hideturtle()
leo.penup()

for i in range(-200, 200, 40):
    for j in range (-200, 200, 40):
        leo.color(random.choice(hirst_colors))
        leo.setposition(j,i)
        leo.begin_fill()
        leo.pendown()
        leo.circle(10)
        leo.penup()
        leo.end_fill()






screen.exitonclick()



