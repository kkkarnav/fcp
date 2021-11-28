import turtle
import random


def drawPolygon(t, sides, size):
    # we need to return a list of vertices
    vertices = []

    angle = 360.0 / sides  # play around with this
    for i in range(sides):
        vertices.append(t.pos())
        t.forward(size)
        t.right(angle)
    # loop ends

    return vertices


def drawEpicycloid(T, multiplier, vertices, size):
    numVertices = vertices  # number of vertices or sides
    sideSize = size
    v = drawPolygon(T, numVertices, sideSize)

    # ==========================

    used = [False] * numVertices

    # do this for all values of current from 1 to 199
    for current in range(1, numVertices):
        T.penup()
        T.setposition(v[current])
        T.pendown()

        while not used[current]:
            used[current] = True  # marking this place as used

            nextVertex = (current * multiplier) % numVertices

            # draws a line from current position to v[nextVertex]

            T.setposition(v[nextVertex])

            current = nextVertex


# ==================================================


def paint_tree(tortoise, branch):

    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                tortoise.color("snow")
            else:
                tortoise.color("lightcoral")
            tortoise.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1):
                tortoise.color("snow")
            else:
                tortoise.color("lightcoral")
            tortoise.pensize(branch / 2)
        else:
            tortoise.color("sienna")
            tortoise.pensize(branch / 10)

        tortoise.forward(branch)
        a = 1.5 * random.random()
        tortoise.right(20 * a)
        b = 1.5 * random.random()
        paint_tree(tortoise, branch - 10 * b)
        tortoise.left(40 * a)
        paint_tree(tortoise, branch - 10 * b)
        tortoise.right(20 * a)
        tortoise.penup()
        tortoise.backward(branch)
        tortoise.pendown()


def paint_flowers(tortoise, num_of_petals):
    tortoise.pensize(1)
    base_pos = tortoise.pos()
    base_heading = tortoise.heading()

    for i in range(num_of_petals):
        tortoise.color("yellow")

        x = 150 - (300 * random.random())
        y = 120 - (100 * random.random())

        # move to random position
        tortoise.penup()
        tortoise.forward(y)
        tortoise.left(90)
        tortoise.forward(x)
        tortoise.pendown()

        # drawPolygon(tortoise, 100, 1)
        drawEpicycloid(tortoise, 41, 50, 1)
        tortoise.setheading(270)
        tortoise.color("green")
        tortoise.forward(y)

        # move to back to og position
        tortoise.penup()
        tortoise.setposition(base_pos)
        tortoise.setheading(base_heading)
        tortoise.pendown()


def draw_central_figure(t):

    t.left(90)
    t.penup()
    t.backward(150)
    t.pendown()
    t.color("sienna")

    # Painting the trunk of Cherry Blossom
    paint_tree(t, 60)
    # spirits
    paint_flowers(t, 20)


def draw_sun(t):
    t.pencolor("yellow")
    t.penup()
    t.setposition(200, 200)
    t.pendown()
    drawEpicycloid(t, 181, 200, 1)


if __name__ == "__main__":
    # setup
    t = turtle.Turtle()
    turtle.tracer(5, 0)
    turtle.colormode(255)
    turtle.bgcolor("wheat")
    t.hideturtle()

    draw_central_figure(t)
    draw_sun(t)
    turtle.done()
