def q1(start, stop):
    first, second = 0, 1
    for i in range(start, stop):
        print(f"{i}th term is: {first}")
        first, second = first + second, first


if __name__ == "__main__":
    n = 20
    q1(0, n)
