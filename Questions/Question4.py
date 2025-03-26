# You are given a list of integers. Write a Python program that reverses the list without using slicing (lst[::-1]). The program should return the reversed list.

def reverse_list(lst):
    
    low = 0
    high = len(lst) - 1
    while low < high :
        lst[low] , lst[high] = lst[high] , lst[low]
        low = low + 1 
        high = high - 1 
        
    return lst

lst = [1,2,3,4,5]
print(reverse_list(lst))
