def max_circular_array(arr):

    max_sum  = arr[0]
    curr_sum  = arr[0]

    total = 0

    min_sum = arr[0]
    curr_min = arr[0]

    for i in range(len(arr)):

        total += arr[i]

        if i > 0 :
            curr_sum = max(arr[i] , curr_sum + arr[i])
            max_sum  = max(curr_sum , max_sum)

            curr_min = min(arr[i] , curr_min + arr[i])
            min_sum = min(curr_min, min_sum)

        if max_sum < 0:
            return max_sum

        circular_sum  = total - min_sum
    return max(circular_sum, max_sum)

arr = [1,-2,3,-2]
print(max_circular_array(arr))
