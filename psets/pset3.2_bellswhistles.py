import timeit

# these imports aren't really necessary except for a charting function i built to visualize the array
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ==========================================================================================================
# =======================================Do not change these lines==========================================


# The timestamps are in 24H format. So, 1921 represents 7:21 PM
def readInput():
    f = open(
        "./names.txt", "r", encoding="utf8"
    )  # open text file containing names in order
    g = open(
        "./timestamps.txt", "r", encoding="utf8"
    )  # open text file containing timestamps in order
    names = []
    tStamps = []
    subs = []

    for line in f:
        names.append(line.strip())  # read names and append to names array

    for line in g:
        tStamps.append(int(line.strip()))  # read timestamps, convert to int and append

    l = len(names)

    if l != len(tStamps):  # In case you make changes to the .txt files
        print("Error in .txt files")  # and end up with inequal rows
        exit(-1)

    for i in range(l):
        subs.append((names[i], tStamps[i]))  # append (name,tStamp) to submissions array

    return subs


# For this section to run, place this .py file in
# a folder containing the attached "names.txt" and "timestamps.txt" files
# ==========================================================================================================
# ==========================================================================================================

subs = readInput()  # subs contains your submissions. It is an array


# NOT my algo, this is just the quicksort given to us, included to compare times with
def quickSort(L, start, stop):

    # protection against stupidity
    # helps us stop in edge cases
    if stop <= start:
        return

    p = partition(L, start, stop)
    quickSort(L, start, p-1)  # sort the "lesser" list
    quickSort(L, p+1,   stop)  # sort the "greater" list


# helper function to draw a bar chart with with the unsorted and sorted array
def chart(array):
    data = pd.DataFrame(array, columns=["name", "timestamp"])
    size_over_years_plot = sns.barplot(data=data, x="name", y="timestamp")
    plt.setp(size_over_years_plot.get_xticklabels(), rotation=75)
    plt.tick_params(axis="x", labelsize=8)
    plt.tick_params(axis="y", labelsize=12)
    plt.show()


# helper function to compare algorithm's results with the actual, expected results
def test(unsorted_subs, sorted_subs, k):

    # just finds the actual results to reference against the results the algo gets
    sorted_array = [element for element in sorted(unsorted_subs, key=lambda x: x[1], reverse=True)[:k]]

    # the results the algo gets
    quicksorted_array = sorted_subs

    # throws an assertion error if the first twenty elements of the builtin-sorted array and the quicksorted array
    # are not the same, ignoring order of elements
    assert(set(sorted_array) == set(quicksorted_array[:k]))


# helper function to time the algorithms
# use the temp functions below to pass as first-class members into the timer function
def timer(function_call, name):
    start = timeit.default_timer()
    function_call()
    end = timeit.default_timer()
    print(f"{str((end - start)*1000)[:10]} milliseconds with {name}")


def temp():
    quickSort(subs, 0, len(subs)-1)


def temp2():
    quick_algorithm(subs, 20, 0, len(subs) - 1)


def temp3():
    extra_credit__selection_sort(subs, 20)


# the partition for the sort
# basically the same as the code we were given except i changed variable names to be easier to keep track of
# i've marked substantive changes with CHANGE:
def partition(array, start, stop):

    pivot_position, pivot_value = start, array[start]

    # start+1 to remove redundant self comparison, stop+1 because range is exclusive
    for current_position in range(start+1, stop+1):

        # CHANGE: use [1] to compare timestamps instead of the entire tuples
        # CHANGE: < to > to sort it descending instead of ascending
        if (
            array[current_position][1] > pivot_value[1]
        ):

            pivot_position = pivot_position + 1
            array[pivot_position], array[current_position] = (
                array[current_position],
                array[pivot_position]
            )
            # move the current element to the end of the first list

    array[pivot_position], array[start] = array[start], array[pivot_position]
    # move the pivot element to the end of the first list

    return pivot_position


# the algorithm is actually closer to quickselect than quicksort tbh
# specifically, it doesn't bother sorting one half of the partition if it can help it

# runs in O(n) average time complexity and O(n^2) worst case

# i switched the recursive calls to tail recursive for efficiency (though it shouldn't affect time complexity)
# added a parameter k, representing the number of largest elements needed. k=20

# note that the algorithm can fail if the k is chosen such that the last element to be included has a non-unique
# timestamp, such as k=190. not sure how to resolve that but since the question doesn't mention how it should be
# handled, i consider it undefined behaviour that shouldn't be held against the algorithm
def quick_algorithm(array, k, start, stop):

    # don't continue if k is out of bounds of the indices of the list
    if 0 < k <= stop - start + 1:

        # partition the array and return the position where the arrays are separated
        pivot_position = partition(array, start, stop)

        # essentially, find out if the left array is of atleast k length
        if pivot_position - start > k - 1:
            # if it is, only sort the left array, otherwise sort the right array
            # the sort essentially ignores half the array as long as it still gets k elements
            quick_algorithm(array, k, start, pivot_position - 1)
        else:
            quick_algorithm(array, k - pivot_position + start - 1, pivot_position + 1, stop)


# a partial selection sort algo
# runs in O(kn) -> assuming k=20 constant, O(20n) = O(n) time
def extra_credit__selection_sort(array, k):
    # loop over the entire array k times
    for step in range(k):

        # designate the kth element as the reference base
        reference_element = step

        # loop over the array
        for element in range(step + 1, len(subs)):

            # if the current element is larger than the base element, designate it as the reference
            if array[element][1] > array[reference_element][1]:
                reference_element = element

        # swap the two elements
        array[step], array[reference_element] = array[reference_element], array[step]


def main():
    # the number of late students to be found
    k = 20

    # chart the unsorted array
    unsorted_subs = [x for x in subs]
    chart(unsorted_subs)

    copyof_subs = [x for x in subs]

    # display the sorted array and test it
    quick_algorithm(subs, k, 0, len(subs) - 1)  # sorts the array
    chart(subs)  # charts the sorted array

    # prints the first twenty elements of the sorted arrays
    # which are the twenty largest elements but in no particular order
    print([element for element in subs[:k]])

    # prints only the names without timestamps, and prints them by descending order of submission
    print([name for name, time in sorted(subs[:k], key=lambda x: x[1], reverse=True)])

    test(unsorted_subs, subs, k)  # tests if the sort is correct

    # the same for the extra credit algo
    print("\n extra credit algo")
    extra_credit__selection_sort(copyof_subs, k)
    chart(copyof_subs)
    print([element for element in copyof_subs[:k]])
    print([name for name, time in sorted(copyof_subs[:k], key=lambda x: x[1], reverse=True)])
    test(unsorted_subs, copyof_subs, k)


if __name__ == '__main__':
    main()
