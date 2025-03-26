# Maximum difference between two consecutive elements in a list.

def max_consecutive_difference(lst):
    # Your code goes here
    if len(lst) < 2:
        return 0
    max_diff = lst[0]
    for i in range(1 ,len(lst)):
        diff = abs(lst[i] - lst[i-1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

lst = [1,7,3,10,5]
print(max_consecutive_difference(lst))