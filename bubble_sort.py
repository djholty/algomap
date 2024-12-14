def bubblesort(arr):
    n = len(arr)
    isSorted = False

    while not isSorted:
         isSorted = True
         for i in range(1, n):
            if arr[i] < arr[i-1]: #if value on right is smaller than left, swap
                arr[i], arr[i-1] = arr[i-1], arr[i]
                isSorted = False
    return arr
