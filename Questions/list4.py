# You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into one sorted list. The resulting list should also be in non-decreasing order.

def merge_two_sorted_lists(list1, list2):
    
    result  =[]
    i=0
    j=0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i = i+1 
        else:
            result.append(list2[j])
            j = j +1 
            
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

a = []
b = []
a_input = input("enter the list1: ").split()
for i in a_input:
    a.append(int(i))

b_input = input("enter the list1: ").split()
for i in b_input:
    b.append(int(i))

print(merge_two_sorted_lists(a,b))