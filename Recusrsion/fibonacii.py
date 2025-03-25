def fibseries(n):
    
    arr = []
    fib_sum = 0
    for i in range(n):
        fib_num = fibonacci(i)
        arr.append(fib_num)
        fib_sum =  fib_sum + fib_num
    return arr , fib_sum

def fibonacci(n):
    if n==0:
        return 0
    elif  n==1:
        return 1
       
    ld = fibonacci(n-1)  #multiple recursion
    sld = fibonacci(n-2)
    
    return ld +sld

num  = int (input("enter the number: "))
fibser , fib_sum = (fibseries(num))
print(f"the list of the fibinaccci series till the {num} is: {fibser}")
print(f"the sum of the series is: {fib_sum} ")


