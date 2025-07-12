words=["bad","ganda","donkey"]
with open ("FILE/practice/donkey.txt","r") as f:
    a=f.read()
    for word in words:
        a=a.replace(word,"######")
        with open ("FILE/practice/donkey.txt","w") as f:
            f.write(a)
