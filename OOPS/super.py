class employee:
    a=1
class programmer(employee):
    b=2
    def __init__(self):
        print("programmer")
class manager(programmer):
    def __init__(self):
        super().__init__()
    c=3
o=manager()
print(o.a,o.b,o.c)