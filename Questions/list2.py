# ###`Problem 4:` Running Sum on list
# Write a program to print a list after performing running sum on it.

# i.e:

# `Input:`
# ```
# list1 = [1,2,3,4,5,6]
# ```
# `Output:`
# ```
# [1,3,6,10,15,21]

def runningsum(lst):
    result  =[]
    sum = 0
    for i in lst:
        sum  = sum + i
        result.append(sum)
    return result

numbers =[]
input_numbers = input("Enter numbers: ").split()
for num in input_numbers:
    numbers.append(int(num))

print("Running sum of the list is: " , runningsum(numbers))