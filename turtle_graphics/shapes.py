# shapes.by
# By Aspen
# A module for drawing shapes with the built-in turtle module for Python3

from turtle import *

# 1. An equilateral triangle
def draw_triangle_up(size, pcolor='black', fcolor='white', wait=False):
    pencolor(pcolor)
    fillcolor(fcolor)
    begin_fill()
    for i in range(3):
        forward(size)
        left(120)
    end_fill()
    if wait:
        mainloop()
#draw_triangle_up()

def draw_triangle_down(size, pcolor='black', fcolor='white', wait=False):
    pencolor(pcolor)
    fillcolor(fcolor)
    begin_fill()
    for i in range(3):
        forward(size)
        right(120)
    end_fill()
    if wait:
        mainloop()
#draw_triangle_down()

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
def draw_trapezoid(size, pcolor='black', fcolor='white', wait=False):
    pencolor(pcolor)
    fillcolor(fcolor)
    begin_fill()
    forward(size)
    left(120)
    forward(size/2)
    left(60)
    forward(size/2)
    left(60)
    forward(size/2)
    left(120)
    forward(size)
    end_fill()
    if wait:
        mainloop()
#draw_trapezoid(100, pcolor='blue', fcolor='lightblue')

def draw_trapezoid_mirror(size, pcolor='black', fcolor='white', wait=False):
    pencolor(pcolor)
    fillcolor(fcolor)
    begin_fill()
    forward(size/2)
    right(120)
    forward(size/2)
    right(60)
    forward(size/2)
    right(60)
    forward(size)
    right(120)
    forward(size)
    end_fill()
    if wait:
        mainloop()
#draw_trapezoid(100, pcolor='blue', fcolor='lightblue')

def draw_rhombus(size, pcolor='black', fcolor='white', wait=False):
    pencolor(pcolor)
    fillcolor(fcolor)
    begin_fill()
    forward(size)
    left(120)
    forward(size)
    left(60)
    forward(size)
    left(120)
    forward(size)
    left(60)
    end_fill()
    if wait:
        mainloop()
#draw_rhombus(100)

def draw_rhombus_mirror(size, pcolor='black', fcolor='white', wait=False):
    pencolor(pcolor)
    fillcolor(fcolor)
    begin_fill()
    forward(size)
    right(120)
    forward(size)
    right(60)
    forward(size)
    right(120)
    forward(size)
    right(60)
    end_fill()
    if wait:
        mainloop()
#draw_rhombus(100)
