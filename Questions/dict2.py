# Design a Python function named merge_lists_to_dictionary to merge two lists into a dictionary where elements from the first list act as keys and elements from the second list act as values.

def merge_lists_to_dictionary(keys, values):
    
    if (len(keys) != len(values)):
        return False
    else:
        return dict(zip(keys , values))
    
k =[]
keys_input = input("Keys: ").split()
for i in keys_input:
    if i.isdigit():
        k.append(int(i))
    else:
        k.append(i)

val =[]
val_input = input("Values: ").split()
for i in val_input:
    if i.isdigit():
        val.append(int(i))
    else:
        val.append(i)

print(merge_lists_to_dictionary(k , val))
