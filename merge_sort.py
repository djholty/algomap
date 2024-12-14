
def mergesort(arr):
    n = len(arr)
    m = n//2

    if len(arr) == 1:
        return arr

    left = arr[0:m]
    right = arr[m:]

    L = mergesort(left) #recursively split arrays into left and right sides until length is 1
    R = mergesort(right)

    #merge part
    l , r = 0, 0 #create two indices for left and right arrays
    left_len = len(L)
    right_len = len(R)
    sorted_array = [0]*(left_len + right_len)

    i = 0
    while l < left_len and r < right_len: #pick smallest number from r or left
        if L[l] < R[r]:
            sorted_array[i] = L[l]
            l += 1
            i += 1
        else:
            sorted_array[i] = R[r]
            r +=1
            i +=1

    while l < left_len: #once all right is used, finish with left
        sorted_array[i] = L[l]
        l += 1
        i += 1

    while r < right_len: #if left all used, finish with right
        sorted_array[i] = R[r]
        r += 1
        i += 1
    
    return sorted_array





