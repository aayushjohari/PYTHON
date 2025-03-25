def sum_num( i , sum):

    if  i < 1:
     print(sum)
     return
    
    sum_num(i-1 , sum +i)
num  = int(input("enter the number: "))
sum_num(num , 0)
    
