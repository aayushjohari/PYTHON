def armstrong(n):
    k = len(str(n))

    sum =0

    num = n

    while n>0:
        ld = n%10
        sum = sum + (ld**k)
        n = n//10
        
    if sum == num:
        print("yes this is armstrong")

    else :
        print("no this is not armstrong")

number = int(input("enter the number: "))
armstrong(number)        