import random


def generate_list(size):

    random_list = [x for x in range(0, size)]
    random.shuffle(random_list)
    print(f"random list: {random_list}")
    return random_list


def odd_even_sort(random_list):
    even_nums = [random_list[x] for x in range(len(random_list)) if x % 2 == 0]
    odd_nums = [random_list[x] for x in range(len(random_list)) if x % 2 == 1]

    even_nums, odd_nums = sorted(even_nums), sorted(odd_nums)

    sorted_evens_list = [item for sublist in list(zip(even_nums, odd_nums)) for item in sublist]

    return sorted_evens_list


def chunk_sort(random_list, k):
    chunks = []

    for i in range(0, len(random_list)-k, k):
        chunks.append([random_list[i], random_list[i+1], random_list[i+2]])

    if len(random_list) % k != 0:
        chunks.append([*(random_list[i+k:])])

    chunks = [sorted(chunk) for chunk in chunks]
    sorted_chunk_list = [item for sublist in chunks for item in sublist]

    return sorted_chunk_list


def main():
    generated_list = generate_list(10)  # part A

    even_sorted = odd_even_sort(generated_list)
    print(f"even sorted: {even_sorted}")  # part B

    chunk_sorted = chunk_sort(even_sorted, 3)
    print(f"chunk sorted: {chunk_sorted}")  # part C


if __name__ == '__main__':
    main()
