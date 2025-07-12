class employee:#class
    language="python and c++"#class attribute
    salary=120000
    def getinfo(self):
        print("the language is ",{self.language})
        print("salary is ",{self.salary})
    def greet(self):
        print("thnks")
    @staticmethod
    def con():
        print("have a nice day")

vanshika=employee()#object
vanshika.getinfo()
vanshika.greet()
vanshika.con()

# here id is object attribute and salary 
# and language are class object as they directly belong to the class
#instance attribute is preffered over class attribute