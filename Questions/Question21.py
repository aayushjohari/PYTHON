###``: Write a program that will take a decimal number as input and prints out the binary equivalent of the number

n = int(input("Enter the number: "))

l=[]

while n>0:
    l.append(n%2)
    n = n//2
    # print(n , l)

for i in l[::-1]:
    print(i , end="")   