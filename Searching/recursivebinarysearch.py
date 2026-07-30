def binarysearch(arr , x  , low , high):

    if low > high:

        return  -1

    mid = (low + high) //2

    if arr[mid] == x :

        return mid

    elif arr[mid] > x :

        return binarysearch(arr , x ,low , mid -1)

    else:
        return binarysearch(arr , x ,mid+1 , high)


arr = [10,20,30,40,50,60]
print(binarysearch(arr , 60 , low= 0 , high = len(arr)-1))