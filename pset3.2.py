import math
import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina.color("black")
tina.speed(0)


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

		while used[current] == False:
			used[current] = True  # marking this place as used

			nextVertex = (current * multiplier) % numVertices

			# draws a line from current position to v[nextVertex]

			T.setposition(v[nextVertex])
			drawPetal(T)

			current = nextVertex


def drawSunflower(t, numseeds, numpetals, angle, cspread):
	t.fillcolor("orange")
	phi = angle * (math.pi / 180.0)

	for i in range(numpetals):
		# figure out the next x, y position
		r = cspread * math.sqrt(i)
		theta = i * phi
		x = r * math.cos(theta)
		y = r * math.sin(theta)

		# move the turtle and orient it correctly
		t.penup()
		t.goto(x, y)
		t.setheading(i * angle)
		t.pendown()

		drawPetal(t)


def drawPetal(t):
	t.fillcolor("yellow")
	t.begin_fill()
	t.right(20)
	t.forward(70)
	t.left(40)
	t.forward(70)
	t.left(140)
	t.forward(70)
	t.left(40)
	t.forward(70)
	t.end_fill()


turtle.tracer(0)
drawEpicycloid(tina, 161, 200, 10)

tina.hideturtle()
turtle.done()
