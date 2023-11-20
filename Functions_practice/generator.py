#without yield example program
def square(n):
    res=[]
    for i in range(n):
        res.append(2**i)
    return res
res=square(5)
print(res)

#yield keyword to return a value and temporarily suspend the function's execution.
def squ(n):
    for i in range(n):
        yield 2**i
print(list(squ(5)))


#counting of numbers
def count_range(n):
    i=1
    while i<n:
        yield i
        i+=1
print(list(count_range(10)))



#simple generator
def gene():
    yield "hi"
    yield "hello"
    yield "how r u"

r=gene()
print(next(r))
print(next(r))
print(next(r))

#geometric sequence program
def seq(num,factor):
    value=num
    while True:
        yield value
        value*=factor
g=seq(2,3)
print(next(g))
print(next(g))
print(next(g))
print(next(g))


