def second_largest(arr):

    if len(arr) < 2:

        return None

    largest = arr[0]

    second =  None

    for i in range(len(arr)):

        if arr[i] > largest:

            second = largest

            largest = arr[i]

        elif arr[i] != largest:

            if second == None  or arr[i] > second:

                second = arr[i]

    return second

arr = [10, 5, 8, 20, 15]

print(second_largest(arr))