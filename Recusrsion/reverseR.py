# # first approach by taking the new array
# def print1(arr, n):
#     print("THE REVERSE OF THE array :  ")
#     for i in range(n):
#         print(arr[i] , end =" ")
#     # print()

# def reverse(arr , n):
#     arr2 = [0]*n
#     for i in range(n-1 , -1 ,-1):
#         arr2[n-i-1] = arr[i]
#     print1(arr2 , n)

# num = []
# number= input("enter the numbers: ").split()
# for i in number:
#     num.append(int(i))  # num = [int(i) for i in numbers]
# n = len(num)

# reverse(num , n)

# second approach by having the same array

# def printarray(arr , n):
#     print("the reverse of the array : ")
#     for i in range(n):
#         print(arr[i] , end =" ")

# def reverse_array(arr , n):
#     low = 0
#     high = n-1
#     while low < high:
#         temp = arr[low]
#         arr[low] = arr[high]
#         arr[high] = temp
#         # arr[low] , arr[high] = arr[high] , arr[low]
#         low = low+1
#         high = high-1
#     printarray(arr , n)

# if __name__=="__main__":
#     num =[]
#     numbers = input("enter the number: ").split()
#     for i in numbers:
#         num.append(int(i))
#     size = len(num)

#     reverse_array(num , size)

# through recursion

def print_array(arr , n):
    print("the reverse :  ")
    for i in range(n):
        print(arr[i] , end =" ")

def reverse(arr , low , high):
    if low< high:
        arr[low] , arr[high] = arr[high] , arr[low]
        reverse(arr , low+1 , high-1)

if __name__=="__main__":
    num =[]
    numbers = input("enter the number: ").split()
    for i in numbers:
        num.append(int(i))
    size = len(num)

    reverse(num , 0 , size -1)
    print_array(num , size)