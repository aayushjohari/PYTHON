def reversenum(n):
    reverse =0
    while n>0:
        ld = n%10
        n = n//10
        reverse = (reverse *10) + ld
        
    return reverse
number = int(input("Enter a number to reverse: "))
print(reversenum(number))

