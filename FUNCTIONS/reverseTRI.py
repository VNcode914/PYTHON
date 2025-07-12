n=int(input("enter the number:\n"))
def REVtriangle():
    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end="")
        print()       
REVtriangle()

