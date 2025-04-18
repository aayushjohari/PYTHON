def int_to_binary(n):
    # Your code here
    if n ==0:
        return "0"
        
    is_negative = n < 0
    n = abs(n)
    
    
    result = []
    while n > 0 :
        result.append(str(n%2))
        n = n // 2
    binary = ''.join(result[::-1])
    return '-' + binary if is_negative else binary

n = int(input("enter the number: "))
print(int_to_binary(n))