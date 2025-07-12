#Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
with open("FILE/file.txt","r") as f:
    l=f.read()
    print(l)
    if("fup" in l):
        print("present")
    else:
        print("no")