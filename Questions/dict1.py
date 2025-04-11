# Given a dictionary with values list, extract key whose value has most unique values.

# Input:

# ```bash
# test_dict = {"Campus" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
# ```

# Output:
# ```bash
# Campus

test_dict = {"Campus" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
max_val =0
max_key =""
for i in test_dict:
    if max_val < len(set(test_dict[i])):
        max_val = len(set(test_dict[i]))
        max_key = i
print(max_key)