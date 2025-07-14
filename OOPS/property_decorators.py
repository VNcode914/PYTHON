class employee:
    a=3
    @classmethod#when u dont want to take instant attribcls
    def name(self):
        print("your name is good",self.a)

    @property
    def id(self):
        print(self.fname,self.lname)
    @id.setter
    def id(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[2]

e=employee()
e.a=32
e.id="hi bye true"
print(e.fname,e.lname)
e.name()


