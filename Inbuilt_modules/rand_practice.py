from random import *
#to know the current working directory
# import os
# current_directory = os.getcwd()
# print(f"Current Working Directory: {current_directory}")

#package path is appended in current module
import sys
sys.path.append('C:/Users/dell/PycharmProjects/pythonProject4')

from advanced_python import arithmetic

obj=arithmetic.Operations(30,6)

l=["+","-","*","/","//","%"]
x=choice(l)
print(x)
if x=="+":
    print(obj.add())
elif x=="-":
    print(obj.sub())
elif x=="*":
    print(obj.mul())
elif x=="/":
    print(obj.div())
elif x=="//":
    print(obj.div2())
elif x=="%":
    print(obj.mod())
else:
    print("invalid choice")

