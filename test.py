#it import sample module and it calls the function in sample module
#in f1 function it checks it is from main or not
#if it is in main means it takes from individual program only but this is from other file so it is executed from other file

#import sample
#sample.f1()

#importing mutiple modules

# from sample import *
# from sample2 import *
# f1()
# f1()
# print(a)
#output:
#executed from another program
# sample file to import mutiple modules
# sample file to import mutiple modules
# 5

#latest module i.e.,sample2 got effected so to avoid this
# in the below manner multiple modules will be imported

from sample import *
f1()
from sample2 import *
f1()
print(a)
#output:
# executed from another program
# executed from another program
# sample file to import mutiple modules
# 5


#it gives module name and methods or variables or classes in that module
#help(sample)

