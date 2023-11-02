# Python program to find the Strongest Neighbour

arr = [1,2,2,3,4,5]

result = list(i for i in arr if arr[i] < arr[i+1] and arr[i]> arr[i-1])

print(result)

