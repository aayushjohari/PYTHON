def fact(n):

    if n == 0:
        return 1
    
    return n* fact(n-1)
    
    
    
# if __name__ == "__main__":
#    num = int(input("enter the number:  "))
#    print(fact(num))
   
   

num  = int(input("enter the number: "))
print(fact(num))