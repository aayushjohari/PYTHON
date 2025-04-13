# Design a Python function named merge_three_dictionaries to merge exactly three dictionaries into one.

def merge_three_dictionaries(dict1, dict2, dict3):
    return dict1 | dict2 | dict3

def get_dict():
    d = {}
    k = []
    val = []
    k_input = input("enter keys: ").split()
    val_input = input("enter  values: ").split()

    for i in k_input:
        if i.isdigit():
            k.append(int(i))
        else:
            k.append(i)
    for i in val_input:
        if i.isdigit():
            val.append(int(i))
        else:
            val.append(i)

    if len(k) != len(val):
        print("no. of keys and values must be same")
        return {}
    else:
        for key , value in zip(k , val):
            d[key] = value
        return d
    
print("Enter Dictionary 1:")
dict1 = get_dict()

print("Enter Dictionary 2:")
dict2 = get_dict()

print("Enter Dictionary 3:")
dict3 = get_dict()


merged = merge_three_dictionaries(dict1, dict2, dict3)
print("Merged Dictionary:", merged)
        

