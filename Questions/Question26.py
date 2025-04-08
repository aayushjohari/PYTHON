# Count Number of Odd and Even Elements in a List

def count_even_odd(lst):
   
    count1 = 0
    count2 =0
    for i in lst:
        if i%2 == 0:
            count1 = count1 + 1
        else:
            count2 = count2 + 1 
    return (count1 , count2)

num  = []
num_input  = input("enter the numbers: ").split()
for i in num_input:
    num.append(int(i))

print(count_even_odd(num))
            
            
