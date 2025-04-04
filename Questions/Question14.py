## COUNT THE LENGTH OF THE STRING WITHOUT USING THE LENGTH FUNCTION


str = input("enter the string :  " )

counter = 0

for i in str:
    if i == " ": #skipping the spaces
        continue
    counter = counter + 1

print(counter)