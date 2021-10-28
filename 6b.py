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


def drawPolygon(t, sides, size):
	# we need to return a list of vertices
	vertices = [None] * sides  # vertices = []

	angle = 360.0 / sides  # play around with this
	for i in range(sides):
		vertices[i] = t.pos()  # vertices.append(  t.pos()  )
		t.forward(size)
		t.right(angle)
	# loop ends

	return vertices


def drawEpicycloid(t, x, y, num_vertices, size, multiplier):
	moveto(x, y)
	vertices = drawPolygon(t, num_vertices, size)

	used_vertices = [False] * num_vertices

	for current_vertex in range(1, num_vertices):

		moveto(*(vertices[current_vertex]))

		# bounce around the polygon, stopping only when you hit a used vertex
		while not used_vertices[current_vertex]:
			used_vertices[current_vertex] = True  # this vertex is now used
			next_vertex = (current_vertex * multiplier) % num_vertices  # using a different multiplier will change the shape!
			t.setposition(vertices[next_vertex])
			current_vertex = next_vertex


if __name__ == "__main__":
	print("hello world")

	# for 6 part b
	n = 10
	polygon_vertices = drawPolygon(t, n, 100)
	for vertex in polygon_vertices:
		drawEpicycloid(t, *(vertex), 100, 5, 20)

	turtle.done()
