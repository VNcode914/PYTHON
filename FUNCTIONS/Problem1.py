a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
def greatest(a,b,c):
    if(a>b and a>c):
       print(a,"is the greatest") 
    if(b>a and b>c):
        print(b,"is the greatest")
    if(c>a and c>b):
        print(c,"is the greatest")
greatest(a,b,c)

   

