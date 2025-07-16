class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,num):
        return complex(self.real+num.real,self.img+num.img)
    def __str__(self):
        return f"Addition is:{self.real}+{self.img}i"
    def __mul__(self,num):
        return complex(self.real*num.real,self.img*num.img)
    def __str__(self):
        return f"Multiplication is:{self.real}+{self.img}i"

n=complex(7,4)
m=complex(2,4)
add=n+m
mul=n*m
print(add)
print(mul)
