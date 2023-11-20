#SyntaxError: '(' was never closed
a=print("hello"
print(a)

#runtime errors
#ValueError: invalid literal for int() with base 10: 's'
a=int(input("enter the integer value"))
print(a)

#NameError: name 'A' is not defined. Did you mean: 'a'?
a="Hemalatha"
print(A)

#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(10+"abc")

#ZeroDivisionError: division by zero
print(10/0)

#sometimes we can solve run time error by logical implementation
a=int(input("enter the first value"))
b=int(input("enter the second value"))
if b==0:
    print("second num can't be 0")
else:
    print(a/b)


#all the time logical implementation is not possible so go with exception handling

