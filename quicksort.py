def quicksort(alist: list):
    if len(alist) < 2:
        return alist
    else:
        pivot = alist[0]
        less = [i for i in alist[1:] if i <= pivot]
        biggish = [i for i in alist[1:] if i > pivot]
        return quicksort(less)+[pivot]+quicksort(biggish)


alist1 = [2, 14, 15, 3, 5, 6, 8, 9]

print(quicksort(alist1))
