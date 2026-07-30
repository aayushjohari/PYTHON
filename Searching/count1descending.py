def countonedescending(arr):
    low = 0
    high = len(arr)-1
    ans  = -1

    while low <= high:
        mid = (low+ high)//2
        if arr[mid] == 1:
            ans  = mid
            low= mid +1
        else:
            high= mid -1
    if ans == -1:
        return 0
    return ans + 1

arr =[1,1,1,1,1,1,0,0]
print(countonedescending(arr))