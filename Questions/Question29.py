# Length of the Longest Word
# Problem Description:

# You are given a string s. Your task is to find the length of the longest word in the string. A word is defined as a sequence of characters separated by spaces. Do not use any built-in functions for string manipulation.

def longest_word_length(s):
    max_length  = 0
    current_length  = 0
    
    for char in s:
        if char != " ":
            current_length += 1 
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
            
    if current_length > max_length:
        max_length = current_length
        
    return max_length
s = input("enter the string : ")
print("The longest word count : ",longest_word_length(s))  

            
        
