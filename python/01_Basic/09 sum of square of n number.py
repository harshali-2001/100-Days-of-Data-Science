

# // insertio sort 

def insertionSort(arr):
    n = len(arr)
    
    for i in range(n):
        x = arr[i]
        j = i-1
        while j>=0 and arr[j]>x:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = x 
    
    return arr
    

array = [ 12 , 13 , 5 , 6 ]

print("Sorted array : " , insertionSort(array))