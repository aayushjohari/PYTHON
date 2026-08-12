def maxsubarraysum_kadane(arr):

    current =  arr[0]
    maximum = arr[0]

    for i in range(1 , len(arr)):

        current = max(current + arr[i] , arr[i])
        maximum = max(current  , maximum)

    return maximum

arr = [-2, 1, -3, 4, -1, 2, 1]
print(maxsubarraysum_kadane(arr))