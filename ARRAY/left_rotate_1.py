def left_rotate_by_1(arr):

    x = arr[0]

    for i in range(1 , len(arr)):

        arr[i-1] = arr[i]

    arr[len(arr)-1] = x

    return arr

arr =  [1,2,3,4,5]

print(left_rotate_by_1(arr))