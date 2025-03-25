# Find the Largest Element in a List

# Write a Python function that finds and returns the largest element in a given list of integers.

def find_largest(numbers):
    largest  = numbers[0]
    for i in range (len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

print(find_largest([1,3,2,5,4]))