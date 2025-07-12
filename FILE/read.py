f=open("FILE/file.txt","r")
# read=f.readlines()#readline read all lines and give them in a list
# print(read)
# f.seek(0)

# line=f.readline()
# print(line,type(line))
# line2=f.readline()
# print(line2)

####using while loop###auto read using readline###
line =f.readline()
while(line!= ""):
    print(line)
    line=f.readline()
f.close()
