import random

# not really part of the algo, just needed to run it
def generate_list():
    list_size = random.randrange(10, 20, 1)

    elements = []
    majority_element = random.randint(0, 100)

    # put 50%+1 of the majority element in the list
    for i in range(0, (int(list_size / 2) + 1)):
        elements.append(majority_element)

    # fill the rest of the list with random numbers
    for i in range(0, (int(list_size / 2) - 1)):
        elements.append(random.randint(0, 100))

    random.shuffle(elements)

    print(f"for the list \n{elements}\naccepted as input\n")
    return elements


# the boyer moore algorithm
def find_majority(elements):
    current_leader = elements[0]
    lead_margin = 1

    for element in elements[1:]:

        # if the ball drawn is the same colour as the current leading element
        if element == current_leader:
            lead_margin += 1

        # if the ball drawn creates a new leading element
        elif (element != current_leader) and (lead_margin == 0):
            current_leader = element
            lead_margin = 1

        # if the ball drawn is a different colour
        else:
            lead_margin -= 1

    return current_leader


if __name__ == "__main__":
    print(f"the majority element is {find_majority(generate_list())}")
