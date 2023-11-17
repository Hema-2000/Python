import time
import threading
single thread(main thread) by using time module
def square(n):
    for i in n:
        print("the square of num:",i*i)
        time.sleep(1)
def cube(n):
    for i in n:
        print("the cube of num:",i*i*i)
        time.sleep(1)

n=[2,3,4]
square(n)
cube(n)


#creating multiple threads to reduce execution time
def square(n):
    for i in n:
        print("the square of num:",i*i)
        time.sleep(1)
def cube(n):
    for i in n:
        print("the cube of num:",i*i*i)
        time.sleep(1)

n=[2,3,4]
t1=threading.Thread(target=square,args=(n,))
t2=threading.Thread(target=cube,args=(n,))
t1.start()  #it is going to call the function
time.sleep(1)
t2.start()
print(t2.is_alive()) #check whether thread is alive or not
time.sleep(1) 
t1.join()
t2.join()   #if thread wants to wait until the other thread
print(t2.is_alive())   #it get false because thread is completed
print(t1.ident) #every thread has unique identify number
print(t2.ident)








