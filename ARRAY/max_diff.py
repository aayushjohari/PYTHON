def max_diff(arr):

    res=  arr[1] - arr[0]

    min_val = arr[0]

    for i in range(1 , len(arr)):

        res = max(res , arr[i] - min_val)

        min_val= min(arr[i] , min_val)

    return res

arr = [2,3,10,3,4,4,2,1]

print(max_diff(arr))


def max_diff2(nums):

            if len(nums) <2:
                 return 0

            max_diff = -1
            min_val = nums[0]

            for i in range(1 , len(nums)):
                if nums[i] > min_val:
                    max_diff = max(max_diff , nums[i] - min_val)

                else:
                    min_val = nums[i]

            return max_diff

arr = [2,3,10,3,4,4,2,1]
print(max_diff2(arr))