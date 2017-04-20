# shapes.by
# By Aspen
# A module for drawing shapes with the built-in turtle module for Python3

from turtle import *

# 1. An equilateral triangle
def draw_triangle():
    for i in range(3):
        forward(100)
        left(120)
    mainloop()
#draw_triangle()

# 2. A square
def draw_square():
    for i in range(4):
        forward(100)
        left(90)
    mainloop()
#draw_square()

# 3. A pentagon
def draw_pentagon():
    for i in range(5):
        forward(100)
        left(72)
    mainloop()
#draw_pentagon()

# 4. A hexagon
def draw_hexagon():
    for i in range(6):
        forward(100)
        left(60)
    mainloop()
#draw_hexagon()

# 5. An octagon
def draw_octagon():
    for i in range(8):
        forward(100)
        left(45)
    mainloop()
#draw_octagon()

# 6. A star
def draw_star():
    for i in range(5):
        forward(200)
        right(144)
    mainloop()
#draw_star()

# 7. A circle
def draw_circle():
    circle(100)
    mainloop()
draw_circle()
