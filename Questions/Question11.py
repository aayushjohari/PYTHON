###`Problem 10`: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.


lst =[]

for i in range(1000 , 3000 +1):
    flag  = True
    num = i

    while num > 0:
        last = num %10
        if last % 2 != 0:
            flag  = False
            break
        num = num// 10

    if flag:
        lst.append(str(i))


print(",".join(lst))

 
