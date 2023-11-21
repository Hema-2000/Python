#below 2 lines gives same output but when we have single class in a module
#from advanced_python.arithmetic import Operations
#from advanced_python.arithmetic import *

#alias name for class
#from advanced_python.arithmetic import Operations as op
#obj=op(30,6)

#below 2 lines are not working because package and main.py both are not in same directory
#import advanced_python
#obj=advanced_python.arithmetic.Operations(30,6)

#importing arithmetic module from advanced_python package
from advanced_python import arithmetic

#creating object to instantiate the class
obj=arithmetic.Operations(30,6)

#calling methods within operations class through created object
sum=obj.add()
print(sum)

diff=obj.sub()
print(diff)

multi=obj.mul()
print(multi)

float_division=obj.div()
print(float_division)

floor_division=obj.div2()
print(floor_division)

modulus=obj.mod()
print(modulus)







