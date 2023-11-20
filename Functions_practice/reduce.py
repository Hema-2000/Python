from functools import *
def add(a,b):
    return a+b
l=[1,2,3,4]
output=reduce(add,l)
print(reduce(lambda x,y:x+y , l))#reduce with lambda
print("with an iniitial value "+ str(reduce(lambda x,y:x+y , l,10))) #we can also use like this
print(output)

#to find max value in a list 
l=[2,6,4,8,1]
print(reduce(lambda x,y: x if x>y else y , l))


from itertools import *
r1=list(accumulate(l,lambda x,y:x+y))#[2, 8, 12, 20, 21]
print(r1)
r2=reduce(lambda x,y:x+y,l)#21
print(r2)

