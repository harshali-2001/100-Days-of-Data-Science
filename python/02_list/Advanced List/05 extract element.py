# Python – Extract elements with Frequency greater than K


"""
input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
Output : [4, 3] 
"""
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3
# Using lambda function and list comprehension
result = [x for x in set(test_list) if test_list.count(x) > K]
print("Extracted elemenents from the list having greater frequency : " , result)

