# Check if element exists in list in Python

# Input: test_list = [1, 6, 3, 5, 3, 4]
#             3  # Check if 3 exist or not.
# Output: True
# Explanation: The output is True because the element we are looking is exist in the list.


test_list = [1, 6, 3, 5, 3, 4]
i = int(input("enter the number :"))

if i in test_list:
    print("exits")
else:
    print("not exits ")
