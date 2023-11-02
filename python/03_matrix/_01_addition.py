# Question: Write a Python function to add or subtract two matrices.
# Explanation: This question will help you understand basic operations on matrices.

x = [[3, 2 , 4],[1 , 2, 6], [7,5, 8]]
y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# initializa the result matrix 
result =[[0,0,0],[0,0,0],[0,0,0]]
for r in range(len(x)):
    for c in range(len(x[0])):
        result[r][c]= x[r][c] + y[r][c]

print(result)

