'''
def soreted_rem_dup(arr):

    temp = [0] * len(arr)

    temp[0] = arr[0]
    
    res = 1
    for i in range(1 , len(arr)):

        if arr[i] != temp[res-1]:

            temp[res] = arr[i]

            res+=1

    return temp[:res]

arr = [10,10,20,10,40]
print(rem_dup(arr))
'''
'''
def unsorted_rem(arr):

    temp = []

    for i in range(len(arr)):

        if arr[i] not in temp:
            temp.append(arr[i])

    return temp

arr = [10,10,20,10,40]
print(unsorted_rem(arr))
'''



def remove_duplicates(arr, n):

    res = 1

    for i in range(1 , n):

        if arr[res-1] != arr[i]:

            arr[res] = arr[i]

            res+=1

    return arr[:res]

arr =[10,20,30,40,40,40]

print(remove_duplicates(arr , len(arr)))