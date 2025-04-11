# Multiply Adjacent elements (both side) and take sum of right and left side multiplication result.

# For eg.
# ```
# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication :

# (1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

# output-(5, 40, 91, 136, 80)


t = ()
t_input = input("enter the tuple: ").split()
for i in t_input:
    t = t + (int(i) ,)

l =[]

l.append(t[0]*t[1])

for i in range(1 , len(t)-1):
    l.append(t[i]*t[i-1]+t[i]*t[i+1])

l.append(t[-1]*t[-2])
print(tuple(l))




