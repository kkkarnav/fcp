import math
from images_fcp import *

array = readImage("xi.jpg")
width, height = len(array[0]), len(array)  # 2560, 1707

kernel = [
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]
]


# blur or sharpen A with K
def apply_kernel(A, K):
	B = [[(255, 255, 0) for column in row] for row in A]

	for row in range(len(A)):  # height-wise
		for column in range(len(A[row])):  # width-wise

			B[row][column] = multiply(A, K, row, column, len(A), len(A[row]))

	return B


# generate colour pattern
def create_pattern(pattern, height, width):
	for row in range(width):
		for col in range(height):
			nb = ((255 - (row + col) * 1.2) / 4) % 255

			pattern[col][row] = (pattern[col][row][0] - nb, pattern[col][row][1] - nb, nb)

	return pattern


def surround(A, k):
	B = [[(0, 0, 0) for column in range(len(A[0]) + (k))] for row in range(len(A) + (k))]

	for row in range(k * 2, len(A[0]) - k - 1):
		for col in range(k * 2, len(A) - k - 1):
			B[col][row] = A[col][row]

	return B


if __name__ == '__main__':
	# Note that the original lenna.png is square but this one isn't
	q2 = array

	# Subpart 1
	reverse_q2 = [[(255 - (q2[row][column][0]), 255 - (q2[row][column][1]), 255 - (q2[row][column][2])) for column in
	               range(len(q2[0]))] for row in range(len(q2))]

	# Subpart 2
	detected_reverse_q2 = apply_kernel(reverse_q2, kernel)

	# Subpart 3
	blue = create_pattern(q2, len(q2), len(q2[0]))

	# Subpart 4
	k = 10
	bordered = surround(blue, int(k / 4))

	writeImage(reverse_q2, "q2_reverse.jpg")
	writeImage(detected_reverse_q2, "q2_detected.jpg")
	writeImage(blue, "blue.jpg")
	writeImage(bordered, "bordered.jpg")
