# convert into binary into decimal


def binary_to_decimal(binary_str):
    
    decimal = 0
    length = len(binary_str)
    for i in range(length):
        if binary_str[length - 1 - i] == '1':
            decimal += 2**i
    return decimal

n = input("enter the number: ")
print(binary_to_decimal(n))
