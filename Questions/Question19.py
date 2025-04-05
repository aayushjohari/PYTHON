### `Problem 5`: Write a Python Program to Find the Sum of the Series till the nth term:<br>
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user


x = int(int(input("Enter the x: ")))
n  = int(input("Enter the n: "))

sum = 1
series = "1"

for i in range(2 , n+1):
    sum  = sum  + x**i/i
    series = series + f"+{x}^{i}/{i}"

print(series)
print(sum)
