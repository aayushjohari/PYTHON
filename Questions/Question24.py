# Reverse words in a given String

s = input("Enter the string: ")

reverse =[]

for i in s.split():
    reverse.append(i)

reverse = reverse[::-1]
print(" ".join(reverse))