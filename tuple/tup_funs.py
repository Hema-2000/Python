#creating tuple and printits id
t=(10,20,30)
print(t)
print(type(t))

#tuple using membership operator
print(10 in t)
print(100 in t)
print(100 not in t)
# sum() & max() & len() & min()
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sum(t,4))

#insert value in a tuple if we have list in a tuple
t = (4, 2, 3, [6, 5])
t[3][1] = 9
print(t)

#convert string to tuple
s="hemalatha"
t=tuple(s)
print(t, type(t))

#convert list to tuple
l=[1,2,3,4,5]
t=tuple(l)
print(t,type(t))

#packing of tuple
a=10
b=20
c=30
t=a,b,c
print(t)
print(type(t))

#unpacking of tuple
t=1,2,3
a,b,c=t
print(a,b,c)

#concatenate and repeating of tuples
a=(1,2,3)
a=a+(4,5)
print(a)
print((a)*3)

#accessing elements in tuples using indexing
t=(2,"hema",3,"sai",(5,"latha",3),6,8)
print(t[2])
print(t[-2])
print(t[-3])
print(t[4][1])
print(t[-3][-2])

#accessing elements in tuple using slicing
t=(2,"hema",3,"sai",5,"latha",31,6,8)
print(t[2:5])
print(t[:5])
print(t[:])
print(t[3:])
print(len(t))

#count & index methods
t=(10,20,30,10,20,10,10,20,10,20)
print(t.count(10)) #how many times 10 will be there in a tuple
print(t.count(100))#it got 0 as output because 100 is no there in tuple
print(t.index(30))# it gives index value of 30
#print(t.index(2))#ValueError: 2 is not in tuple


a=(1,2,0,3,8)
print(all(a)) #print true if 0 is not there in list else false
print(any(a)) #print true if any pne of the element is true else false
print(list(enumerate(a)))#along index value it prints [(0, 1), (1, 2), (2, 0), (3, 3), (4, 8)]

#creating empty tuple
t=()
print(t)