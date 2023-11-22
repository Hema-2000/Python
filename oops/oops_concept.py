#the main advantage of oops concept is reusabilty and security
#class is a collection of data members(attributes) or function members(methods)
#object is a instance of class or it is used to represent the class
#features of oops
'''
1.Encapsulation - it is the process of providing restrictions to access variables  and methods.
  it is mainly used to prevent data modifications
2.Abstaction - it is the process of hiding implementation and provide services.
  it is mainly used to provide essential attributes and hides unnecessary information.
3.Polymorphism - it descirbes the situation in which something occurs in many different forms.
  for example operator or method shows different behaviour when we pass different data types
  --> static polymorphism - method overloading
  --> Dynamic polymorphism - method overriding
4.Inheritence - it is the process of creating new class from existing class .
  existing class- parent class orsuper class or base class
  new class- child class or derived class
  the main purpose is code reusability and extensibility
  -->single- process to create new class from single base class
  -->multiple- process of creating new class from two or more base classes
  -->multi level- process of creating new class from already derived class
  -->hierarchical- process of creating multiple child class from single base class
  -->hybrid- it is combination of above inheritances
'''


#how to create a class
class Student:
    '''This is student class for display
    student details'''
    # help(Student)
s = Student()
print(s.__doc__)


#constructor is used to initialise the data to variables
#self is used to access current class members
#constructor is executed when we create object to a class
#we can create any no. of objects to a class, for every object constructor object will execute once
