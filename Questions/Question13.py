## Print all the prime numbers containing between the given numbers 

lower  = int(input("Enter the lower number: "))
upper = int(input("enter the upper number: "))

for i in range(lower , upper+1):
    for j in range(2 , i):
        if i%j == 0:
            break
    else:
        print(i)