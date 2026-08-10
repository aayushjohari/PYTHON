def merge(arr):
    low = 0
    high = len(arr)-1

    mid = (low+high)//2

    left = arr[:mid+1]
    right = arr[mid+1:]

    i = j= 0
    k= low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            k+=1

    while i < len(left):
        arr[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1

    return arr

arr = [2,6,10,2,4]
print(merge(arr))