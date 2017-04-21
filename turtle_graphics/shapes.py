# shapes.by
# By Aspen
# A module for drawing shapes with the built-in turtle module for Python3

from turtle import *

# 1. An equilateral triangle
def draw_triangle(size, color, wait=False):
    pencolor(color)
    fillcolor(color)
    for i in range(3):
        forward(size)
        left(120)
    if wait:
        mainloop()
#draw_triangle()

# 2. A square
def draw_square(size, color, wait=False):
    pencolor(color)
    fillcolor(color)
    for i in range(4):
        forward(size)
        left(90)
    if wait:
        mainloop()
#draw_square()

# 3. A pentagon
def draw_pentagon(size, color, wait=False):
    pencolor(color)
    fillcolor(color)
    for i in range(5):
        forward(size)
        left(72)
    if wait:
        mainloop()
#draw_pentagon(100, 'black', wait=True)

# 4. A hexagon
def draw_hexagon(size, color, wait=False):
    pencolor(color)
    fillcolor(color)
    for i in range(6):
        forward(size)
        left(60)
    if wait:
        mainloop()
#draw_hexagon()

# 5. An octagon
def draw_octagon(size, wait=False):
    pencolor(color)
    fillcolor(color)
    for i in range(8):
        forward(size)
        left(45)
    if wait:
        mainloop()
#draw_octagon()

# 6. A star
def draw_star(size, color, wait=False):
    pencolor(color)
    fillcolor(color)
    for i in range(5):
        forward(size)
        right(144)
    if wait:
        mainloop()
#draw_star(200, 'black')

# 7. A circle
def draw_circle(size, color, wait=False):
    pencolor(color)
    fillcolor(color)
    circle(size)
    mainloop()
#draw_circle()

# BONUS STUFF
def draw_trapezoid(size, pcolor, fcolor, wait=False):
    pencolor(pcolor)
    fillcolor(fcolor)
    forward

# def draw_stuff():
#     print("\nINSTRUCTIONS: You can draw lots of stuff. It's so cool man. Here's what you can draw:\n\ntriangle\nsquare\npentagon\nhexagon\noxagon\nstar\ncircle")
#
#     ans = input("\nWhat do you want to draw? ")
#
#     shapes = {  "triangle" : draw_triangle(),
#                 "square" : draw_square(),
#                 "pentagon" : draw_pentagon(),
#                 "hexagon" : draw_hexagon(),
#                 "oxagon" : draw_octagon(),
#                 "star" : draw_star(),
#                 "circle" : draw_circle() }
#
#
#     shapes.get(ans)
#
#
# if __name__ == "__main__":
#     draw_stuff()
