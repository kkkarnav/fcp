
def q3(start, stop):
	first, second = 0, 1
	for i in range(start, stop):
		if not (i + 1) % 4:
			print(f"{i}th term is: {first}")
		first, second = first + second, first

if __name__ == "__main__":
	n = 20
	q3(0, n)
