#converting into upper case
l=["hema","sravani","tanu"]
upper_str=list(map(str.upper,l))
print(upper_str)

#using round()
circle_areas = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]
res=list(map(round,circle_areas,range(len(circle_areas))))
print(res)

#using zip()
my_char=["hema","sravs","krupa"]
my_num=[20,30,40]
print(list(zip(my_char,my_num)))


def my_fun(s):
    return s[-1]=="a"
fruits=["apple","banana","guava","pineapple"]
output=list(map(my_fun,fruits))
res=list(map(lambda x:x[-1]=='a',fruits)) #map with lambda function
print(output)
print(res)


