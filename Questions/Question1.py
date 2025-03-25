# Sum of List Elements

# Write a Python function that calculates the sum of all elements in a given list of integers.

def sum_list(numbers):
    
    sum =0
    for i in range(0 , len(numbers)):
        sum = sum + numbers[i] 
    return sum

print(sum_list([1,2,3,4,5]))