# Check if Tuple is Palindromic

def is_palindromic_tuple(tup):
   
    mid = len(tup) // 2
    
    if len(tup) % 2 == 0:
       
        first_half = tup[:mid]
        second_half = tup[mid:]
    else:
        first_half = tup[:mid]
        second_half = tup[mid+1:]
        
    return first_half == second_half[::-1]


tup = ()
input_tup = input("Enter the tuple:  ").split()
for i in input_tup:
    if i.isdigit():
        tup = tup + (int(i) ,)
    else:
        tup = tup + (i ,) 

print(is_palindromic_tuple(tup))
    