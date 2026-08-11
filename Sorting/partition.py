def partition(arr  , index):
    n = len(arr)
    arr[index]  , arr[n-1] = arr[n-1] , arr[index]
    temp =[]

    for i in range(n):
        if arr[i] <= arr[n-1]:
            temp.append(arr[i])

    for i in range(n):
        if arr[i] > arr[n-1]:
            temp.append(arr[i])

    for i in range(n):
        arr[i] = temp[i]

    return arr

arr = [5, 13, 6, 9, 12, 8,11]

print(partition(arr , 5))

    


    