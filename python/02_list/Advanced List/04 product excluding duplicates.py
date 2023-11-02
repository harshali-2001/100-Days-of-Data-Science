# Python – List product excluding duplicates
import math
input_list = [1, 3, 5, 6, 3, 5, 6, 1]
new_list = set(input_list)
prodcut = math.prod(new_list)
print("Product of list: ", prodcut)