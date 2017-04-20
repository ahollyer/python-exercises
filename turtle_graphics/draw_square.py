from turtle import *

def draw_square():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    draw_square()
    mainloop()
draw_square()
