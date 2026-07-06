def max_profit(arr):

    min_price = arr[0]

    max_profit = 0

    for i in range(1  , len(arr)):

        if arr[i] < min_price :

            min_price = arr[i]

        else:

            profit = arr[i] - min_price

            max_profit = max(max_profit , profit)

    return max_profit

arr = [7,6,4,3,1]

print(max_profit(arr))