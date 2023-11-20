#calculate square using lambda
square=lambda x:x**2
print(square(5))

#calculate multiplication
mul=lambda x,y:x*y
print(mul(2,5))

#lambda function with in another function and return a function using lambda
def my_fun(n):
    return lambda x:x*n
cal=my_fun(3)
print(cal(2))


#using lambda for sorting
l=[("banana",50),("apple",20),("cherry",80)]
list_sorted=sorted(l,key=lambda x:x[1])
print(list_sorted)


l=["cherry","banana","apple"]
list_sorted=sorted(l,key=lambda x:x[-1])
print(list_sorted)



#list comprehension using lambda
lis=[1,2,3,4,5,6]
new_lis=[(lambda x:x**2)(x) for x in lis]
print(new_lis)


