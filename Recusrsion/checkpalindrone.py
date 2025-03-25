def palindrome(n):

    low = 0
    high =  len(n)-1

    while low < high:
        if n[low] != n[high]:
            return False
        low = low+1
        high = high-1
    return True


n  = input("enter here: ")
print(palindrome(n))





