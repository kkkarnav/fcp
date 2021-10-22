import turtle
import math

# wasn't sure if we were allowed to use turtle.circle() so i've done it manually

# turtle configs
t = turtle.Turtle()
t.pencolor("#545454")
t.speed(0)


# helper function to move the turtle to a coordinate without drawing a line to it
def moveto(x, y):
	t.penup()
	t.setposition(x, y)
	t.pendown()


# helper function to draw curves with angles = angle, of radius = radius
def drawCircle(angle, radius):
	for i in range(angle):
		t.forward(((2 * math.pi * radius) / 360))
		t.left(1)


# draws a square with sides of length side, centred around (x, y)
# could've done this a little simpler but felt cleaner to have the square centred
def drawSquare(x, y, side):
	moveto(x, y)
	for i in range(8):
		t.forward(side / 2)
		t.left(90 if i % 2 else 0)
	moveto(x, y)


# tilts the turtle, sets the side using the pythagoras theorem and delegates to drawSquare()
def drawTiltedSquare(x, y, side):
	moveto(x, y)
	t.left(45)
	diagonal_side = math.sqrt(2 * (side * side)) / 2
	drawSquare(x, y, diagonal_side)
	moveto(x, y)


# calls drawSquare() and drawTiltedSquare() in sequence
def squareInSquare(x, y, side):
	t.setheading(0)
	drawSquare(x, y, side)
	drawTiltedSquare(x + (side / 2), y, side)


# for every iteration, double the side length and call squareInSquare()
def fractal(x, y, startSide, k):
	moveto(x, y)
	for i in range(
			1, k + 1
	):  # starting with 1 to avoid multiplying with 0 on the first run
		t.setheading(0)
		startSide *= 2
		squareInSquare(x - (startSide / 2), y - (startSide / 2), startSide)
	# ^ the -startSide/2 just centres the squares around the centre
	# 	instead of the bottom right corner

	# could've done this recursively instead of iteratively but the loop felt better
	"""if k:
		t.setheading(0)
		squareInSquare(x - (startSide / 2), y - (startSide / 2), startSide)
		startSide *= 2
		fractal(x, y, startSide, k - 1)"""


# calls fractal(), then calls drawCircle() to draw
# 	semicircles with increasing startLength as radius
def spiralOut(x, y, startLength, k):
	fractal(x, y, startLength, k)
	moveto(x, y)
	for i in range(k * 2):
		drawCircle(180, startLength * (i * 2))


# calls fractal(), then calls drawCircle() to draw
# 	semicircles with increasing startRadius as radius,
# 	in fibonacci ratio
def drawFibonacci(x, y, startRadius, loops):
	fractal(x, y, startRadius, loops)
	moveto(x, y)
	i, j = startRadius, startRadius
	for loop in range(loops):
		drawCircle(180, (10 * i))  # the question said semicircle so 180,
		# for the actual golden spiral set the first parameter to 90
		i, j = i + j, i
		print(f"{i}, {j}")


if __name__ == "__main__":
	# drawSquare(0, 0, 50)  # part (a)
	# drawTiltedSquare(0, 0, 50)  # part (b)
	# squareInSquare(0, 0, 80)  # part (c)
	# fractal(0, 0, 10, 10)  # part (d)
	# spiralOut(0, 0, 20, 10)  # part (e)
	# drawFibonacci(0, 0, 2, 10)  # extra credit
	turtle.done()
