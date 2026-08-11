def hoare_partion(arr , low , high):

    pivot = arr[low]

    i = low - 1
    j = high +1

    while True:

        i +=1

        while  arr[i] < pivot:

            i+=1

        j-=1

        while arr[j] > pivot:
            j-=1

        if i >= j:
            return j 
        arr[i], arr[j] = arr[j] , arr[i]

def quick_Sort(arr, low , high):

    if  low < high:

        p = hoare_partion(arr , low , high)

        quick_Sort(arr , low, p)

        quick_Sort(arr, p+1 , high)

arr = [8, 13, 6, 9, 12, 5, 11]

quick_Sort(arr, 0, len(arr) - 1)

print(arr)