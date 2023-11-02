# pos1 = int(input("enter First Position : "))

# Input: lst = [10,20,30,40]
# Output: 4
# Explanation: The output is 4 because the length of the list is  4.


from operator import length_hint


arr = [1, 2, 8, 'Mahal', 6, 5, 125.45, 6]
# using len function
print("Length of List using len method : " , len(arr))


#  Using Length_hint

# This particular method is defined in the operator class 
# and it can also tell the no. of elements present in the list.

print("Length of List using length_hints method : " , length_hint(arr))

