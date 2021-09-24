import math

def judith(number):

	print(f'after step 1: {number}')

	# step 2
	while number%7:
		number = number + 2

	print(f'after step 2: {number}')

	# step 3
	for divisor in range(2, math.ceil(number/2)+1):
		if not (number%divisor):
			number = number * divisor
			break

	print(f'after step 3: {number}')

	# step 4
	number = number + 100

	print(f'after step 4: {number}')

	# step 5
	while number < 10000:
		number = number * 20

	print(f'after step 5: {number}')

	# step 6
	while number%11:
		number = number + 1

	print(f'after step 6: {number}')

	return number

############################################

def douglas(number):

	print(f'after step 1: {number}')

	# step 2
	number = number * (1/number)

	print(f'after step 2: {number}')

	# step 3
	number = round(number)

	print(f'after step 3: {number}')

	# step 4
	for repeat in range(0, 2):
		number = number/6

	print(f'after step 4: {number}')

	# step 5
	number = number * 1296

	print(f'after step 5: {number}')

	return number

if __name__ == '__main__':
	# print(judith(input("input a number greater than 104: ")))
	print(judith(107))
	print(douglas(2/5))
