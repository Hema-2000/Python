#creation of class with class keyword and class name(it must start with capital letter
class Operations:
    #below line is  constructor.it is special method in class
    #self is first parameter of constructor, it is used to access current class members
    #constructor execute automatically when we create an obj to class
    def __init__(self,a,b):
        self.x=a
        self.y=b

    #below line represents method, self is 1st parameter in method
    def add(self):
        print("the addition of 2 numbers")
        return self.x + self.y

    def mul(self):
        print("the multiplication of 2 numbers")
        return self.x * self.y

    def sub(self):
        print("the subtraction of 2 numbers")
        return self.x -self.y

    def div(self):
        if self.y != 0:
            print("float division of 2 numbers")
            return self.x / self.y
    def div2(self):
        if self.y != 0:
            print("floor division of 2 numbers")
            return self.x // self.y
    def mod(self):
        print("modulus of 2 numbers")
        return self.x % self.y