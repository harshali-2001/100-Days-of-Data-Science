# Python program to find the sum of all items in a dictionary

my_dict = {'a': 100, 'b': 200, 'c': 300}

add = 0
for i in my_dict.values():
    add = add+i
print(add)