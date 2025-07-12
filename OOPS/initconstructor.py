class employee:#class
    # language="python and c++"
    # salary=120000
    # def getinfo(self):
    #     print("the language is ",{self.language})
    #     print("salary is ",{self.salary})
    # def greet(self):
    #     print("thnks")
    # @staticmethod
    # def con():
    #     print("have a nice day")
    def __init__(self,name,salary,language,id):#dunder methods auto called before all the function
        print("this is from the _init_")
        self.name=name
        self.language=language
        self.salary=salary
        self.id=id

vanshika=employee("vanshika",2870274,"c++",101)
print(vanshika.id,vanshika.salary,vanshika.language,vanshika.name)
# vanshika.getinfo()
# vanshika.greet()
# vanshika.con()
