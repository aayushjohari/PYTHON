# Check if All Elements in a List are Unique

def check_unique(lst):
    # Your code goes here
    seen  = set()
    for i in lst:
        if i in seen:
            return False
        seen.add(i)
    return True

print(check_unique([1 ,2,3,4,5 ,5]))
print(check_unique([1,2,3,4,5]))