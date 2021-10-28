import random


# ==================================================
def partitionTerrible(L, start, stop):
	pivot = L[start]

	# go through the list L
	# split the elements into a lesser and a greater pile
	lesser = []
	greater = []
	for i in range(start + 1, stop + 1):
		if L[i] < pivot:
			lesser.append(L[i])
		else:
			greater.append(L[i])

	L[start:stop + 1] = lesser + [pivot] + greater

	return start + len(lesser)  # final position of the pivot element


# ==================================================
def partitionBetter(L, start, stop):
	pivot = L[start]
	wall = start

	for scout in range(start + 1, stop + 1):
		if L[scout] < pivot:
			wall = wall + 1
			L[wall], L[scout] = L[scout], L[wall]
	# LOOP ENDS HERE

	L[wall], L[start] = L[start], L[wall]
	return wall  # returning to us the index/position of the pivot


def quickSort(list, start, top):
    if top <= start:
        return
    p = start
    q = top
    k = p+1
    h = k
    l = q-1
    if list[p] > list[q]:
        list[p], list[q] = list[q], list[p]
    while k <= l:
    # the last non-check index is l,as l+1 to top - 1 is the part III,
    #where all elements > list[top]
        if list[k] < list[p]:
            list[h], list[k] = list[k], list[h]
            #h is the first element of part II
            h += 1
            #increase h by 1, for pointing to the first element of part II
            k += 1
            #increase k by 1, because we have checked list[k]
        elif list[k] > list[q]:
        #l is the last element of part IV
            list[k], list[l] = list[l], list[k]
            #don't increase k, as we have not check list[l] yet
            l -= 1
            #after swap, we should compare list[k] with list[p] and list[q] again
        else: k += 1
        # no swap, then the current k-th value is in part II, thus we plus 1 to k
    h -= 1#now,h is the last element of part I
    l += 1 #now, l is the first element of part III
    list[p], list[h] = list[h], list[p]
    list[q], list[l] = list[l], list[q]
    quickSort(list, start, h-1)
    quickSort(list, h+1, l-1)
    quickSort(list, l+1, top)



# ==================================================
def blah():
	# create a shuffled list of length n, starting from 100
	n = 16
	X = list(range(100, 100 + n))
	random.shuffle(X)
	print(f"Initially, X = {X}")

	quickSort(X, 0, len(X) - 1)
	print(X)


blah()
