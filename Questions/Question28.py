# An integer representing the total count of vowels in the input string.

def count_vowels(s):
    count  = 0
    vowels = "AEIOUaeiou"
    for i in s:
        if i in vowels:
            count  += 1 
    return count

s = input("Enter the string: ")

print(count_vowels(s))

