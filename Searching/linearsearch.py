def linear_Search(arr , x ):

    for i in range(len(arr)):

        if arr[i] == x:

            return i
        return "ELEMENT NOT FOUND"

arr = [1,2,3,4,5,6,7]
print(linear_Search(arr , 0))