class number:
    def __init__(self,n,h):
        self.n=n
        self.h=h
    def __add__(self,num):
        return self.n+num.n
    def __len__(self):
        return len(str(self.h))
n=number(1,"hello")
m=number(2,"")
h="hello"
print(n+m)
print(len(n))
