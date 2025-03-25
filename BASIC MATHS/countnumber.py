def countdigit(n):
    count =0
    while n>0:
        n = n//10
        count = count +1
    return  count

number = int(input("enter the number: "))
print(countdigit(number))

