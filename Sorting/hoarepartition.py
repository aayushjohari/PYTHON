def hoare_partition(arr):

    pivot = arr[0]

    i =-1
    j= len(arr)

    while True:

        i+=1

        while arr[i] < pivot:
            i+=1
        j-=1

        while arr[j] > pivot:
            j-=1

        if i  >= j :
            return j 

        arr[i] , arr[j] = arr[j], arr[i]

arr= [8, 13, 6, 9, 12, 5, 11]
print(hoare_partition(arr))
print(arr)