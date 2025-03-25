count  = 0
def count_num(n):
    global count
   
    if count  == n:
        # print(count)
        return
    
    print(count)
    count = count +1
    count_num(n)

num  = int(input("enter the  number: "))
count_num(num)
    


# def count_num(i , n):
    
#     if i  == n:
#         return
    
#     print(i)
#     i = i+1
#     count_num(i , n)

# num = int(input("enter the number: "))
# count_num(1, num)
