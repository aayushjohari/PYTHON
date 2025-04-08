# find the largest element in the list 

def largest(lst):
    largest  = lst[0]
    for i in range(0 , len(lst)):
        if lst[i] > largest:
            largest = lst[i]
    return largest

num  = []
input_num  = input("enter the list: ").split()
for i in input_num:
    num.append(i)

print(largest(num))
        
    

