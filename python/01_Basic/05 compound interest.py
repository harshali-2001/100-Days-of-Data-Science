# Python Program for Compound Interest

# A = P(1 + R/100) t 
# Compound Interest = A – P 

def compound_interest(p , r , t):
    amount = p * pow((1+ r/100) , t)
    ci = amount - p
    
    print("the amount is : " , amount)
    print("The simple interest is : " , ci)


p = int(input("Enter principal : "))
r = int(input("Enter rate of interest : "))
t = int(input("Enter time period :"))

compound_interest(p , r ,t)

