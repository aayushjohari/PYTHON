def functional_count(n):
    if n==0:
        return 0
    
    return n+functional_count(n-1)

num = int(input("enter the number: "))
print(functional_count(num))
