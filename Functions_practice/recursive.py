#printing numbers
def printing(n):
    if(n>0):
        print(n-1)
        printing(n-1)
        print(n) #this value at starting stores at instruction pointer
        #after the function calling completed then it retrives one by one from back

print("starting in main")
printing(5)
print("end of the main")


#factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


#fabinocci series
def recur_fab(n):
    if n<=1:
        return n
    else:
        return(recur_fab(n-1)+recur_fab(n-2))
n=10
if n<=0:
    print("invaid number")
else:
    print("fabinocci series")
    for i in range(n):
        print(recur_fab(i))


#sum of natural numbers
def s(n):
    if n==1:
        return 1
    else:
        return n+s(n-1)
print(s(5))


#calculate power
def power(base,p):
    if p==0:
        return 1
    else:
        return base*power(base,p-1)
print("{} to the power of {} is {}".format(3,4,power(3,4)))


#sum of each digit in a num
def sumDigits(no):
    if no == 0:
        return 0
    else :
        return int(no % 10) + sumDigits(int(no / 10))
nums = int(input("Enter a number: "))
print("The sum is:", sumDigits(nums))


ist1 = [1, "Hello", 3.4, "Hello", 1]
print(ist1)