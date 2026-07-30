def countoneascending(arr):
    low = 0
    high = len(arr)-1
    ans  = -1

    while low <= high:
        mid = (low+ high)//2
        if arr[mid] == 1:
            ans  = mid
            high = mid -1
        else:
            low = mid +1
    if ans == -1:
        return 0
    return len(arr) - ans

arr =[0,0,0,1,1,1]
print(countoneascending(arr))