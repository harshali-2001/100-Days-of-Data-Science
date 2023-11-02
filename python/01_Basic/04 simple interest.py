# 
# Simple interest formula is given by: Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate
def simple_interest(p , r , t):
    print("/n/n/nThe principal is " , p)
    print("The time period is" , t)
    print("the rate of interest is " , r)
    si = (p*r*t)/100
    
    print("The simple interest is : " , si)


p = int(input("Enter principal : "))
t = int(input("Enter time period :"))
r = int(input("Enter rate of interest : "))

simple_interest(p , r ,t)




