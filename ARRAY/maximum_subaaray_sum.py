def maximum_subarray_sum(arr ,  k):

    curr = 0 

    for i in range(k):

        curr =  curr + arr[i]

    res = curr

    for i in range(k  , len(arr)):

        curr = curr + arr[i] - arr[i-k]

        res = max(res , curr)

    return res

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(maximum_subarray_sum(arr , k))
