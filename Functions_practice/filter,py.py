def scr(n):
    return n>50
scores=[40,50,20,60,100,110,140,130,10,45]
res1=list(filter(scr,scores))#using filter
res=list(map(scr,scores))#using map
res2=list(filter(lambda x:x>50,scores))#lambda and filter
print(res2)
print(res1)
print(res)


#to check given string is palindrome or not
l=["madam","hema","tat","kok","frog"]
res=list(filter(lambda x:x==x[::-1],l))
res1=list(map(lambda x:x==x[::-1],l))
print(res)
print(res1)

def my_fun(s):
    return s[-1]=="a"
fruits=["apple","banana","guava","pineapple"]
output=list(filter(my_fun,fruits))
res=list(filter(lambda x:x[-1]=='a',fruits)) #filter with lambda function
print(output)
print(res)

