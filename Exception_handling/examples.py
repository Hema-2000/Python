l=[1,2,3,4]
#IndexError: list index out of range
# print(l[5])
try:
    print(l[5])
# except:
#     print("invalid index")
except IndexError as msg:
    print(msg)


#using else statement in try , except block
n=int(input())
try:
    assert n%2==0 #assert keyword is used to produce boolean expression
    #if it is true it does nothing and continues the execution but if false it stops execution and throws error
except:
    print("it is not even number")
else:
    print("it is a even number")
    print(1/n)


#The raise error keyword raises a value error with the message
s = 'apple'
try:
    num = int(s)
except ValueError:
    raise ValueError("String can't be changed into integer")

def abc(x,y):
    try:
        c=((x+y)/(x-y))
    except ZeroDivisionError as msg:
        print(msg)
    else:
        print(c)
abc(2,3)
abc(2,2)


