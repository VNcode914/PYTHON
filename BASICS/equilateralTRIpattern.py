n=int(input("enter a number"))
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,2*i+1):
        print("*",end="")
    for j in range(0,n-i):
        print(" ",end="")
    print()
    