### **Problem 12:** Create Short Form from initial character
# Given a string create short form ofthe string from Initial character. Short form should be capitalised.

s = input("enter the string: ")

s_2 = " "

for i in s.split():
    s_2 = s_2 + i[0].upper()

print(s_2)