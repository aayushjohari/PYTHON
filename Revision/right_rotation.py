def right_rotation(arr , d):

    rotation(arr, 0 , len(arr)-1)

    rotation(arr, 0 , d-1)

    rotation(arr, d , len(arr)-1)

    return arr

def rotation(arr , left, right):

    while left  < right:

        arr[left]  , arr[right] = arr[right] , arr[left]

        left+=1

        right-=1

arr = [1, 2, 3, 4, 5]
d = 2

print(right_rotation(arr, d))
    