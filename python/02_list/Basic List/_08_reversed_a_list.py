# Reversing a List in Python

# Input: list = [4, 5, 6, 7, 8, 9]
# Output: [9, 8, 7, 6, 5, 4] 

# using slicing technique

List = [4, 5, 6, 7, 8, 9]
print("given List" , List)
new_list = List[::-1]
print("After reversed by slicing method : " , new_list)

List.reverse()
print("Using reverse() ", List)
 
print("Using reversed() ", list(reversed(List)))