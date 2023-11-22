#instance variable-value of variable is varied from one object to another object

class Instance:
    def __init__(self):
        self.a=10 #inside the constructor we can declare instance variables using self
        self.b=20

    def fun(self):
        self.c=30 #inside instance method also we can declare instance variables using self
        print("with in a class")
        print(self.a)#
        print(self.b)
        print(self.c)

obj=Instance()
obj.d=40 # outside of class we can declare instance variables by using object
print(obj.d)
print("instance variables")
obj.fun()
print("instance variables outside the class")
print(obj.a)
print(obj.b)