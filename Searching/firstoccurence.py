def binarySearch(arr , x):

    low = 0

    high = len(arr)-1

    ans =-1

    while low <= high:

        mid = (low + high)//2

        if arr[mid] == x :

            ans = mid

            high = mid -1

        elif arr[mid] < x :

            low = mid +1

        else:

            high = mid -1

    return ans
arr = [10,20,20,20,30,40]
print(binarySearch(arr , 20))