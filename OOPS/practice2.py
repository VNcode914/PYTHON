import math
class calculator:
    @staticmethod
    def greet():
        print("hello")
    def __init__(self,n):
        self.n=n
    def square(self):
        print("the square is ",{self.n*self.n})
    def square_root(self):
        print("the square root is ",{self.n**1/2})
    def cube(self):
        print("the cube is ",{self.n*self.n*self.n})
    
calc=calculator(4)
calc.greet()
calc.square()
calc.cube()
calc.square_root()

