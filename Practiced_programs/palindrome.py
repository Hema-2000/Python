#to check given number is palindrome or not after converting it into string

num=int(input("enter the number to check"))
s=str(num)
r=s[::-1]
# print("".join(reversed(s)))
if s==r:
    print("the given num is palindrome")
else:
    print("given number is not palindrome")



#to check given number after converting string or string is palindrome or not through recursion
def is_palindrome(s):
    if len(s)<1:
        return True
    else:
        if s[0]==s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

s=input("enter the string")
r=is_palindrome(s)
if r== True:
    print("palindrome")

else:
    print("not palindrome")



#to check given int number is palindrome or not through recursion
def reverse(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+str(reverse(n//10)))
def is_palindrome(n):
    if n==reverse(n):
        return True
    else:
        return False
n=int(input("enter the number:"))
r=is_palindrome(n)
if r==True:
    print("palindrome")
else:
    print("not palindrome")

