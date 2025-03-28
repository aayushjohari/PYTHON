### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

p = int(input("Enter the amount: "))
r = float(input("enter the rate: "))
t = float(input("enter the time: "))

interest  = (p*r*t)/100

print("The interest will be: " , interest)