#using try except and finally block
a=int(input("enter the 1st value"))
b=int(input("enter the second value"))
try:
    print(a/b)
#default except block
except:
    print("something went wrong")
finally:
    print("this is final block...mainly finally block is used to deallocate the resources after try block excution")



#using same example with specific except block
a=int(input("enter the 1st value"))
b=int(input("enter the second value"))
try:
    print(a/b)
#specific except block
except ZeroDivisionError as msg:
    print(msg)
finally:
    print("this is final block...mainly finally block is used to deallocate the resources after try block excution")


#multi except blocks
try:
    a = int(input("Enter Num1:"))
    b = int(input("Enter Num2:"))
    print("result is:", a / b)
#in how many types multi except blocks can write
except ZeroDivisionError as msg:
    print(msg)
# except ValueError as msg:
# except (ZeroDivisionError,ValueError) as msg:
# except Exception as msg:
    print(msg)
finally:
    print("done with finally block")


#when we use both default and specific except block then we first suggest specific
try:
    a = int(input("Enter Num1:"))
    b = int(input("Enter Num2:"))
    print("result is:", a / b)
except:                            #SyntaxError: default 'except:' must be last
    print("something went wrong")
except ZeroDivisionError as msg:
    print(msg)