def missing_number(arr):

    n = len(arr)

    expected_Sum = n*(n+1)//2

    actual_sum = 0

    for i in range(len(arr)):

        actual_sum+=arr[i]

    return expected_Sum- actual_sum

arr = [3, 0, 1]
print(missing_number(arr))