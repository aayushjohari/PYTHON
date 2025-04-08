# Check if All Elements in a List are Unique

def check_unique(lst):
    # Your code goes here
    seen  = set()
    for i in lst:
        if i in seen:
            return False
        seen.add(i)
    return True
lst =[]
numbers = input("Enter the sequence: ").split()
for i in numbers:
    lst.append(int(i))

print(check_unique(lst))
