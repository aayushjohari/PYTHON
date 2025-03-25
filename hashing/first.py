def counting(n , arr):
    num = int(input("enter the number you want to count: "))
    
    count =0
    for i in range(n):
        if arr[i] == num:
            count  = count  +1
    return count 

arr = []
number = input("enter the array: ").split()
for i in number:
    arr.append(int(i))

n = len(arr)

if __name__ == "__main__":
    print(counting(n , arr))