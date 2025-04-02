# ###`Problem 11`: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# ```
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# ```
# > The numbers after the direction are steps.

# > `!` means robot stop there.

pos =[0,0]
while True:
    s = input("enter the position: ")
    if s == "!":
        break
    direction  = s.split()[0]
    steps = int(s.split()[1])

    if direction  =="UP":
        pos[1] = pos[1] + steps
    elif direction  == "Down":
        pos[1] = pos[1] + steps
    elif direction  == "RIGHT":
        pos[0] = pos[0] + steps
    elif direction  ==  "LEFT" :
        pos[0] = pos[0] - steps
    else:
        pass
print("new pos" , pos)
print((pos[0]**2 +pos[1]**2)**0.5)


