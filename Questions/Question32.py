# You are given a string s. Your task is to remove duplicate characters from the string while preserving the order of the first occurrences and return the modified string.


def remove_duplicates(s):
    
    seen  = set()
    result  = ''
    for char in s :
        if char not in seen:
            seen.add(char) 
            result += char 
            
    return result 

s = input("enter the string: ")
print(remove_duplicates(s))
            
