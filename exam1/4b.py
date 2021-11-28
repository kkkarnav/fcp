def q2(stop_value):
    first, second = 0, 1
    i = 0
    while first < stop_value:
        print(f"{i}th term is: {first}")
        first, second = first + second, first
        i += 1


if __name__ == "__main__":
    n = 20
    q2(n)
