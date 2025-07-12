#method to work in file without closing it
str="\nbye"
with open("FILE/file.txt","a+") as f:
    print(f.read())
    f.write(str)
    f.seek(0)
    r=f.readlines()
    print(r)


