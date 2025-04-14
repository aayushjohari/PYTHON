## check whether the given string is palindrome or not 

def is_palindrome(s):
    normal_string =""
    for i in s:
        if i.isalnum():
            normal_string += i.lower()
            
    low = 0
    high = len(normal_string)-1
    
    while low < high:
        if normal_string[low] != normal_string[high]:
            return False
        low += 1 
        high -= 1 
        
    return True

s = input("enter the string: ")
print(is_palindrome(s))
