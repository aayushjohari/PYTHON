def max_even_odd_subarray(arr):

    curr = 1
    maximum = 1

    for i in range(1 , len(arr)):

        if arr[i]%2 != arr[i-1]%2:
            curr += 1
        else:
            curr = 1

        maximum = max(curr , maximum)

    return maximum

arr = [10, 12, 14, 7, 8, 9, 10]
print(max_even_odd_subarray(arr))