n=int(input("enter the number:\n"))
def sumN(n):
    if(n==1):
        return 1
    if(n>1):
        return n+sumN(n-1)
       
print("the sum of first",n,"natural numbers is :",sumN(n))

