# Python Program to Find Sum of Array

def sum1(array):
    sum = 0
    for i in range(len(array)):
        sum = sum + array[i]
    return sum

def sum2(array):
    ans = sum(array)
    return ans
 

array = [12, 3, 4, 15 ]
print("the sum of array is " , sum2(array) )
