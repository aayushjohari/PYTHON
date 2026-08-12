'''
def max_sub_variable(arr, k):

    maximum =  0

    for i in range(len(arr)):

        curr =0

        for j in range(i, len(arr)):

            curr = curr + arr[j]

            if curr <= k :
                length  = j-i+1
                maximum = max(length  , maximum)

    return maximum

arr = [2, 1, 5, 1, 3, 2]
k = 7
print(max_sub_variable(arr , k))
'''

def max_subarray_variable(arr , k):

    left = 0
    maxlength = 0
    curr = 0

    for right in range(len(arr)):
        curr += arr[right]

        while curr > k:
            curr -=arr[left]
            left+=1

        length = right - left +1
        maxlength = max(maxlength , length)

    return maxlength


arr = [2, 1, 5, 1, 3, 2]
k = 7
print(max_subarray_variable(arr, k))