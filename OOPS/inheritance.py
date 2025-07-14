# class abc:
#     p="vanshika"
#     def hello(self):
#         print("hello😎")
# class rst:
#     p="kabu"
#     def hello1(self):
#         print("bye🙌")
# class xyz(abc,rst):#multiple inheritance
#     p="devansh"
#     def hello2(self):
#         print("hru?🤞🤞")
# b=xyz()
# b.hello()
# b.hello2()
# b.hello1()
class employee:
    a=1
class programmer(employee):
    b=2
class manager(programmer):
    c=3
o=manager()
print(o.a,o.b,o.c)