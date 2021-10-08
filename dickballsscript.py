import turtle

print("hello world")


def setUp():
	tortoise = turtle.Turtle()
	tortoise.pencolor('#545454')
	tortoise.speed(0)
	return tortoise


def tearDown():
	turtle.done()


def drawCircle(tortoise, angle):
	for i in range(angle):
		tortoise.forward(0.5)
		tortoise.right(1)


def drawBar(tortoise):
	tortoise.forward(20)
	tortoise.left(90)
	tortoise.forward(200)

	drawCircle(tortoise, 180)

	tortoise.forward(200)
	tortoise.left(90)
	tortoise.forward(20)


if __name__ == '__main__':
	turtle_object = setUp()

	drawCircle(turtle_object, 360)

	drawBar(turtle_object)

	drawCircle(turtle_object, 360)

	tearDown()
