def maximumSubarrayProduct(arr):

    current_max = arr[0]
    current_min = arr[0]
    max_product = arr[0]

    for i in range(1 ,len(arr)):

        if arr[i] < 0 :

            current_max , current_min = current_min , current_max

        current_max = max(current_max*arr[i] , arr[i])
        current_min = min(current_min*arr[i] , arr[i])

        max_product = max(current_max , max_product)

    return max_product

arr = [2,3,-2,4]
print(maximumSubarrayProduct(arr))