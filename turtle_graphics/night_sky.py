# night_sky.py
# By Aspen
# Draws a random night sky full of stars

from turtle import *
import random
import shapes

def draw_sky():
    bgcolor('#001220')
    pretty_colors = ['#efe9f4', '#fff', '#e05cb2', '#5fbff9', '#1cefff', '#bd5ce0', '#9368ff' ]

    for i in range(40):
        penup()
        x = random.randint(-250, 250)
        setx(x)
        y = random.randint(-250, 250)
        sety(y)
        pendown()
        star_color = pretty_colors[random.randint(0, len(pretty_colors)-1)]
        star_size = random.randint(5, 20)
        shapes.draw_star(star_size, star_color)

    mainloop()

draw_sky()
