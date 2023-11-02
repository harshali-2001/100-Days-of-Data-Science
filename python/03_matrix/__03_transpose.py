# Question: Write a Python function to find the transpose of a matrix.
# Explanation: Understanding and computing the transpose of a matrix is crucial in various applications.

x = [[3, 2 , 4],[1 , 2, 6], [7,5, 8]]


# initializa the result matrix 
result =[[0,0,0],[0,0,0],[0,0,0]]


for r in range(len(x)):
    for c in range(len(x[0])):
        result[c][r]= x[r][c]

print(result)