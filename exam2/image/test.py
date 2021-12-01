import math
from images_fcp import *


array = readImage("lenna.png")
width, height = len(array[0]), len(array)  # 2560, 1707

kernel = [
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]
]

# turn the array left by 90 degrees
def transpose(A):

	B = [[(255, 255, 0) for row in A] for column in A[0]]

	assert(len(B[0]) == len(A))
	assert(len(B) == len(A[0]))

	for row in range(len(A)):  # height-wise
		for column in range(len(A[row])):  # width-wise

			# A[row][column] rotates 90 left
			# A[len(A)-row-1][column] rotates 90 right
			B[column][row] = A[row][column]
	
	return B


# mirror the array vertically
def yflip(A):

	B = [[(255, 255, 0) for column in row] for row in A]

	for row in range(len(A)):  # height-wise
		for column in range(len(A[row])):  # width-wise

			B[row][len(A[row])-column-1] = A[row][column]

	return B


# mirror the array horizontally
def xflip(A):

	B = [[(255, 255, 0) for column in row] for row in A]

	for row in range(len(A)):  # height-wise
		for column in range(len(A[row])):  # width-wise

			B[len(A)-row-1][column] = A[row][column]

	return B


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

			nb = ((255 - (row+col)*1.2)/4)%255

			pattern[col][row] = (pattern[col][row][0]-nb, pattern[col][row][1]-nb, nb)

	return pattern


def surround(A, k):

	B = [[(0, 0, 0) for column in range(len(A[0])+(k))] for row in range(len(A) + (k))]

	for row in range(k*2, len(A[0])-k-1):
		for col in range(k*2, len(A)-k-1):
			B[col][row] = A[col][row]

	return B


if __name__ == '__main__':
	
	# add a colour filter
	filtered_array = [[(array[row][column][0], array[row][column][1], array[row][column][2]) for column in range(width)] for row in range(height)]

	# rotate or mirror the array
	mirrored_array = xflip(yflip(transpose(array)))

	# apply image kernel
	output_array = apply_kernel(array, kernel)

	# generate colour pattern
	# pattern_array = create_pattern(800, 500)


	q2 = array
	reverse_q2 = [[(255-(q2[row][column][0]), 255-(q2[row][column][1]), 255-(q2[row][column][2])) for column in range(len(q2[0]))] for row in range(len(q2))]
	detected_reverse_q2 = apply_kernel(reverse_q2, kernel)

	blue = create_pattern(q2, len(q2), len(q2[0]))
	bordered = surround(blue, 10)

	writeImage(blue, "blue.jpg")
	writeImage(reverse_q2, "q2_reverse.jpg")
	writeImage(detected_reverse_q2, "q2_detected.jpg")
	writeImage(bordered, "bordered.jpg")
