
#x is a golbal variable so we can access anywhere in the program
x=10

def f1():
    a=100
    print("a=",a)
    print("x=",x+10)

def f2():
    b=200
    print("b=",b)
    print("x=",x)

f1()
f2()


#declare sample class
class sample:
    x=10           #class variables or attributes or data member
    def f1(self):  #method or function member
        a=100      # local variable to method f1
        print("a=",a)
        print("x=",sample.x)
    def f2(self):    #method , self is the first or default parameter in class
        b=200        # local variable to f2
        print("b=",b)
        print("x=",sample.x)
    def f3(self):
        print("Current Object is",self)
        self.f1()
        self.f2() #"." is accessing operator used to access the members in a class


# x f1 and f2 are called members of a class sample
# will use . operator to access the members of a class. it(.) is member accessing operator

obj=sample() #creating object to a class
obj.f3()#calling f3() throgh created object
print("x value is",obj.x) #printing global variable with in a class through created class object



class test:
#data memebers and function memebers
    def read_data(self):
        test.a=eval(input("Enter a value"))
        test.b=eval(input("Enter b Value"))
    def print_data(self):
        print("A value is",test.a)
        print("B value is",test.b)
    def __init__(self):
        a=0
        b=0
        print("\n I am in constructor menthod")
        print("a=",a,"b=",b)

#creating object to above class
test_obj=test() #when we create an object then first it implements init function thats is constructor method
test_obj.read_data()
test_obj.print_data()


#with constructor
class Student: #student is name of the class
 def __init__(self): #it is constuctor or initializer method and self is for reference to instance of class
     #instance attributes
     self.sid=123
     self.sname="sai"
     self.saddress="hyderabad"
 #instance method
 def display(self):
     print("Student id is:",self.sid)
     print("Student name is:",self.sname)
     print("Student address is:",self.saddress)

s1=Student()
s2=Student()
s1.display()
s2.display()

#without constructor

class Student:
    def getdata(self):
        self.sid=int(input("Enter sid:"))
        self.sname=input("Enter sname:")
        self.saddress=input("Enter saddress:")

    def display(self):
        print("Student id is:",self.sid)
        print("Student name is:",self.sname)
        print("Student address is:",self.saddress)

s1=Student()
s1.getdata()
s1.display()


#without display method
class Student:
    def __init__(self,x,y,z):
        self.sid=x
        self.sname=y
        self.saddress=z

s1=Student(101,"sai","hyderabad")#passing arguments to constructor
s2=Student(102,"mohan","sr nagar")#we can create any number of objects for a single class
print(s1.__dict__) #it is used to print s1 ina dictionary form
print(s2.__dict__)