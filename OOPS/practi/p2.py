class animal:
    def __init__(self):
        print("i love animals")

class pets(animal):
    def __init__(self):
        print("pets are dogs")

class dogs(pets):
    @staticmethod
    def bark():
        print("dogs always bark")
d=dogs()
d.bark()