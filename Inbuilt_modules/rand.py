from random import *

#random() print float values between 0 to 1
for i in range(5):
    print(random())

#randint() is used print random numbers between given numbers
for i in range(10):
    print(randint(1, 20))


#uniform() is used print random float values between given numbers
for i in range(10):
    print(uniform(1, 20))


#randrange() will generates within a range and in step
for i in range(5):
    print(randrange(1,20,2))


#choice function will not generate random values but it generated random object
l=["hema",23,89.1,"latha",65]
x=choice(l)
print(x,type(x))


