def print_name(i , n):

    if i > n:
        return
    print("Aayush")
    i = i+1
    print_name(i , n)

if __name__=="__main__":
    num = int(input("enter the name : "))
    print_name(1 , num)