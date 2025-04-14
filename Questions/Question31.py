# You are given a string s. Your task is to count the number of words in the string and return the total count. A word is defined as a sequence of characters separated by spaces.

def count_words(s):
    count  = 0
    word  = False
    
    for char in s:
        if char != " ":
            if not word:
                word = True
                count  += 1
                
        else:
            word = False
    return count
    
s = input("enter the string : ")

print(count_words(s))