def subarray_given_sum(arr , sum):

    left  =  0
    curr = 0

    for i in range(len(arr)):

        curr+=arr[i]

        while curr > sum :

            curr = curr - arr[left]
            left +=1

        if curr == sum :
            return arr[left : i+1]

    return [-1.-1]

arr = [1, 4, 20, 3, 10, 5]
target = 33
print(subarray_given_sum(arr , target))