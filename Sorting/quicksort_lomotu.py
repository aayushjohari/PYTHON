def quick_sort(arr, low , high):

    if  low < high :

        p = lomuto_partition(arr , low, high)

        quick_sort(arr , low , p-1)

        quick_sort(arr , p+1 , high)


def lomuto_partition(arr, low , high):

    pivot = arr[high]

    pos = low

    for i in range(low ,high):

        if arr[i] <= pivot:

            arr[i] , arr[pos] = arr[pos] , arr[i]

            pos += 1

    arr[pos] , arr[high] = arr[high] , arr[pos]

    return pos

arr = [8, 13, 6, 9, 12, 5, 11]

quick_sort(arr, 0, len(arr) - 1)

print(arr)