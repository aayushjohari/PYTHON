# Move zeros
# Two Sum
# Missing number
# Majority element
# Maximum subarray sum (Kadane's Algorithm)

# Strings

# Reverse string
# Palindrome
# Anagram
# Character frequency
# First non-repeating character

# Searching & Sorting

# Linear search
# Binary search
# Bubble sort
# Selection sort
# Insertion sort
# Know time + space complexity

# Basic patterns

# Two pointers
# Sliding window
# Hashing / dictionary

def left_rotation(arr , d):

    rotate(arr ,0 , d-1)

    rotate(arr , d , len(arr)-1)

    rotate(arr,  0 , len(arr)-1)

    return arr

def rotate(arr, left , right):

    while left  < right:

        arr[left] , arr[right] = arr[right] , arr[left]

        left+=1

        right-=1

arr = [1, 2, 3, 4, 5]
d = 2

print(left_rotation(arr, d))
