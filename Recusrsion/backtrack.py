def backtrack(i ,n):

    if  i > n :
        return
    
    backtrack(i+1  ,n)
    print(i)

num = int(input("enter the number: "))
backtrack( 1 , num)

