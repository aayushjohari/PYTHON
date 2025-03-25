def divisors(n):
    for i in range(1  , n+1):
        if n%i==0:
            print(i)
    return i

number = int(input("enter the number: "))
divisors(number)
                             