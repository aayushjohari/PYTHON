def swapping_two_index(arr , index1 , index2):

    temp = arr[index1]

    arr[index1] = arr[index2]

    arr[index2] = temp

    return arr

arr = [10,20,30,40,50,60,70]
print(swapping_two_index(arr, 1,5))
    