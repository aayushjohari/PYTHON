def gcd(n1,n2):
    gcd =1
    for i in range(1 , min(n1,n2)+1):
        if  n1%i==0 and n2%i==0 :
            gcd =i
            
        return gcd

num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
print(gcd(num1 , num2))