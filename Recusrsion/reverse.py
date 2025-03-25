def reverse(n):
    
    if n < 1:
        return
    print(n , end =" ")
    n = n-1
    reverse(n)

num = int(input("enter the number: "))
reverse(num)
