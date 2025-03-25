# num  = int (input("Enter the number : "))

# if num > 0:
#     print("the number is positive")
#     if num%2 ==0:
#         print("the number is even")
#     else:
#         print("the number is odd")

# else:
#     print("the number is zero or negative")


# num  = int(input("enter the number : ").strip())
# sum = 0
# count  = 1

# while count <= num:
#     sum  = sum  + count 
#     count  = count + 1

# print ("the sum of n natural numbers  = " , sum)


def func(n):
    a=n**2
    return a

n = int(input("enter the number to get the square : "))
print(func(n))