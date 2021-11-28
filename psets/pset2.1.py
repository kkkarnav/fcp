import turtle
import math

# turtle configs
t = turtle.Turtle()
t.pencolor("#545454")
t.speed(0)


# helper function to move the turtle to a coordinate without drawing a line to it
def moveto(x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()


def drawSpiral(x, y, radius, loops):
    moveto(x, y)
    start_radius = radius  # allows me to increment radius by a constant figure
    for i in range(
        1, loops + 1
    ):  # starting with 1 to avoid multiplying with 0 on the first run
        for j in range(180):  # 180 for semicircles
            t.forward(((2 * math.pi * radius) / 360))  # circumference formula
            t.left(1)
        radius = start_radius + (i * 10)  # increments radius


# this is pretty much the same but adds a moveto() call to center the pentagons
# 	and swaps out the circumference formula
def drawPentagon(x, y, side, loops):
    moveto(x, y)
    start_side = side
    for i in range(1, loops + 1):
        moveto(x - (side / 2 + i), y - (side / 2 + i))
        for j in range(5):
            t.forward(side)
            t.left(72)
        side = start_side + (i * 20)


# it would've been easier to handle the increasing radius with a function call to
# 	something like drawCircle() but i wasn't sure if Ron would understand something like that


if __name__ == "__main__":
    # drawSpiral(0, 0, 50, 20)  # part (a)
    # drawPentagon(0, 0, 100, 20)  # part (b)
    turtle.done()
