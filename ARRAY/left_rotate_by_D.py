def left_rotation(arr , d):

    reverse(arr , 0 , d-1)

    reverse(arr , d , len(arr)-1)

    reverse(arr, 0 , len(arr)-1)

    return arr

def reverse(arr , left , right):

    while left < right:

        arr[left] , arr[right] = arr[right] , arr[left]

        left+=1

        right-=1

arr = [1,2,3,4,5]

print(left_rotation(arr, 4))



