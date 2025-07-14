class employee:
    a=3
    @classmethod#when u dont want to take instant attribcls
    def name(cls):
        print("your name is good ",cls.a)

e=employee()
e.a=32
e.name()