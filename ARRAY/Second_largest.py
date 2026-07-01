def second_largest(arr):

    if len(arr) < 2:

        return None

    large = arr[0]

    second = None

    for i in range(len(arr)):

        if arr[i] > large:

            second = large

            large = arr[i]

        elif arr[i] != large:

            if second == None or second < arr[i]:

                second = arr[i]

    return second

arr = list(map(int , input("enter the array: ").split()))

print(second_largest(arr))