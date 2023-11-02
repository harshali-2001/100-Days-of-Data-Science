# Python program to interchange first and last elements in a list

# swap function

def swap_fun(arr):
    arr[0] , arr[-1] = arr[-1] , arr[0]


    return arr


arr = [1,5,8,9,6,2,5,6]
print("Original List :" , arr)
print("After Swapping FIrst and Last element in the list : " , swap_fun(arr))