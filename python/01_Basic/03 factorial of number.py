# Python Program to Find the Factorial of a Number
# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 


num = int(input("Enter a number : "))
num2 = num
fact = 1
if num <= 0:
    print("factorial can not be found.")
else:
    while num !=1 :
        fact *= num
        num = num-1

print("factotial of  {} is {}".format(num2 , fact))


