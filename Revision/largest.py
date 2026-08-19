def largest(arr):

    maximum = arr[0]

    for i in range(len(arr)):

        if maximum < arr[i]:

            maximum = arr[i]

    return maximum

arr =  [1,2,3,51,2,22]

print(largest(arr))
