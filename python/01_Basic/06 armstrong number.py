# Python Program to Check Armstrong Number

def armstrong(num):
    ans = num
    n = len(str(num))
    sum = 0
    while num!=0:
        remainder = num%10
        sum = sum + remainder**n
        num = num//10

    if sum == ans:
        return print("{} is a armstrong number".format(ans))
    else:
        return print("{} is a not armstrong number".format(ans))



num = int(input("enter a number to check if armstrong "))

armstrong(num)