# You are given two strings s and t. Your task is to check if the two strings are equal. Two strings are considered equal if they have the same length and the same characters at each position. You are not allowed to use any built-in string comparison functions.

def are_equal_strings(s, t):
    if len(s) != len(t):
        return False
        
    for i in range(len(s)):
        if s[i]!= t[i]:
           return False
    return True
        

s = input("enter the first string: ")
t = input("enter the second string: ")

print(are_equal_strings(s,t))
