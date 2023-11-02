# Python – Remove empty List from List

test_list = [5, 6, [], 3, [], [], 9]
new1 = []
#  method 1 to remove empty list
for i in test_list:
    if i!=[]:
        new1.append(i)
print("orignal list : " , test_list)
print("After removing empty list (Method 1) : " , new1)

# method 2 to remove empty list

while [] in test_list:
    test_list.remove([])

print("After removing empty list (Method 2) : " , test_list)

