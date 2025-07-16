
n=int(input("enter : "))
tablelist=[n*i for i in range(1,11)]
print(tablelist)
with open("ADVANCED PYTHON/file.txt","a+") as f:
    f.write(str(tablelist))
