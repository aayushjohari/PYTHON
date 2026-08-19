def buy_sell(arr):

    min_price = arr[0]

    max_profit = 0 

    for i in range(1 , len(arr)):

        if arr[i] < min_price:

            min_price = arr[i]

        else:

            profit = arr[i] - min_price

            max_profit = max(profit , max_profit)

    return max_profit

arr = [7,1,5,3,6,4]
print(buy_sell(arr))
