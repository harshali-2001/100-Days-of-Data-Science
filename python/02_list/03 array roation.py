# Python Program for Array Rotation

def rotate(arr, d ):
    temp = []
    n = len(arr)
    for i in range(d ,n):
        temp.append(arr[i])
    
    for j in range(d):
        temp.append(arr[j])
    
    return temp

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(arr)

print(rotate(arr , 2))