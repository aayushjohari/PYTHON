### `Problem 2`: Print the following pattern.


# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n  = int(input("Enter the number: "))

for i in range(0 , n):
    for j in range(0, i+1):
        print("*" , end=" ")
    
    print()

for k in range(n-1 ,0,-1):
    for l in range(k , 0,-1):
        print("*" , end=" ")
    print()
