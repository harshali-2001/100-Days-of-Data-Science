# Question: Create a Python function to multiply two matrices.
# Explanation: This question focuses on implementing matrix multiplication, a fundamental operation in linear algebra

x = [[3, 2 , 4],[1 , 2, 6], [7,5, 8]]
y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# initializa the result matrix 
result =[[0,0,0],[0,0,0],[0,0,0]]
for r in range(len(x)):
    for c in range(len(x[0])):
        result[r][c]= x[r][c] * y[r][c]

print(result)