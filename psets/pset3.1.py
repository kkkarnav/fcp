# didn't use debayan's code as base so i reimplemented the example triangle for reference
def triangle_example(total_lines):

    for current_line in range(total_lines):

        for space in range(0, current_line, 1):
            print(" ", end="")

        for number in range(total_lines - current_line - 1, -1, -1):
            print(number, end="")

        print()
    print("\n")


def triangle_1(total_lines):

    for current_line in range(total_lines):

        for space in range(0, total_lines - current_line - 1, 1):
            print(" ", end="")

        for number in range(current_line, -1, -1):
            print(number, end="")

        print()
    print("\n")


def triangle_2(total_lines):

    for current_line in range(total_lines):

        for number in range(0, current_line + 1, 1):
            print(number, end="")

        for space in range(0, total_lines - current_line - 1, 1):
            print(" ", end="")

        print()
    print("\n")


def triangle_3(total_lines):

    for current_line in range(total_lines):

        for number in range(0, total_lines - current_line, 1):
            print(number, end="")

        for space in range(0, current_line, 1):
            print(" ", end="")

        print()
    print("\n")


def diagonal(total_lines):

    # it's the same as the code provided in 3-1 except the order of iteration of i is reversed
    for i in range(total_lines - 1, -1, -1):
        for j in range(0, i):
            print(" ", end="")
        print(i)


# triangle_example(5)
triangle_1(5)  # Triangle A
triangle_2(5)  # Triangle B
triangle_3(5)  # Triangle C

diagonal(5)  # Diagonal for D
