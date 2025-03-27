### Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

x1 = float(input("enter the x1 coordinaate: "))
x2 = float(input("enter the x2 coordinaate: "))
y1 = float(input("enter the y1 coordinaate: "))
y2 = float(input("enter the x2 coordinaate: "))

distance  = ((x1-x2)**2 + (y2-y1)**2)**0.5

print(distance)
