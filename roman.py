def interpreter(input_num, step, upper_num, mid_num=""):
	output = step

	if input_num < 4:
		output = mid_num + output*input_num
		return output

	elif input_num <= 5:

		if 5 - input_num:
			return step + upper_num

		else:
			return upper_num


def parser(arabic_number):

	tens_digit = int(arabic_number[-2])
	ones_digit = int(arabic_number[-1])

	if tens_digit > 5:
		tens_output = interpreter(tens_digit-5, "X", "C", "L")
	else:
		tens_output = interpreter(tens_digit, "X", "L")

	if ones_digit > 5:
		ones_output = interpreter(ones_digit-5, "I", "X", "V")
	else:
		ones_output = interpreter(ones_digit, "I", "V")

	return tens_output + "" + ones_output


if __name__ == '__main__':
	print(f"The roman equivalent is: {parser(input('Enter an arabic number: '))}")
