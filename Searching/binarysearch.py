def binary_search(arr , x):

    left =  0

    right  = len(arr) - 1

    while left <= right :

        mid = (left + right) // 2

        if arr[mid]  == x:

            return mid 

        elif arr[mid] < x :

            left = mid + 1

        else:

            right = mid -1

    return -1

arr = [10,20,21,30 ,34,45]
print(binary_search(arr , 30))