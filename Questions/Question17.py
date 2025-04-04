## convert the integer into string without using the typcasting function like str()

s = int(input("ENTER THE NUMBER: "))

digits ="0123456789"

result =" "

while s != 0:
    result = digits[s%10] + result
    s = s //10

print(result)
print(type(result))