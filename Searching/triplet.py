def triplet(arr , target):

    for i in range(len(arr)-2):

        left = i+1

        right = len(arr)-1

        while left < right:

            current_Sum  = arr[i] + arr[left] + arr[right]

            if current_Sum == target:

                return [i , left , right]

            if current_Sum > target:

                right = right -1
            else:
                left = left + 1

    return False

arr = [1,2,4,5,6,8,9]
target = 15
print(triplet(arr, target))