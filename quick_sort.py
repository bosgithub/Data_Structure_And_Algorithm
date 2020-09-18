''' Quick Sort Algorithm

    this algorithm orders an unordered list of elements by picking a pivot
    element within the list and compare each and every element within the
    list to break the original list into 2 lists, larger than pivot and
    less than pivot, this runs recursively until the smallest list is 1
    then every list is combined to form the ordered list

    #####################################################################
    the trick of this quick sort algorithm is cleverly picking the pivot,
    worst case is when extreams are selected as the pivot'''


def quick_sort(sequence):
    # length here returns the length of our data sequence
    length = len(sequence)
    # if the lenght of list is of a single element just return the element
    if length <= 1:
        return sequence

    else:
        # we label one of the element in the list "pivot" in order to compare
        # other elements to this pivot element to position accordingly
        pivot = sequence.pop()

    # here we define 2 lists, one list contains elements less than pivot from
    # our original sequence, other list contain elements greater than pivot
    items_greater = []
    items_lower = []

    for item in sequence:  # passing through our sequence
        if item > pivot:   # compare each elements in our sequence with pivot
            # add element to items_greater if larger than pivot
            items_greater.append(item)

        else:
            # add element to items_lower if smaller or equal than pivot
            items_lower.append(item)
    # pass sequence recursively until lenghth is 1 and combine every list
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
