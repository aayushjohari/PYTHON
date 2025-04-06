#  Check whether the string is Symmetrical.

# Code here
s = input("Enter the string: ")

if len(s)%2 == 0:
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2:]
else:
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2+1:]

if s1 == s2:
    print("the given string is symmetrical")
else:
    print("the given string is not symmetrical")
