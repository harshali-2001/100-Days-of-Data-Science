# Python Program to Swap Two Elements in a List

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

def swap_fun(arr , pos1 , pos2):
    n=len(arr)

    if (pos1 > n or pos1 < 0 or pos2>n or pos2 <0):
        return print("enter Postion is out of range .. plz try again")
    else:
        arr[pos1], arr[pos2] = arr[pos2] , arr[pos1]
    
    return arr


# main 
arr = [1,5,8,"Mahal",6,2, 125.45 ,6]
print("List is : " , arr)
pos1 = int(input("enter First Position : "))
pos2 = int(input("enter First Position : "))
print("List After Swapping : " , swap_fun(arr , pos1, pos2))
