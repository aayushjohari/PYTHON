def partition(arr):

    pivot = len(arr)-1

    pos = 0 

    for i in range(len(arr)-1):

        if arr[i] <= arr[pivot]:

            arr[i] , arr[pos] = arr[pos] , arr[i]

            pos+=1

    arr[pos] , arr[pivot] = arr[pivot] , arr[pos]

    return pos

arr = [5, 13, 6, 9, 12, 8, 11]
print(partition(arr))
print(arr)